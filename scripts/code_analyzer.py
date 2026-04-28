import ast
import os
import sys

def find_symbol_definition(root_dir, symbol_name):
    """
    Finds the definition of a symbol (function or class) in the given directory.
    Returns (file_path, start_line, end_line, content) or None.
    """
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        lines = f.readlines()
                        tree = ast.parse("".join(lines))
                        
                        for node in ast.walk(tree):
                            if (isinstance(node, ast.FunctionDef) or isinstance(node, ast.ClassDef)) and node.name == symbol_name:
                                start = node.lineno
                                end = node.end_lineno
                                content = "".join(lines[start-1:end])
                                return (path, start, end, content)
                except:
                    pass
    return None

def find_callers(root_dir, target_symbol):
    """
    Scans Python files in root_dir and finds calls to target_symbol.
    Returns a list of (file_path, line_number, context_line).
    """
    callers = []
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        lines = f.readlines()
                        tree = ast.parse("".join(lines))
                        
                        for node in ast.walk(tree):
                            if isinstance(node, ast.Call):
                                # Check if it's a direct name call or an attribute call
                                called_name = ""
                                if isinstance(node.func, ast.Name):
                                    called_name = node.func.id
                                elif isinstance(node.func, ast.Attribute):
                                    called_name = node.func.attr
                                
                                if called_name == target_symbol:
                                    lineno = node.lineno
                                    context = lines[lineno-1].strip()
                                    callers.append((path, lineno, context))
                except Exception as e:
                    # print(f"Error parsing {path}: {e}")
                    pass
    return callers

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] in ["--help", "-h"]:
        print("AntiGravity Code Analyzer")
        print("Usage: python code_analyzer.py <command> <root_dir> <symbol>")
        print("\nCommands:")
        print("  callers <root> <symbol>     Find all calls to the specified symbol in Python files.")
        print("  extract <root> <symbol>     Extract the full definition of the specified function or class.")
        sys.exit(0)
    
    if len(sys.argv) < 4:
        print("Error: Missing arguments.")
        print("Usage: python code_analyzer.py <command> <root_dir> <symbol>")
        sys.exit(1)
    
    cmd = sys.argv[1]
    root = sys.argv[2]
    symbol = sys.argv[3]
    
    if cmd == "callers":
        results = find_callers(root, symbol)
        if not results:
            print(f"No callers found for '{symbol}' in {root}")
        else:
            print(f"Found {len(results)} callers for '{symbol}':")
            for path, line, ctx in results:
                print(f"{path}:{line} -> {ctx}")
    elif cmd == "extract":
        result = find_symbol_definition(root, symbol)
        if result:
            path, start, end, content = result
            print("<extraction_result>")
            print(f"  <file_path>{path}</file_path>")
            print(f"  <line_range>{start}-{end}</line_range>")
            print("  <source_code>")
            print(content.strip())
            print("  </source_code>")
            print("</extraction_result>")
        else:
            print(f"Symbol '{symbol}' not found in {root}")
