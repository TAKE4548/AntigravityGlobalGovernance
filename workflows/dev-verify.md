---
description: "Integration testing and PBI closure phase. Command: /dev-verify"
---

# Development Workflow: Verification Phase (/dev-verify)

Use this workflow to perform integration testing and formally close a PBI with a local QA audit.

## Phase 0: Identity Activation [Role: QA]
- **[MUST [W-DV-0]]**: Read `C:\Users\audih\.gemini\antigravity\skills\role-tester-reviewer\SKILL.md` to load role-specific instructions and constraints.

## Phase 1: Audit & Readiness [Role: QA]
- **Identity**: This role is performed by the `role-tester-reviewer` (Local-Primary).
- **PBI Selection**: Run `python C:\Users\audih\.gemini\antigravity\scripts\pbi_manager.py list-in-progress`.
    - **[MANDATORY TURN-END]**: Ask the user which PBI ID to verify.
- **Readiness Check**: Run `python C:\Users\audih\.gemini\antigravity\scripts\workflow_validator.py verify-ready <PBI_ID>`.
- **Task Verification**: Ensure all tasks in `docs/backlog/task/active/<PBI_ID>.md` are marked complete.

## Phase 2: Integration & Local Audit [Role: QA]
- **Scenario Execution**: Run CLI commands defined in `docs/design/PBI-<PBI_ID>-test-plan.md`.
    - **[MUST [R-TE-Tool-1]] API Verification**: Use `openapi_parser.py` for API checks. DO NOT read `openapi.yaml` directly.
- **Evidence Collection**: Save Stdout or screenshots as specified in the test plan.
- **Local Auditor Check**: Run `python C:\Users\audih\.gemini\antigravity\scripts\ollama_adapter.py qa-audit docs/design/PBI-<PBI_ID>-test-plan.md`.
    - **[Hallucination Prevention]**: DO NOT issue PASS without the audit output.
- **Defect Handling**: If defects are found, add new tasks to `docs/backlog/task/active/<PBI_ID>.md` and return to `/dev-task`.

## Phase 3: Walkthrough & SSoT Sync [Role: Architect]
- **[MUST [W-DV-3]]**: Read `C:\Users\audih\.gemini\antigravity\skills\role-architect\SKILL.md` to ensure design integrity during synchronization.
- **SSoT Update**: According to the **"Impacted Documents List"** in `implementation_plan.md`, update all identified existing documents to reflect the changes.
- **AC Compliance Table**: Create the mandatory Markdown table in `walkthrough.md` (**Japanese**) verifying all AC.
- **Closure**: Once all documents are synced and AC are verified, run `python C:\Users\audih\.gemini\antigravity\scripts\pbi_manager.py archive <PBI_ID>`.
