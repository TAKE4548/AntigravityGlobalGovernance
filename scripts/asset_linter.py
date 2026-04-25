import re
import os
import sys
import json
from pathlib import Path

def detect_project_type():
    """Detects the project type based on existence of specific files and their content."""
    # 1. Frontend check (Vite/React)
    pkg_json = Path("package.json")
    if pkg_json.exists():
        try:
            content = json.loads(pkg_json.read_text(encoding="utf-8"))
            deps = content.get("dependencies", {})
            dev_deps = content.get("devDependencies", {})
            # Common markers for modern frontend projects
            if "vite" in dev_deps or "react" in deps or "next" in deps:
                return "frontend-vite-react"
        except:
            pass
        return "frontend-generic"

    # 2. Backend check (Python/FastAPI/Streamlit)
    req_txt = Path("requirements.txt")
    pyproj = Path("pyproject.toml")
    if req_txt.exists() or pyproj.exists():
        content = ""
        if req_txt.exists():
            content = req_txt.read_text(encoding="utf-8")
        elif pyproj.exists():
            content = pyproj.read_text(encoding="utf-8")
            
        if "fastapi" in content.lower():
            return "python-fastapi"
        if "streamlit" in content.lower():
            return "python-streamlit"
        return "python-generic"

    return "unknown"

def lint_frontend_vite():
    """Standard checks for modern Frontend projects."""
    print("  -> Running Frontend Checks...")
    errors = []
    # Essential directories for the project conventions
    essential_dirs = [Path("src"), Path("src/components")]
    for d in essential_dirs:
      if not d.exists():
        errors.append(f"Missing essential directory: {d}")
    
    # Configuration files check
    config_files = [Path("vite.config.ts"), Path("tailwind.config.js")]
    for f in config_files:
      if not f.exists():
        # Only warn as these might have different names (e.g. .mjs, .cjs)
        print(f"  [INFO] Optional config file {f} not found.")
        
    return errors

def lint_python_backend():
    """Standard checks for Python/Backend projects."""
    print("  -> Running Python Backend Checks...")
    errors = []
    # Check for core source directory
    if not (Path("src").exists() or Path("app").exists() or Path("main.py").exists()):
        errors.append("Could not find a standard Python source structure (src/, app/, or main.py)")
    
    if not Path("docs").exists():
        print("  [INFO] No docs directory found.")
        
    return errors

def lint_legacy_icons():
    """Legacy check for projects using a specific icon mapping file."""
    ICON_PY_PATH = Path("src/components/icons.py")
    ICON_DIR = Path("assets/icons")
    
    if not ICON_PY_PATH.exists() or not ICON_DIR.exists():
        return [] # Silently skip if this pattern doesn't apply

    print("  -> Running Legacy Icon Synchronization Checks...")
    errors = []
    try:
        content = ICON_PY_PATH.read_text(encoding="utf-8")
        map_match = re.search(r'ICON_MAP = \{(.*?)\}', content, re.DOTALL)
        if not map_match:
            errors.append("ICON_MAP not found in icons.py even though file exists.")
            return errors
            
        map_content = map_match.group(1)
        pattern = r'"([^"]+)":\s*(?:"([^"]+)"|None)'
        matches = re.findall(pattern, map_content)
        icon_map_definitions = {k: v for k, v in matches if v}
        
        actual_files = {f.relative_to(ICON_DIR).as_posix() for f in ICON_DIR.rglob("*") if f.is_file()}
        
        for key, filename in icon_map_definitions.items():
            if filename not in actual_files:
                errors.append(f"Linked in ICON_MAP but missing from disk: '{filename}' (Key: {key})")
        
        defined_filenames = set(icon_map_definitions.values())
        for filename in actual_files:
            if filename not in defined_filenames:
                errors.append(f"Icon exists on disk but not defined in ICON_MAP: '{filename}'")
    except Exception as e:
        errors.append(f"Error during legacy icon lint: {e}")
            
    return errors

def main():
    proj_type = detect_project_type()
    print(f"Project Type Detected: {proj_type}")
    
    all_errors = []
    
    # 1. Run type-specific linters
    if proj_type.startswith("frontend"):
        all_errors.extend(lint_frontend_vite())
    elif proj_type.startswith("python"):
        all_errors.extend(lint_python_backend())
    
    # 2. Run conditional pattern-based linters (Legacy support)
    all_errors.extend(lint_legacy_icons())
    
    # Final Result
    if all_errors:
        print("\nAsset Lint Errors Found:")
        for err in all_errors:
            print(f"  [FAIL] {err}")
        sys.exit(1)
    
    print("\nAsset Lint: [PASS]")
    sys.exit(0)

if __name__ == "__main__":
    main()
