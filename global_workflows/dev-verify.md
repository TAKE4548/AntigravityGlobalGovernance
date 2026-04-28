---
description: "Integration testing and PBI closure phase. Command: /dev-verify"
---

# Development Workflow: Verification Phase (/dev-verify)

<current_workflow>/dev-verify</current_workflow>

Use this workflow to perform integration testing and formally close a PBI with a local QA audit.

## Phase 0: Identity Activation [Role: QA]

<current_step>Phase 0: Identity Activation</current_step>
<workflow_instructions>
1. Read `${GLOBAL_SKILLS}\role-tester-reviewer\SKILL.md` to load QA instructions.
2. Prepare for evidence-based verification.
</workflow_instructions>

- **[MUST [W-DV-0]]**: Activate QA identity and load constraints.

## Phase 1: Audit & Readiness [Role: QA]

<current_step>Phase 1: Audit & Readiness</current_step>
<workflow_instructions>
1. Run `pbi_manager.py list-in-progress` and ask user for selection.
2. Run `workflow_validator.py verify-ready` to ensure all tasks are complete.
</workflow_instructions>

- **PBI Selection**: Present in-progress PBIs to the user.
- **Readiness Check**: Validate that all tasks are marked as complete.

## Phase 2: Integration & Local Audit [Role: QA]

<current_step>Phase 2: Integration & Local Audit</current_step>
<workflow_instructions>
1. Run CLI commands from the test plan.
2. Collect evidence and isolate it in the `<execution_evidence>` tag.
3. Use `openapi_parser.py` for API checks.
4. Run `ollama_adapter.py qa-audit` for an objective compliance check.
</workflow_instructions>

- **Scenario Execution**: Execute test plan commands.
- **Evidence Collection**: Save logs and screenshots.
- **Local Audit**: Obtain objective proof of compliance via local LLM.

## Phase 3: Walkthrough & SSoT Sync [Role: Architect]

<current_step>Phase 3: Walkthrough & SSoT Sync</current_step>
<workflow_instructions>
1. Update impacted documents to reflect implementation results.
2. Produce `walkthrough.md` in Japanese with the mandatory AC compliance table.
3. Run `pbi_manager.py archive` to close the PBI.
</workflow_instructions>

- **SSoT Update**: Synchronize all specifications with the final implementation.
- **AC Compliance Table**: Generate the mandatory table in `<expected_deliverables>`.
- **Closure**: Archive the PBI and present the final walkthrough.
