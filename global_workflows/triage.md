---
description: "Initial bug investigation and classification workflow. Command: /triage"
---

# Bug Triage & Investigation Workflow (/triage)

<current_workflow>/triage</current_workflow>

Use this workflow to identify the root cause of a bug and determine the next action.

## Step 0: Identity Activation [Role: Incident Analyst]

<current_step>Step 0: Identity Activation</current_step>
<workflow_instructions>
1. Read `${GLOBAL_SKILLS}\role-incident-analyst\SKILL.md` to load investigation protocols.
2. Initialize analysis in the `<thinking>` tag in English.
</workflow_instructions>

- **[MUST [W-TR-0]]**: Activate Incident Analyst identity.

## Step 1: Intake & Reproduction Check [Role: Incident Analyst]

<current_step>Step 1: Intake & Reproduction Check</current_step>
<workflow_instructions>
1. Collect symptoms, logs, and screenshots.
2. Ask for clarification if details are missing.
3. Document reproduction steps clearly.
</workflow_instructions>

- **Intake**: Receive bug details.
- **Reproduction**: [MUST [W-TR-1]] Document exact steps to reproduce.

## Step 2: Deep Dive Analysis (Read-Only) [Role: Incident Analyst]

<current_step>Step 2: Deep Dive Analysis (Read-Only)</current_step>
<workflow_instructions>
1. Run `ollama_adapter.py` on logs.
2. Use `code_analyzer.py` for structural mapping.
3. Use `view_file` for detailed verification.
4. Use the `<thinking>` tag for logic tracing.
</workflow_instructions>

- **Structural Mapping**: Map affected symbols and call graphs.
- **Detailed Verification**: Check line-level details.
- **[PROHIBITED]**: DO NOT suggest fixes or technical solutions.

## Step 3: Root Cause Isolation & Classification [Role: Incident Analyst]

<current_step>Step 3: Root Cause Isolation & Classification</current_step>
<workflow_instructions>
1. Pinpoint the exact failure location.
2. Classify as Type A (Implementation) or Type B (Specification) within the `<incident_report>` tag.
</workflow_instructions>

- **Isolation**: Pinpoint file, line, or configuration.
- **Classification**: Distinguish between developer mistake and flawed logic.

## Step 4: Incident Report & Approval Gate [Role: Incident Analyst]

<current_step>Step 4: Incident Report & Approval Gate</current_step>
<workflow_instructions>
1. Create/update `docs/incident_report.md` in Japanese.
2. Present summary and ask for the next action (YES/NO).
</workflow_instructions>

- **Reporting**: Detail symptoms, steps, root cause, and classification.
- **Gate**: Wait for user response before proceeding.

## Step 5: Backlog Registration & Routing [Role: Incident Analyst]

<current_step>Step 5: Backlog Registration & Routing</current_step>
<workflow_instructions>
1. Register the PBI based on the user's choice.
2. Instruct the user on which workflow to start next.
</workflow_instructions>

- **Registration**: Run `pbi_manager.py` to create the entry.
- **Routing**: Direct to `/dev-design`, `/wish`, or `/sys-design`.
