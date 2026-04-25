import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Dispatch PBI-SYS to child repositories.")
    parser.add_argument("--source", required=True, help="Path to PBI-SYS definition")
    parser.add_argument("--targets", required=True, help="Comma-separated child repository paths")
    
    args = parser.parse_args()
    
    print(f"# Dispatching {args.source} to {args.targets}")
    print("\n[INFO] This is a placeholder for the pbi_dispatcher.py.")
    print("In production, this would parse the source PBI and create child PBIs in ready state.")
    
    targets = args.targets.split(",")
    for target in targets:
        print(f"Creating child PBI in {target.strip()}/docs/backlog/pbi/active/...")

if __name__ == "__main__":
    main()
