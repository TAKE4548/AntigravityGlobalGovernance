import sys
import os
import re
from pathlib import Path

"""
AntiGravity Artifact Linter (XML Structured Edition)
Validates implementation_plan.md and walkthrough.md for governance compliance.
Usage: python artifact_linter.py <path_to_directory_or_file>
"""

REQUIRED_PLAN_SECTIONS = [
    r"## Proposed Changes",
    r"## Trade-off Disclosure",
]

WALKTHROUGH_TABLE_PATTERN = r"\|.*ID.*\|.*要件.*\|.*結果.*\|"

def lint_plan(content):
    errors = []
    for section in REQUIRED_PLAN_SECTIONS:
        if not re.search(section, content, re.IGNORECASE):
            errors.append(f"Missing required section: {section}")
    return errors

def lint_walkthrough(content):
    errors = []
    if not re.search(WALKTHROUGH_TABLE_PATTERN, content):
        errors.append("Missing AC Compliance Table (Markdown table with ID, 要件, 結果)")
    return errors

def check_file(file_path):
    path = Path(file_path)
    if not path.exists():
        return [f"File not found: {file_path}"]

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    errors = []
    if "implementation_plan.md" in path.name:
        errors = lint_plan(content)
    elif "walkthrough.md" in path.name:
        errors = lint_walkthrough(content)
    
    return errors

def main():
    if len(sys.argv) < 2:
        print("<linter_report>\n  <status>Error</status>\n  <message>Usage: python artifact_linter.py <path></message>\n</linter_report>")
        sys.exit(1)

    target_path = Path(sys.argv[1])
    all_errors = {}

    files_to_check = []
    if target_path.is_file():
        files_to_check.append(target_path)
    elif target_path.is_dir():
        for f in target_path.glob("*.md"):
            if "implementation_plan.md" in f.name or "walkthrough.md" in f.name:
                files_to_check.append(f)
    
    for f in files_to_check:
        errs = check_file(f)
        if errs:
            all_errors[str(f.name)] = errs

    print("<linter_report>")
    if not all_errors:
        print("  <status>PASS</status>")
        print("  <message>All checked artifacts comply with governance rules.</message>")
    else:
        print("  <status>FAIL</status>")
        print("  <audit_findings>")
        for file, errs in all_errors.items():
            print(f"    <file name='{file}'>")
            for e in errs:
                print(f"      <error>{e}</error>")
            print("    </file>")
        print("  </audit_findings>")
    print("</linter_report>")

    if all_errors:
        sys.exit(1)

if __name__ == "__main__":
    main()
