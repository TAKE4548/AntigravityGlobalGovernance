import sys
import argparse
import os
import re

def extract_tag_content(text, tag_name):
    pattern = rf"<{tag_name}>(.*?)</{tag_name}>"
    match = re.search(pattern, text, re.DOTALL)
    return match.group(1).strip() if match else None

def main():
    parser = argparse.ArgumentParser(description="Dispatch PBI-SYS to child repositories using XML tags.")
    parser.add_argument("--source", required=True, help="Path to PBI-SYS definition")
    parser.add_argument("--targets", required=True, help="Comma-separated child repository paths")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.source):
        print(f"<dispatch_report>\n  <status>Error</status>\n  <message>Source file not found: {args.source}</message>\n</dispatch_report>")
        sys.exit(1)
        
    with open(args.source, "r", encoding="utf-8") as f:
        content = f.read()
    
    system_context = extract_tag_content(content, "system_context")
    frontend_spec = extract_tag_content(content, "frontend_pbi_spec")
    backend_spec = extract_tag_content(content, "backend_pbi_spec")
    
    targets = [t.strip() for t in args.targets.split(",")]
    
    print("<dispatch_report>")
    print(f"  <source>{args.source}</source>")
    print("  <actions>")
    
    for target in targets:
        spec = None
        repo_type = ""
        if "frontend" in target.lower():
            spec = frontend_spec
            repo_type = "Frontend"
        elif "backend" in target.lower():
            spec = backend_spec
            repo_type = "Backend"
            
        if spec:
            # Generate target PBI ID (simplified for placeholder)
            pbi_id_match = re.search(r"REQ-(\d+)", args.source)
            pbi_id = f"REQ-{pbi_id_match.group(1)}" if pbi_id_match else "REQ-UNKNOWN"
            
            target_dir = os.path.join(target, "docs/backlog/pbi/active")
            os.makedirs(target_dir, exist_ok=True)
            target_file = os.path.join(target_dir, f"{pbi_id}.md")
            
            with open(target_file, "w", encoding="utf-8") as out:
                out.write(f"--- \nstatus: ready \nsource: system_dispatch \n---\n\n")
                if system_context:
                    out.write(f"## System Context\n{system_context}\n\n")
                out.write(spec)
                
            print(f"    <action status='Success'>Dispatched {repo_type} spec to {target_file}</action>")
        else:
            print(f"    <action status='Skipped'>No spec found for {target}</action>")
            
    print("  </actions>")
    print("</dispatch_report>")

if __name__ == "__main__":
    main()
