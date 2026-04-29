---
description: "Workflow for repository-wide refactor scanning using local models. Command: /refactor-scan"
---

# Refactor Scan Workflow (/refactor-scan)

<current_workflow>/refactor-scan</current_workflow>

Use this workflow to scan the repository for refactoring opportunities, focusing on AI-context efficiency.

## Phase 0: Role Initialization
<current_step>Phase 0: Role Initialization</current_step>
<workflow_instructions>
1. Read `${GLOBAL_SKILLS}\role-refactor-auditor\SKILL.md`.
2. Activate the Refactor Auditor identity.
</workflow_instructions>

## Phase 1: Deterministic Extraction
<current_step>Phase 1: Deterministic Extraction</current_step>
<workflow_instructions>
1. Run `python ${GLOBAL_SCRIPTS}\audit_extractor.py` to get a list of all tracked non-binary files.
2. Filter target files based on priority (e.g., core logic, large files).
</workflow_instructions>

## Phase 2: Sequential Audit
<current_step>Phase 2: Sequential Audit</current_step>
<workflow_instructions>
1. For each file, run `python ${GLOBAL_SCRIPTS}\ollama_adapter.py refactor-audit <file_path>`.
2. Collect JSON outputs from the local model (DeepSeek/Qwen).
</workflow_instructions>

## Phase 3: Consolidation & PBI Creation
<current_step>Phase 3: Consolidation & PBI Creation</current_step>
<workflow_instructions>
1. Consolidate all findings into `docs/refactor_report.md` in Japanese.
2. For each High-priority issue, create a PBI using `python ${GLOBAL_SCRIPTS}\pbi_manager.py create "<Title>"`.
3. Fill the generated PBI file with details from the report, ensuring compliance with the standard PBI format.
4. Run `python ${GLOBAL_SCRIPTS}\backlog_linter.py` to verify the consistency and format of the new PBIs.
</workflow_instructions>
