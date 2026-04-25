import os
from pathlib import Path

def check_env():
    print("--- Environment Audit ---")
    context_path = Path(".agents/context.md")
    if context_path.exists():
        print(f"[FOUND] {context_path.absolute()}")
        print("Contents:")
        print(context_path.read_text(encoding="utf-8"))
    else:
        print(f"[NOT FOUND] {context_path.absolute()}")
    
    # Check for basic project-level defines if any
    # (Simplified for now)
    print("Environment check complete.")

if __name__ == "__main__":
    check_env()
