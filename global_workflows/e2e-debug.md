---
description: >
  Cross-repository debugging workflow.
  Systematically isolates and resolves bugs where the Frontend/Backend boundary is unclear.
  Command: /e2e-debug
---

# E2E Verification & Debugging Workflow (/e2e-debug)

<current_workflow>/e2e-debug</current_workflow>

Systematically resolving cross-repository bugs through isolation.

## Step 0: Prerequisites [Role: Tester/Reviewer]

<current_step>Step 0: Prerequisites</current_step>
<workflow_instructions>
1. Check `E2E_BACKLOG.md` for Gate completion (Stub/Driver).
2. Halt if unit development is incomplete.
</workflow_instructions>

- **Readiness**: Ensure both sides of the contract are ready for integration.

## Step 1: Isolation & Evidence [Role: Tester/Reviewer]

<current_step>Step 1: Isolation & Evidence</current_step>
<workflow_instructions>
1. Start client and server environments.
2. Reproduce issue and capture API Request/Response (JSON).
3. Record logs in the `<execution_evidence>` tag.
</workflow_instructions>

- **Evidence Collection**: Gather objective proof from browser and server.

## Step 2: Classification [Role: Architect]

<current_step>Step 2: Classification</current_step>
<workflow_instructions>
1. Use the `<thinking>` tag to analyze evidence.
2. Classify as Unit Bug or Contract Bug.
</workflow_instructions>

- **Classification**: Determine if the error is implementation-specific or contract-level.

## Step 3: Specification Reconstruction [Role: System Architect]

<current_step>Step 3: Specification Reconstruction</current_step>
<workflow_instructions>
1. In the Backend repo, update `docs/system/` documents.
2. Create cross-repo tasks and obtain user approval.
3. Record decisions in the `<design_decisions>` tag.
</workflow_instructions>

- **Contract Fix**: Re-align FE/BE expectations via SSoT updates.

## Step 4: Task Distribution & Unit Re-fix [Role: Engineer]

<current_step>Step 4: Task Distribution & Unit Re-fix</current_step>
<workflow_instructions>
1. Process tasks in respective repositories.
2. Update Gates in `E2E_BACKLOG.md`.
</workflow_instructions>

- **Execution**: Apply fixes based on the reconstructed specification.

## Step 5: Verification (Re-integration) [Role: Tester]

<current_step>Step 5: Verification (Re-integration)</current_step>
<workflow_instructions>
1. Resume integration testing and update status to `[VERIFIED]`.
</workflow_instructions>

- **Verification**: Confirm the fix in a live integrated environment.

## Step 6: Final Reporting [Role: Agent Architect]

<current_step>Step 6: Final Reporting</current_step>
<workflow_instructions>
1. Run `artifact_linter.py`.
2. Present the walkthrough in Japanese.
</workflow_instructions>

- **Report**: Complete the E2E debug session.
