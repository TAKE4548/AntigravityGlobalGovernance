import yaml
import sys
import os
import json

def resolve_refs(spec, obj):
    """
    Recursively resolves $ref entries within the spec.
    """
    if isinstance(obj, dict):
        if "$ref" in obj:
            ref_path = obj["$ref"]
            if ref_path.startswith("#/"):
                # Local reference
                parts = ref_path.split("/")[1:]
                ref_obj = spec
                for p in parts:
                    ref_obj = ref_obj.get(p, {})
                # Recursively resolve the referred object
                return resolve_refs(spec, ref_obj)
            else:
                # External reference not supported for now, return as is
                return obj
        return {k: resolve_refs(spec, v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [resolve_refs(spec, i) for i in obj]
    else:
        return obj

def load_spec(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        sys.exit(1)
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def list_endpoints(spec):
    paths = spec.get("paths", {})
    print(f"{'METHOD':<8} | {'PATH':<40} | {'SUMMARY'}")
    print("-" * 80)
    for path, methods in paths.items():
        for method, details in methods.items():
            if method.lower() in ["get", "post", "put", "delete", "patch"]:
                summary = details.get("summary", "No summary")
                print(f"{method.upper():<8} | {path:<40} | {summary}")

def get_endpoint(spec, target_path, target_method):
    paths = spec.get("paths", {})
    path_item = paths.get(target_path)
    if not path_item:
        print(f"Path not found: {target_path}")
        return
    
    endpoint = path_item.get(target_method.lower())
    if not endpoint:
        print(f"Method {target_method} not found for path {target_path}")
        return
    
    resolved = resolve_refs(spec, endpoint)
    print(yaml.dump(resolved, allow_unicode=True, sort_keys=False))

def get_schema(spec, schema_name):
    components = spec.get("components", {})
    schemas = components.get("schemas", {})
    schema = schemas.get(schema_name)
    if not schema:
        print(f"Schema not found: {schema_name}")
        return
    
    resolved = resolve_refs(spec, schema)
    print(yaml.dump({schema_name: resolved}, allow_unicode=True, sort_keys=False))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: openapi_parser.py <file_path> <command> [args]")
        print("Commands: list-endpoints, get-endpoint <path> <method>, get-schema <name>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    cmd = sys.argv[2]
    spec = load_spec(file_path)
    
    if cmd == "list-endpoints":
        list_endpoints(spec)
    elif cmd == "get-endpoint":
        if len(sys.argv) < 5:
            print("Missing path or method")
        else:
            get_endpoint(spec, sys.argv[3], sys.argv[4])
    elif cmd == "get-schema":
        if len(sys.argv) < 4:
            print("Missing schema name")
        else:
            get_schema(spec, sys.argv[3])
