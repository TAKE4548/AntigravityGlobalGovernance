import os
import sys
import yaml

def get_mapped_docs(docs_dir, modified_path):
    """
    Finds markdown files in docs_dir that are mapped to the modified_path.
    Uses 'related_paths' or 'tags' in frontmatter.
    """
    mapped_docs = []
    for root, _, files in os.walk(docs_dir):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        content = f.read()
                        if content.startswith("---"):
                            parts = content.split("---")
                            if len(parts) >= 3:
                                fm = yaml.safe_load(parts[1])
                                related = fm.get("related_paths", [])
                                tags = fm.get("tags", [])
                                
                                # Match against path
                                match = False
                                for r in related:
                                    if modified_path.startswith(r):
                                        match = True
                                        break
                                
                                # Match against tags (simplified: tag = directory)
                                if not match:
                                    for t in tags:
                                        if t in modified_path:
                                            match = True
                                            break
                                
                                if match:
                                    mapped_docs.append(path)
                except:
                    pass
    return mapped_docs

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: doc_mapper.py <docs_dir> <modified_path>")
        sys.exit(1)
    
    docs = sys.argv[1]
    path = sys.argv[2]
    results = get_mapped_docs(docs, path)
    
    if not results:
        print(f"No mapped documents found for path: {path}")
    else:
        print(f"Impacted documents for {path}:")
        for d in results:
            print(d)
