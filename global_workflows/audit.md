---
name: audit
description: "Global workflow for pre-publish security audit. Command: /audit"
---

Security Audit Workflow (/audit)

Phase 0: Role Initialization [MANDATORY]
- Action: You MUST explicitly load and adopt the `role-security-auditor` skill before proceeding with any audit tasks.
- Constraint: Ensure you are operating strictly under the local DeepSeek model constraints defined in the role. Do not use default cloud models for Phase 2.

Use this workflow to perform a systematic, deterministic security audit of the repository using a local DeepSeek model before publishing to external platforms (e.g., GitHub).

Phase 1: Deterministic Extraction [Role: Security Auditor]
- Objective: Obtain a strict list of tracked files, ignoring binaries and `.gitignore` matches.
- Execution: Run `python scripts/audit_extractor.py` (which MUST use `git ls-files` internally).
- Constraint: Save the output list to a temporary file or memory. Do NOT attempt to list files based on your own reasoning.

Phase 2: Local LLM Inspection [Role: Security Auditor]
- Objective: Scan each extracted file for hardcoded secrets, PII, and absolute paths.
- Execution: For each file identified in Phase 1, run `python scripts/ollama_adapter.py sec-audit <filepath>`.
- System Prompt injection for DeepSeek (Handled by adapter):
  "You are a DevSecOps engineer. Scan the input for: 1. Credentials (AKIA..., ghp_..., passwords, private keys). 2. DB connection strings. 3. PII (emails, phone numbers). 4. Local paths (C:\Users\[USER]\...). Output strictly in JSON format: [{'line': int, 'type': string, 'severity': 'High|Medium|Low', 'description': string}]. Return [] if clean."
- Chunking: The adapter script MUST handle chunking if the file size threatens the 8192 `num_ctx` limit of the local DeepSeek model.

Phase 3: Consolidation & Reporting [Role: Security Auditor]
- Objective: Aggregate findings into a final report.
- Deliverable: Create or update `docs/audit_report.md` in Japanese.
- The report MUST include:
  1. 監査サマリー (Audit Summary)
  2. 発見されたリスク (Detected Risks categorized by High/Medium/Low)
  3. 該当箇所とファイルパス (Specific file paths and line numbers)
  4. 推奨される修正アクション (Recommended remediations)
- Mandatory Turn-End: Stop execution and wait for the user to review the report.