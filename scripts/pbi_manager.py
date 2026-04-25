import os
import re
import sys
import yaml

from pathlib import Path
import subprocess

# Base directory for backlogs
BACKLOG_DIR = "docs/backlog"
PBI_ACTIVE = os.path.join(BACKLOG_DIR, "pbi/active")
PBI_ARCHIVE = os.path.join(BACKLOG_DIR, "pbi/archive")
TASK_ACTIVE = os.path.join(BACKLOG_DIR, "task/active")
TASK_ARCHIVE = os.path.join(BACKLOG_DIR, "task/archive")
DESIGN_DIR = "docs/design"

def ensure_dirs():
    for d in [PBI_ACTIVE, PBI_ARCHIVE, TASK_ACTIVE, TASK_ARCHIVE, DESIGN_DIR]:
        os.makedirs(d, exist_ok=True)

def shard_backlog(source_file, prefix="REQ"):
    """
    Shards a backlog file into multiple PBI files based on REQ-XXX or PBI-XXX.
    """
    if not os.path.exists(source_file):
        print(f"Source file not found: {source_file}")
        return

    with open(source_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Split by REQ/PBI header
    pattern = rf"(?=### {prefix}-\d+)"
    pbi_blocks = re.split(pattern, content)
    
    header = pbi_blocks[0]
    pbis = pbi_blocks[1:]

    for pbi in pbis:
        # Extract ID
        match = re.search(rf"### ({prefix}-\d+): (.*)", pbi)
        if match:
            pbi_id = match.group(1)
            title = match.group(2).strip()
            
            # Determine status
            status_match = re.search(r"- \*\*Status\*\*: ([\w-]+)", pbi)
            status = status_match.group(1) if status_match else "ready"
            
            target_dir = PBI_ARCHIVE if status == "done" else PBI_ACTIVE
            file_path = os.path.join(target_dir, f"{pbi_id}.md")
            
            frontmatter = {
                "id": pbi_id,
                "title": title,
                "status": status,
                "tags": []
            }
            
            with open(file_path, "w", encoding="utf-8") as out:
                out.write("---\n")
                yaml.dump(frontmatter, out, allow_unicode=True)
                out.write("---\n\n")
                out.write(pbi.strip())
            
            print(f"Sharded {pbi_id} to {file_path}")

def list_pbis(status_filter=None):
    """Lists PBIs in the active directory."""
    pbis = []
    if os.path.exists(PBI_ACTIVE):
        for f in os.listdir(PBI_ACTIVE):
            if f.endswith(".md"):
                path = os.path.join(PBI_ACTIVE, f)
                with open(path, "r", encoding="utf-8") as file:
                    content = file.read()
                    try:
                        parts = content.split("---")
                        if len(parts) >= 3:
                            fm = yaml.safe_load(parts[1])
                            if not status_filter or fm.get("status") == status_filter:
                                pbis.append(f"{fm.get('id')}: {fm.get('title')} [{fm.get('status')}]")
                    except:
                        pass
    
    for p in sorted(pbis):
        print(p)

def archive_pbi(pbi_id):
    """Moves a PBI and its corresponding Task from active to archive."""
    # PBI move
    pbi_src = os.path.join(PBI_ACTIVE, f"{pbi_id}.md")
    pbi_dst = os.path.join(PBI_ARCHIVE, f"{pbi_id}.md")
    if os.path.exists(pbi_src):
        os.rename(pbi_src, pbi_dst)
        print(f"Archived PBI {pbi_id}")
    
    # Task move
    task_src = os.path.join(TASK_ACTIVE, f"{pbi_id}.md")
    task_dst = os.path.join(TASK_ARCHIVE, f"{pbi_id}.md")
    if os.path.exists(task_src):
        os.rename(task_src, task_dst)
        print(f"Archived Task {pbi_id}")

def migrate_ai_backlog(source_file=".ai-backlog.md"):
    """Moves .ai-backlog.md to task/active/REQ-XXX.md."""
    if not os.path.exists(source_file):
        return
    
    with open(source_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract REQ ID from header
    match = re.search(r"# (REQ-\d+):", content)
    if match:
        pbi_id = match.group(1)
        target_path = os.path.join(TASK_ACTIVE, f"{pbi_id}.md")
        os.rename(source_file, target_path)
        print(f"Migrated tasks for {pbi_id} to {target_path}")

def create_pbi(title, status="new"):
    """Creates a new PBI file with the next available ID."""
    ensure_dirs()
    ids = []
    for d in [PBI_ACTIVE, PBI_ARCHIVE]:
        if os.path.exists(d):
            for f in os.listdir(d):
                match = re.match(r"REQ-(\d+)\.md", f)
                if match:
                    ids.append(int(match.group(1)))
    
    next_id = max(ids) + 1 if ids else 1
    pbi_id = f"REQ-{next_id:03d}"
    file_path = os.path.join(PBI_ACTIVE, f"{pbi_id}.md")
    
    frontmatter = {
        "id": pbi_id,
        "title": title,
        "status": status,
        "tags": []
    }
    
    content = f"""---
id: {pbi_id}
title: "{title}"
status: {status}
tags: []
---

### {pbi_id}: {title}

- **Status**: {status}
- **Description**: (要件をここに記述)

#### Acceptance Criteria (AC)
- [ ] AC-1: 
"""
    
    with open(file_path, "w", encoding="utf-8") as out:
        out.write(content)
    
    print(f"Created new PBI: {file_path}")

def init_task(pbi_id, symbol=None):
    """Initializes a sharded task file with optional auto-extracted snippets."""
    ensure_dirs()
    task_file = os.path.join(TASK_ACTIVE, f"{pbi_id}.md")
    
    # Extract code if symbol provided
    types_snippet = "// 関連する Interface/Type 定義をここに物理的に抽出して貼り付ける"
    code_snippet = "// 修正対象となる既存の関数/ロジックの本体をここに貼り付ける"
    target_file = "[フルパス]"
    target_symbol = symbol if symbol else "[関数名・クラス名]"
    target_range = "[Lxxx付近]"

    if symbol:
        # Resolve script path via environment variable or default context lookup
        global_scripts = os.environ.get("GLOBAL_SCRIPTS")
        if not global_scripts:
            # Fallback: Try to read from .agents/context.md if we are in a repo
            try:
                context_path = os.path.join(os.getcwd(), ".agents", "context.md")
                if os.path.exists(context_path):
                    with open(context_path, "r", encoding="utf-8") as cf:
                        match = re.search(r"- \*\*GLOBAL_SCRIPTS\*\*: `(.*)`", cf.read())
                        if match:
                            global_scripts = match.group(1)
            except:
                pass
        
        script_path = os.path.join(global_scripts, "code_analyzer.py") if global_scripts else "code_analyzer.py"
        
        try:
            res = subprocess.check_output(["python", script_path, "extract", ".", symbol], text=True, encoding="utf-8")
            if "CONTENT_START" in res:
                content_match = re.search(r"CONTENT_START\n(.*?)\nCONTENT_END", res, re.S)
                file_match = re.search(r"FILE: (.*)", res)
                range_match = re.search(r"RANGE: (.*)", res)
                if content_match:
                    code_snippet = content_match.group(1).strip()
                if file_match:
                    abs_file = file_match.group(1).strip()
                    # Convert to relative path to avoid absolute path leakage
                    try:
                        target_file = os.path.relpath(abs_file, os.getcwd())
                    except:
                        target_file = abs_file
                if range_match:
                    target_range = f"L{range_match.group(1).strip()}付近"
        except Exception as e:
            print(f"Extraction failed for {symbol}: {e}")

    content = f"""# TASK-{pbi_id}-01: [概要]

## 1. ターゲット識別
- **対象ファイル**: {target_file}
- **対象シンボル**: {target_symbol}
- **行番号目安**: {target_range}

## 2. 密閉コンテキスト (Hermetic Context)
※エンジニアは、以下のスニペットのみを情報源として実装すること。

### 2.1 必須の型定義
```python
{types_snippet}
```

### 2.2 既存の対象コード
```python
{code_snippet}
```

## 3. 実装要件 (Implementation Logic)
- [ ] [具体的なロジック変更手順を箇条書きで記載]

## 4. 検証手順 (AC)
- [ ] [このタスク単体で実行すべきテストコマンドと期待値]
"""
    with open(task_file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Initialized Task Card: {task_file}")

def init_test_plan(pbi_id):
    """Initializes an executable test plan."""
    ensure_dirs()
    test_plan_file = os.path.join(DESIGN_DIR, f"PBI-{pbi_id}-test-plan.md")
    
    content = f"""# PBI-{pbi_id} 実行可能テスト計画

## 1. 自動テスト (CLI Verification)
- **コマンド**: `pytest tests/test_xxx.py` (適宜修正)
- **期待値**: 全テストケースの PASS。脳内推論での代用は厳禁。

## 2. ツール主導監査 (Tool-Driven Audit)
- **API検証**: `openapi_parser.py` を使用し、エンドポイントの差分を確認すること。
- **コード監査**: `ollama_adapter.py arch-audit .` を実行し、設計整合性の客観的証明を得ること。

## 3. ブラウザ検証 (Browser Agent Verification)
- **対象URL**: `http://localhost:8000/docs`
- **操作手順**: [1. 〇〇をクリック, 2. △△を入力]
- **判定基準 (Assertion)**: [ステータスコード 200, レスポンスボディに期待する値が含まれること]
- **必須エビデンス**: スクリーンショットの保存パスを指定すること。
"""
    with open(test_plan_file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Initialized Test Plan: {test_plan_file}")

if __name__ == "__main__":
    ensure_dirs()
    if len(sys.argv) < 2:
        print("Usage: pbi_manager.py <command> [args]")
        sys.exit(1)
    
    cmd = sys.argv[1]
    if cmd == "shard":
        shard_backlog(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "REQ")
    elif cmd == "migrate-tasks":
        migrate_ai_backlog(sys.argv[2] if len(sys.argv) > 2 else ".ai-backlog.md")
    elif cmd == "list":
        list_pbis()
    elif cmd == "archive":
        archive_pbi(sys.argv[2])
    elif cmd == "list-ready":
        list_pbis("ready")
    elif cmd == "list-in-progress":
        list_pbis("in-progress")
    elif cmd == "init-task":
        symbol = None
        if "--symbol" in sys.argv:
            idx = sys.argv.index("--symbol")
            if len(sys.argv) > idx + 1:
                symbol = sys.argv[idx+1]
        init_task(sys.argv[2], symbol)
    elif cmd == "init-test-plan":
        init_test_plan(sys.argv[2])

