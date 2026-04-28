---
description: >
  Integrated system verification and cross-repo E2E testing workflow.
  Command: /sys-verify
---

# System Verification Workflow (/sys-verify)

<current_workflow>/sys-verify</current_workflow>

Final verification to ensure the entire system meets the AC of the master REQ.

## Step 0: Identity Activation [Role: System Architect]

<current_step>Step 0: Identity Activation</current_step>
<workflow_instructions>
1. Read `${GLOBAL_SKILLS}\role-system-architect\SKILL.md`.
2. Prepare for integrated verification.
</workflow_instructions>

- **[MUST [W-SV-0]]**: Activate System Architect identity.

## Step 1: Autonomous Readiness Check [Role: System Architect]

<current_step>Step 1: Autonomous Readiness Check</current_step>
<workflow_instructions>
1. Run `pbi_manager.py check-status` across FE/BE repositories.
2. Halt if implementation is not `done`.
</workflow_instructions>

- **Readiness Check**: Verify that all child PBIs are complete.

## Step 2: Static Integration Audit [Role: System Architect]

<current_step>Step 2: Static Integration Audit</current_step>
<workflow_instructions>
1. Use `scout_adapter.py` to verify that FE/BE implementation matches the SSoT.
2. Analyze controller interfaces and API alignment in the `<thinking>` tag.
</workflow_instructions>

- **Integration Audit**: Verify alignment of fetch processes and controllers with `openapi.yaml`.

## Step 3: Dynamic E2E Verification [Role: System Architect]

<current_step>Step 3: Dynamic E2E Verification</current_step>
<workflow_instructions>
1. Execute integrated test scripts (e.g., Playwright).
2. Collect recordings or logs and isolate them in the `<execution_evidence>` tag.
</workflow_instructions>

- **E2E Execution**: Run dynamic verification of the entire system.

## Step 4: Strict AC Compliance & Closure [Role: System Architect]

<current_step>Step 4: Strict AC Compliance & Closure</current_step>
<workflow_instructions>
1. Generate the mandatory AC compliance table in `walkthrough.md`.
2. Update master PBI status to `done` and announce completion in Japanese.
</workflow_instructions>

- **Compliance Table**: Verify all master ACs.
- **Closure**: Archive the master REQ and report success.
