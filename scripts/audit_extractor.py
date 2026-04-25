import subprocess
import os
import sys

def get_tracked_files():
    try:
        # Get list of tracked files using git ls-files
        result = subprocess.run(['git', 'ls-files'], capture_output=True, text=True, check=True)
        files = result.stdout.splitlines()
        return files
    except subprocess.CalledProcessError as e:
        print(f"Error running git ls-files: {e}", file=sys.stderr)
        return []
    except FileNotFoundError:
        print("Git command not found. Please ensure git is installed and in your PATH.", file=sys.stderr)
        return []

def is_binary(file_path):
    # Common binary extensions to exclude
    binary_extensions = {
        '.png', '.jpg', '.jpeg', '.gif', '.ico', '.svg', '.webp',
        '.mp4', '.webm', '.ogg', '.mp3', '.wav',
        '.pdf', '.zip', '.gz', '.tar', '.7z',
        '.exe', '.dll', '.so', '.dylib', '.bin', '.obj',
        '.pyc', '.pyo', '.pyd',
        '.woff', '.woff2', '.ttf', '.eot',
        '.db', '.sqlite', '.db3'
    }
    _, ext = os.path.splitext(file_path.lower())
    if ext in binary_extensions:
        return True
    
    # Heuristic check for non-text content in the first 1024 bytes
    if not os.path.exists(file_path):
        return False
    try:
        with open(file_path, 'rb') as f:
            chunk = f.read(1024)
            if b'\0' in chunk:
                return True
    except Exception:
        return True # Treat as binary if unreadable
    
    return False

def main():
    tracked_files = get_tracked_files()
    if not tracked_files:
        sys.exit(0)
    
    for file_path in tracked_files:
        if os.path.isfile(file_path) and not is_binary(file_path):
            print(file_path)

if __name__ == "__main__":
    main()
