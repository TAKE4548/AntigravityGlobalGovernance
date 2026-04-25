import json
import urllib.request
import os
import sys

# Force UTF-8 output on Windows terminals
if sys.stdout.encoding != "utf-8":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

"""
Ollama Adapter for AntiGravity Agents (Native API v2)
Optimized for Qwen3:14b (32k context support)
"""

OLLAMA_API_URL = "http://127.0.0.1:11434/api/chat"
MODEL_ID = "qwen3:14b"
AUDIT_MODEL_ID = "qwen3:14b"

def strip_thinking(text: str) -> str:
    """Strip <think>...</think> block from model output and return only the answer."""
    import re
    cleaned = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    return cleaned.strip()

def query_ollama(prompt, system_prompt="You are a helpful assistant.", max_tokens=2048, model=None):
    target_model = model if model else MODEL_ID
    data = {
        "model": target_model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "stream": False,
        "options": {
            "num_predict": max_tokens,
            "temperature": 0.1,
            "top_p": 0.9,
            "num_ctx": 32768  # Support for Qwen3:14b 32k context
        }
    }
    
    headers = {"Content-Type": "application/json"}
    req = urllib.request.Request(OLLAMA_API_URL, data=json.dumps(data).encode("utf-8"), headers=headers)
    
    try:
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            message = res_data.get("message", {})
            content = message.get("content", "")
            thinking = message.get("thinking", "")
            
            # Universal handling: Use content if available, fallback to thinking field
            final_text = content if content.strip() else thinking
            return strip_thinking(final_text)
    except Exception as e:
        return f"Error querying Ollama Native API: {str(e)}"

def summarize_file(file_path):
    if not os.path.exists(file_path):
        return f"File not found: {file_path}"
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        return f"Reading error: {str(e)}"
    
    # Qwen3:14b 32k allows for larger file chunks (approx 100k chars)
    MAX_CHARS = 100000 
    if len(content) > MAX_CHARS:
        content = content[:MAX_CHARS] + "\n... (omitted due to length)"
    
    prompt = (
        "Analyze the following source code for a developer. "
        "Summarize its purpose, core logic, and key data structures. "
        "Point out any technical debt or potential improvements. "
        "Respond in Japanese with professional tone.\n\n"
        f"{content}"
    )
    system_message = (
        "You are an expert Python engineer specialized in Monster Hunter equipment management systems. "
        "Provide a high-quality, technical summary."
    )
    
    return query_ollama(prompt, system_message)

def audit_requirements(content):
    prompt = (
        "Analyze the following requirement against the project's historical context. "
        "Search for logical contradictions, missing edge cases, or overlaps with existing features. "
        f"Requirement Text:\n{content}"
    )
    system = "You are an expert Business Analyst for a Monster Hunter equipment manager app. Focus on logical consistency."
    return query_ollama(prompt, system)

def audit_design(content):
    prompt = (
        "Check this UI component or CSS against the project's v15 HUD design tokens. "
        "Point out any deviations from standard colors, typography, or spacing patterns. "
        f"Input:\n{content}"
    )
    system = "You are an expert UX Designer specializing in high-end game HUDs. Focus on design system compliance."
    return query_ollama(prompt, system)

def audit_structure(content):
    prompt = (
        "Audit the following code for architectural violations. "
        "Look for hardcoded state, leaking abstractions, or violations of the State/Atom/Dialog separation. "
        f"Source Code:\n{content}"
    )
    system = "You are a Master Architect. Focus on structural integrity and technical debt."
    return query_ollama(prompt, system)

def sync_docs(docs_dir="docs"):
    """Scan and concatenate all .md files in the docs directory for a global spec audit."""
    if not os.path.exists(docs_dir):
        return f"Docs directory not found: {docs_dir}"
    
    combined_content = []
    # Recursive scan for .md files
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        file_body = f.read()
                        combined_content.append(f"### FILE: {path}\n{file_body}\n")
                except Exception as e:
                    combined_content.append(f"### ERROR READING: {path} ({str(e)})\n")
    
    total_specs = "\n".join(combined_content)
    # Check if total length is reasonable for 32k context (~100k-120k chars)
    if len(total_specs) > 120000:
        total_specs = total_specs[:120000] + "\n... (omitted to fit context limit)"
    
    prompt = (
        "Analyze the following full project documentation. "
        "Memorize the key rules, design systems, and backlog status. "
        "Summarize the project's current 'Core Values' and 'Unfinished Tasks' to prove your understanding. "
        "Respond in Japanese.\n\n"
        f"{total_specs}"
    )
    system = "You are an expert system auditor. You have just ingested the full project documentation."
    return query_ollama(prompt, system)

