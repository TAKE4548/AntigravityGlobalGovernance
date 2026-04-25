import os
import re
import sys

# Regex for absolute paths (Windows style)
ABS_PATH_PATTERN = re.compile(r'C:\\Users\\[\w.-]+', re.IGNORECASE)

# Regex for common API keys/secrets
SECRET_PATTERNS = {
    "OpenAI API Key": re.compile(r'sk-[a-zA-Z0-9]{48}'),
    "Google API Key": re.compile(r'AIza[0-9A-Za-z-_]{35}'),
    "GitHub Token": re.compile(r'ghp_[a-zA-Z0-9]{36}'),
    "Generic Secret": re.compile(r'(password|secret|key|token)\s*[:=]\s*["\'][^"\']{8,}["\']', re.IGNORECASE)
}

EXCLUDE_DIRS = {".git", "node_modules", "__pycache__", ".next", "dist", "build", "brain"}
EXCLUDE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".ico", ".pdf", ".zip", ".exe"}
EXCLUDE_FILES = {"context.md", "linter_output.txt", "audit_report.md"}

def scan_file(file_path):
    findings = []
    # Skip excluded files by name
    if os.path.basename(file_path) in EXCLUDE_FILES:
        return findings
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            for i, line in enumerate(f, 1):
                # Check for absolute paths
                if ABS_PATH_PATTERN.search(line):
                    findings.append({
                        "line": i,
                        "type": "Absolute Path",
                        "content": line.strip()
                    })
                
                # Check for secrets
                for name, pattern in SECRET_PATTERNS.items():
                    if pattern.search(line):
                        findings.append({
                            "line": i,
                            "type": f"Secret ({name})",
                            "content": "[REDACTED]"
                        })
    except Exception as e:
        # print(f"Error reading {file_path}: {e}")
        pass
    return findings

def main():
    root_dir = "."
    if len(sys.argv) > 1:
        root_dir = sys.argv[1]

    all_findings = {}
    
    for root, dirs, files in os.walk(root_dir):
        # Prune excluded directories
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in EXCLUDE_EXTS:
                continue
            
            file_path = os.path.join(root, file)
            findings = scan_file(file_path)
            if findings:
                all_findings[file_path] = findings

    if all_findings:
        print(" [!] Security Audit Failed: Absolute paths or secrets detected.")
        print("-" * 60)
        for path, findings in all_findings.items():
            print(f"FILE: {path}")
            for f in findings:
                print(f"  L{f['line']}: [{f['type']}] {f['content']}")
            print("-" * 60)
        sys.exit(1)
    else:
        print(" [OK] Security Audit Passed: No absolute paths or secrets found.")
        sys.exit(0)

if __name__ == "__main__":
    main()
