---
name: dev
description: "Formal development session workflow. Tracks progress via session.md. (v1.7)"
---

# Development Workflow (/dev) [DEPRECATED]

<current_workflow>/dev</current_workflow>

> [!CAUTION]
> This workflow is deprecated. Use `/dev-design`, `/dev-task`, and `/dev-verify`.

## Step 0: Session Initialization [Role: Dev Coordinator]

<current_step>Step 0: Session Initialization</current_step>
<workflow_instructions>
1. Check environment and run linters.
2. Initialize `session.md` and record the target REQ.
</workflow_instructions>

- **Resumption Logic**: Confirm with user whether to resume or start new.

## Step 1: Item Selection & Setup [Role: Dev Coordinator]

<current_step>Step 1: Item Selection & Setup</current_step>
<workflow_instructions>
1. Run `git checkout -b <branch>`.
2. Present `ready` items to the user.
</workflow_instructions>

## Step 3: High-Level Design & SSoT Update [Role: Architect]

<current_step>Step 3: High-Level Design & SSoT Update</current_step>
<workflow_instructions>
1. Identify and update SSoT documents.
2. Analyze impact and create designs in the `<thinking>` tag.
</workflow_instructions>

## Step 5: Approval Gate [Role: Dev Coordinator]

<current_step>Step 5: Approval Gate</current_step>
<workflow_instructions>
1. Present `implementation_plan.md` in Japanese.
2. [MANDATORY TURN-END] Wait for explicit user approval.
</workflow_instructions>

## Step 6: Implementation [Role: Engineer]

<current_step>Step 6: Implementation</current_step>
<workflow_instructions>
1. Implement, test, and collect evidence.
2. Record evidence in the `<execution_evidence>` tag.
</workflow_instructions>

## Step 7: Verification & Review [Role: Tester/Reviewer]

<current_step>Step 7: Verification & Review</current_step>
<workflow_instructions>
1. Audit SSoT compliance.
2. Issue PASS/FAIL/CONCERNS verdict.
</workflow_instructions>

## Step 8: Finalization [Role: Dev Coordinator]

<current_step>Step 8: Finalization</current_step>
<workflow_instructions>
1. Sync backlog and close session.
</workflow_instructions>
