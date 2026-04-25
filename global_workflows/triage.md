---
name: triage
description: "Initial bug investigation and classification workflow. Command: /triage"
---

# Bug Triage & Investigation Workflow (/triage)

Use this workflow to identify the root cause of a bug and determine the next action. This workflow focuses strictly on investigation and prohibits any code modifications.

## Step 0: Identity Activation [Role: Incident Analyst]
- **[MUST [W-TR-0]]**: Read `${GLOBAL_SKILLS}\role-incident-analyst\SKILL.md` to load investigation protocols.

## Step 1: Intake & Reproduction Check [Role: Incident Analyst]
- Receive bug details (logs/screenshots/symptoms).
- If information is insufficient, ask the user for clarification and STOP.
- **[MUST [W-TR-1]]**: Document the reproduction steps clearly.

## Step 2: Deep Dive Analysis (Read-Only) [Role: Incident Analyst]
- **[MUST [W-TR-2-1]]**: Use available analysis scripts (e.g., `${GLOBAL_SCRIPTS}\ollama_adapter.py`) to analyze logs or trace logic.
- **[MUST [W-TR-2-2]]**: Use `code_analyzer.py` or strategic search (grep, ls) to locate the failure point.
- **[PROHIBITED]**: Do NOT suggest any fixes or technical solutions at this stage. Focus strictly on "What is happening" vs "What should happen".

## Step 3: Root Cause Isolation & Classification [Role: Incident Analyst]
- Pinpoint the exact file, line number, or configuration entry.
- **[CRITICAL]** Classify the issue as:
  - **Type A: Implementation Bug**: The code contradicts the SSoT (docs, specs). It is a developer mistake.
  - **Type B: Specification Bug**: The code follows the SSoT, but the SSoT itself is flawed or missing logic.

## Step 4: Incident Report & Approval Gate [Role: Incident Analyst]
- Create or update `docs/incident_report.md` (in Japanese) including:
  - Symptom / Steps to Reproduce / Root Cause / Classification (Type A or B).
- Present a summary in Japanese and ask for the next action:
  - If Type A: "根本原因は実装ミスでした。バックログに登録して修正（/dev-design）へ進みますか？"
  - If Type B: "仕様自体の改善が必要です。仕様を再定義するため /wish を実行しますか？"
  - If spans multiple repos: "リポジトリ横断的な設計変更が必要です。/sys-design を実行しますか？"
- **MANDATORY TURN-END**: Wait for user's YES/NO.

## Step 5: Backlog Registration & Routing [Role: Incident Analyst]
- **If YES for Type A (Single Repo)**:
  - Create/Update entry in `docs/backlog.md` with `Status: ready`.
  - Inform: "バックログに登録しました。/dev-design を実行してください。"
- **If YES for Type B**:
  - Create/Update entry in `docs/backlog.md` with `Status: new`.
  - Inform: "バックログに登録しました。仕様を再定義するため /wish を実行してください。"
- **If Cross-Repo**:
  - Update `docs/system/E2E_BACKLOG.md` or the master backlog.
  - Inform: "リポジトリ横断課題として登録しました。/sys-design を実行してください。"
- **If NO**: Acknowledge and END.
