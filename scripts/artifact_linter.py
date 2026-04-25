import sys
import os
import re
from pathlib import Path

"""
AntiGravity Artifact Linter
Validates implementation_plan.md and walkthrough.md for governance compliance.
Usage: python artifact_linter.py <path_to_directory_or_file>
"""

REQUIRED_PLAN_SECTIONS = [
    r"## Proposed Changes",
    r"## Trade-off Disclosure",
    r"## SSoT Validation", # Added for Architecture-First
]

WALKTHROUGH_TABLE_PATTERN = r"\|.*ID.*\|.*要件.*\|.*結果.*\|"

SSOT_KEYWORDS = [
    "openapi.yaml",
    "SPEC.md",
    "docs/system",
    "DESIGN_SYSTEM.md",
    "E2E_BACKLOG.md"
]

def lint_plan(content, file_path):
    errors = []
    for section in REQUIRED_PLAN_SECTIONS:
        if not re.search(section, content, re.IGNORECASE):
            errors.append(f"Missing required section: {section}")
    
    # Check if SSoT Validation mentions any doc updates or explicit reasoning
    ssot_section = re.search(r"## SSoT Validation(.*?)(?=##|$)", content, re.S | re.I)
    if ssot_section:
        ssot_text = ssot_section.group(1).lower()
        if not any(kw in ssot_text for kw in SSOT_KEYWORDS) and "not required" not in ssot_text:
            errors.append("SSoT Validation section must mention updated documents or state 'Not Required' with reasoning.")

    # Check for [MUST] labels in plan
    if re.search(r"## Proposed Changes", content):
        # Optional: check if files are labeled with [MODIFY], [NEW], etc.
        pass
    
    return errors

def lint_walkthrough(content, file_path):
    errors = []
    if not re.search(WALKTHROUGH_TABLE_PATTERN, content):
        errors.append("Missing AC Compliance Table (Markdown table with ID, 要件, 結果)")
    
    return errors

REQUIRED_TASK_SECTIONS = [
    r"## 2\. 密閉コンテキスト",
    r"### 2\.1 必須の型定義",
    r"### 2\.2 既存の対象コード",
]

REQUIRED_TEST_PLAN_SECTIONS = [
    r"## 1\. 自動テスト",
    r"## 2\. ツール主導監査",
]

def lint_task(content, file_path):
    errors = []
    for section in REQUIRED_TASK_SECTIONS:
        if not re.search(section, content, re.IGNORECASE):
            errors.append(f"Missing required section: {section}")
    
    # Check for empty snippets
    if re.search(r"### 2\.1 必須の型定義\n```\w*\n// 関連する", content):
        errors.append("Task Card has placeholder in '2.1 必須の型定義'. Please paste actual snippets.")
    if re.search(r"### 2\.2 既存の対象コード\n```\w*\n// 修正対象となる", content):
        errors.append("Task Card has placeholder in '2.2 既存の対象コード'. Please paste actual snippets.")
    
    return errors

def lint_test_plan(content, file_path):
    errors = []
    for section in REQUIRED_TEST_PLAN_SECTIONS:
        if not re.search(section, content, re.IGNORECASE):
            errors.append(f"Missing required section: {section}")
    
    if "pytest" not in content and "npm" not in content and "vitest" not in content:
        errors.append("Test plan must contain a specific execution command (pytest, npm, etc.)")
    
    return errors

def check_file(file_path):
    path = Path(file_path)
    if not path.exists():
        print(f"[ERROR] File not found: {file_path}")
        return False

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    errors = []
    if "implementation_plan.md" in path.name:
        print(f"Linting Implementation Plan: {path.name}")
        errors = lint_plan(content, path)
    elif "walkthrough.md" in path.name:
        print(f"Linting Walkthrough: {path.name}")
        errors = lint_walkthrough(content, path)
    elif "REQ-" in path.name and "task/active" in str(path):
        print(f"Linting Task Card: {path.name}")
        errors = lint_task(content, path)
    elif "test-plan.md" in path.name:
        print(f"Linting Test Plan: {path.name}")
        errors = lint_test_plan(content, path)
    else:
        # Default: check for common issues if requested
        return True

    if errors:
        for err in errors:
            print(f"  [FAIL] {err}")
        return False
    else:
        print("  [PASS] Governance check successful.")
        return True

def main():
    if len(sys.argv) < 2:
        print("Usage: python artifact_linter.py <path>")
        sys.exit(1)

    target_path = Path(sys.argv[1])
    success = True

    if target_path.is_file():
        success = check_file(target_path)
    elif target_path.is_dir():
        # Specifically check brain folders if it looks like one
        for f in target_path.glob("*.md"):
            if "implementation_plan.md" in f.name or "walkthrough.md" in f.name:
                if not check_file(f):
                    success = False
    else:
        print(f"[ERROR] Invalid path: {target_path}")
        sys.exit(1)

    if not success:
        sys.exit(1)
    print("Linting completed successfully.")

if __name__ == "__main__":
    main()