def synthesize_context(raw_outputs):
    """
    Synthesizes multiple raw script outputs into a clean implementation context.
    """
    prompt = (
        "Synthesize the following raw analysis results into a structured 'Implementation Context' for a developer. "
        "Remove redundancy, highlight critical dependencies, and provide a clear 'Ready to Implement' snippet. "
        "Respond in Japanese.\n\n"
        f"{raw_outputs}"
    )
    system = "You are a Master Architect. Your goal is to provide the Engineer with exactly what they need to start coding without further exploration."
    return query_ollama(prompt, system)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ollama_adapter.py <action> [args]")
        print("Actions: summarize <path>, query <prompt>, ba-audit <text>, ux-audit <text>, arch-audit <text>, sync-docs [dir], synthesize <raw_text>")
        sys.exit(1)
    
    action = sys.argv[1]
    arg = sys.argv[2] if len(sys.argv) > 2 else ""
    
    if action == "summarize":
        print(summarize_file(arg))
    elif action == "query":
        print(query_ollama(arg))
    elif action == "ba-audit":
        print(audit_requirements(arg))
    elif action == "ux-audit":
        print(audit_design(arg))
    elif action == "arch-audit":
        print(audit_structure(arg))
    elif action == "sync-docs":
        print(sync_docs(arg if arg else "docs"))
    elif action == "engineer-audit":
        if not arg:
            print("Usage: ollama_adapter.py engineer-audit <task_file_path>")
            sys.exit(1)
        with open(arg, "r", encoding="utf-8") as f:
            content = f.read()
        prompt = f"あなたはシニアエンジニアです。以下のタスクカードの情報（特にスニペット）だけで、他を検索せずに実装が可能か、型定義が不足していないかを極めて厳しくチェックしてください。不足があれば具体的な『シンボル名』を指摘してください。\n\n{content}"
        print(query_ollama(prompt))
    elif action == "qa-audit":
        if not arg:
            print("Usage: ollama_adapter.py qa-audit <test_plan_path>")
            sys.exit(1)
        with open(arg, "r", encoding="utf-8") as f:
            content = f.read()
        prompt = f"あなたはQAエンジニアです。以下のテスト計画が機械的に実行可能か（コマンドが具体的か、判定基準が曖昧でないか）を監査してください。特にAIエージェントが『脳内テスト』で逃げられる余地がないかを厳しくチェックしてください。\n\n{content}"
        print(query_ollama(prompt))
    elif action == "sec-audit":
        if not arg or not os.path.exists(arg):
            print(f"File not found or not provided: {arg}")
            sys.exit(1)
        
        try:
            with open(arg, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except Exception as e:
            print(f"Error reading file {arg}: {e}")
            sys.exit(1)

        system_prompt = (
            "You are a DevSecOps engineer. Scan the input for: "
            "1. Credentials (AKIA..., ghp_..., passwords, private keys). "
            "2. DB connection strings. "
            "3. PII (emails, phone numbers). "
            "4. Local paths (C:\\Users\\...). "
            "Output strictly in JSON format: [{'line': int, 'type': string, 'severity': 'High|Medium|Low', 'description': string}]. "
            "Return [] if clean."
        )

        # Simple chunking logic to stay within context limits if needed.
        # Qwen3:14b 32k context can handle a lot, but we chunk at ~20k chars for safety and precision.
        CHUNK_SIZE_LINES = 500
        all_findings = []
        
        for i in range(0, len(lines), CHUNK_SIZE_LINES):
            chunk = lines[i:i+CHUNK_SIZE_LINES]
            # Add line numbers for the model to reference
            chunk_content = "".join([f"{i + idx + 1}: {line}" for idx, line in enumerate(chunk)])
            
            prompt = f"Scan the following file content for security risks:\n\n{chunk_content}"
            response = query_ollama(prompt, system_prompt, model=AUDIT_MODEL_ID)
            
            try:
                # Attempt to parse JSON from the response. Sometimes models wrap it in markdown.
                import re
                json_match = re.search(r'\[.*\]', response, re.DOTALL)
                if json_match:
                    findings = json.loads(json_match.group(0))
                    all_findings.extend(findings)
                else:
                    if response.strip() != "[]":
                        # If not [], and no match, it might be a weird format but we ignore if it doesn't look like JSON
                        pass
            except Exception:
                pass # Skip if unparseable

        print(json.dumps(all_findings, indent=2, ensure_ascii=False))
