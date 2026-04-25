import re
import sys
import os
import yaml
from pathlib import Path

# Config
BACKLOG_PATH = Path("docs/backlog.md")
SHARDED_PBI_DIR = Path("docs/backlog/pbi")
SESSION_PATH = Path("docs/session.md")
VALID_STATUSES = {"new", "ready", "in-progress", "fix-needed", "needs-investigation", "done", "archived", "completed"}

def lint_backlog_monolithic():
    if not BACKLOG_PATH.exists():
        return None # Not monolithic

    content = BACKLOG_PATH.read_text(encoding="utf-8")
    errors = []
    
    # 1. Check for REQ IDs
    req_matches = re.findall(r"### (REQ-\d+):", content)
    seen_ids = set()
    for req_id in req_matches:
        if req_id in seen_ids:
            errors.append(f"Duplicate REQ ID: {req_id}")
        seen_ids.add(req_id)

    # 2. Check Status and Date
    req_blocks = re.split(r"### REQ-\d+:", content)[1:]
    
    for i, block in enumerate(req_blocks):
        req_id = req_matches[i]
        status_match = re.search(r"- \*\*Status\*\*: ([\w-]+)(?:\s*\((.*?)\))?", block)
        if not status_match:
            errors.append(f"{req_id}: Status not found or malformed.")
            continue
            
        status = status_match.group(1).lower()
        date_str = status_match.group(2)
        
        if status not in VALID_STATUSES:
            errors.append(f"{req_id}: Invalid status '{status}'. Valid: {list(VALID_STATUSES)}")
            
        if status == "done" or status == "completed":
            if not date_str or not re.match(r"\d{4}-\d{2}-\d{2}", date_str):
                errors.append(f"{req_id}: Status is '{status}' but missing or invalid date (YYYY-MM-DD). Found: '{date_str}'")

    return errors

def lint_backlog_sharded():
    if not SHARDED_PBI_DIR.exists():
        return None # Not sharded
        
    errors = []
    pbi_files = []
    for d in ["active", "archive"]:
        pbi_dir = SHARDED_PBI_DIR / d
        if pbi_dir.exists():
            pbi_files.extend(list(pbi_dir.glob("*.md")))
            
    seen_ids = set()
    for pbi_file in pbi_files:
        content = pbi_file.read_text(encoding="utf-8")
        parts = content.split("---")
        if len(parts) < 3:
            errors.append(f"{pbi_file.name}: Missing frontmatter.")
            continue
            
        try:
            fm = yaml.safe_load(parts[1])
        except Exception as e:
            errors.append(f"{pbi_file.name}: Invalid YAML frontmatter: {e}")
            continue
            
        req_id = fm.get("id")
        if not req_id:
            errors.append(f"{pbi_file.name}: Missing 'id' in frontmatter.")
            continue
            
        if req_id in seen_ids:
            errors.append(f"Duplicate REQ ID: {req_id} (found in {pbi_file.name})")
        seen_ids.add(req_id)
        
        status = fm.get("status", "").lower()
        if status not in VALID_STATUSES:
            errors.append(f"{req_id}: Invalid status '{status}'.")
            
        # Check matching filename
        if f"{req_id}.md" != pbi_file.name:
            errors.append(f"{pbi_file.name}: Filename does not match ID '{req_id}'.")
            
        # Check actual content matches frontmatter
        status_match = re.search(r"- \*\*Status\*\*: ([\w-]+)(?:\s*\((.*?)\))?", parts[2])
        if status_match:
            content_status = status_match.group(1).lower()
            if content_status != status:
                errors.append(f"{req_id}: Frontmatter status '{status}' does not match content status '{content_status}'.")
            
            date_str = status_match.group(2)
            if status == "done" or status == "completed":
                if not date_str or not re.match(r"\d{4}-\d{2}-\d{2}", date_str):
                    errors.append(f"{req_id}: Status is '{status}' but missing or invalid date (YYYY-MM-DD).")
                    
    return errors

def lint_session(is_sharded=False):
    if not SESSION_PATH.exists():
        return True
        
    content = SESSION_PATH.read_text(encoding="utf-8")
    active_req_match = re.search(r"- \*\*Active REQ\*\*: (REQ-\d+)", content)
    status_match = re.search(r"- \*\*Status\*\*: (\w+)", content)
    
    if active_req_match and status_match:
        active_req = active_req_match.group(1)
        status = status_match.group(1)
        
        if status == "active":
            if is_sharded:
                pbi_path = SHARDED_PBI_DIR / "active" / f"{active_req}.md"
                if not pbi_path.exists():
                    print(f"Warning: Session has active {active_req}, but sharded PBI file not found in active dir.")
                else:
                    pbi_content = pbi_path.read_text(encoding="utf-8")
                    status_match = re.search(r"status: ([\w-]+)", pbi_content)
                    if status_match:
                        backlog_status = status_match.group(1).lower()
                        if backlog_status != "in-progress":
                             print(f"Warning: Session has active {active_req}, but backlog status is '{backlog_status}'.")
            elif BACKLOG_PATH.exists():
                backlog_content = BACKLOG_PATH.read_text(encoding="utf-8")
                req_block = re.search(rf"### {active_req}:.*?- \*\*Status\*\*: ([\w-]+)", backlog_content, re.DOTALL)
                if req_block:
                    backlog_status = req_block.group(1).lower()
                    if backlog_status != "in-progress":
                        print(f"Warning: Session has active {active_req}, but backlog status is '{backlog_status}'.")

    return True

if __name__ == "__main__":
    errors = lint_backlog_monolithic()
    is_sharded = False
    if errors is None:
        errors = lint_backlog_sharded()
        is_sharded = True
        
    if errors is None:
        print("Error: No backlog found (monolithic or sharded).")
        sys.exit(1)
        
    if errors:
        print("Backlog Lint Errors:")
        for err in errors:
            print(f"  [FAIL] {err}")
        sys.exit(1)
    
    print("Backlog Lint: [PASS]")
    lint_session(is_sharded)
    sys.exit(0)
