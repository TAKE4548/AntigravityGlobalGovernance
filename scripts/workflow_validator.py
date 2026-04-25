import sys
import os
from pathlib import Path

def validate(command, pbi_id):
    print(f"--- Workflow Validator: {command} for PBI {pbi_id} ---")
    
    if command == "design-end":
        required_files = [
            f"docs/design/PBI-{pbi_id}.md",
            f"docs/design/PBI-{pbi_id}-test-plan.md"
        ]
        success = True
        for f in required_files:
            if not Path(f).exists():
                print(f"[FAIL] Missing: {f}")
                success = False
            else:
                print(f"[PASS] Found: {f}")
        
        # Check tasks directory
        tasks_dir = Path("docs/tasks")
        if not tasks_dir.exists() or not any(tasks_dir.iterdir()):
            print("[FAIL] No tasks found in docs/tasks/")
            success = False
        else:
            print("[PASS] Tasks generated in docs/tasks/")
            
        if not success:
            sys.exit(1)

    elif command == "verify-ready":
        # Support both old monolithic and new sharded structure
        backlog_old = Path(".ai-backlog.md")
        backlog_sharded = Path(f"docs/backlog/task/active/{pbi_id}.md")
        
        if backlog_sharded.exists():
            print(f"[PASS] Found sharded task file: {backlog_sharded}")
            content = backlog_sharded.read_text(encoding="utf-8")
            if "[ ]" in content or "[/]" in content:
                print(f"[FAIL] There are still uncompleted tasks in {backlog_sharded}")
                sys.exit(1)
            print("[PASS] All tasks marked as [x].")
        elif backlog_old.exists():
            print(f"[PASS] Found legacy .ai-backlog.md")
            content = backlog_old.read_text(encoding="utf-8")
            if "@pending" in content:
                print("[FAIL] There are still @pending tasks in .ai-backlog.md")
                sys.exit(1)
            print("[PASS] All tasks marked as @done.")
        else:
            print("[FAIL] No task tracking file found (.ai-backlog.md or docs/backlog/task/active/REQ-XXX.md)")
            sys.exit(1)

    print("Validation successful.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: workflow_validator.py <command> <pbi_id>")
        sys.exit(1)
    validate(sys.argv[1], sys.argv[2])
