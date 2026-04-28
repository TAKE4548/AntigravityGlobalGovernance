---
description: "Global workflow for pre-publish security audit. Command: /audit"
---

# Security Audit Workflow (/audit)

<current_workflow>/audit</current_workflow>

Systematic security audit using a local model.

## Phase 0: Identity Activation [Role: Security Auditor]

<current_step>Phase 0: Identity Activation</current_step>
<workflow_instructions>
1. Load `role-security-auditor` skill.
2. Prepare for deterministic file extraction and scanning.
</workflow_instructions>

- **Identity**: Activate Security Auditor identity and load constraints.

## Phase 1: Deterministic Extraction [Role: Security Auditor]

<current_step>Phase 1: Deterministic Extraction</current_step>
<workflow_instructions>
1. Run `audit_extractor.py` to get a strict list of tracked files.
2. Isolate the file list in the `<execution_evidence>` tag.
</workflow_instructions>

- **Extraction**: Identify target files using Git metadata.

## Phase 2: Local LLM Inspection [Role: Security Auditor]

<current_step>Phase 2: Local LLM Inspection</current_step>
<workflow_instructions>
1. Scan each file using `ollama_adapter.py sec-audit`.
2. Handle chunking for large files.
3. Record findings in the `<thinking>` tag in English.
</workflow_instructions>

- **Inspection**: Detect secrets, PII, and absolute paths using DeepSeek.

## Phase 3: Consolidation & Reporting [Role: Security Auditor]

<current_step>Phase 3: Consolidation & Reporting</current_step>
<workflow_instructions>
1. Aggregate findings into `docs/audit_report.md` in Japanese.
2. Wait for user review.
</workflow_instructions>

- **Reporting**: Detail risks, locations, and remediations.
