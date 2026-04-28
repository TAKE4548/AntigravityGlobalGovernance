---
description: "Workflow for addressing agent performance issues, rule violations, or creating new roles. Command: /agent-fix"
---

# Agent Improvement Workflow (/agent-fix)

<current_workflow>/agent-fix</current_workflow>

Use this workflow for agent system maintenance, rule updates, or new role creation.

## Step 0: Identity Activation [Role: Agent Architect]

<current_step>Step 0: Identity Activation</current_step>
<workflow_instructions>
1. Read `${GLOBAL_SKILLS}\role-agent-architect\SKILL.md`.
2. Initialize meta-analysis in the `<thinking>` tag in English.
</workflow_instructions>

- **[MUST [W-AF-0]]**: Activate Agent Architect identity.

## Step 1: Intake & Analysis [Role: Agent Architect]

<current_step>Step 1: Intake & Analysis</current_step>
<workflow_instructions>
1. Identify the specific incident (Conversation ID/Turn).
2. Analyze deviation from rules or workflow.
3. Output summary of failure in Japanese.
</workflow_instructions>

- **Incident Identification**: Pinpoint where the agent deviated.
- **Root Cause**: Explain why current rules or role definitions failed.

## Step 2: Design & Planning [Role: Agent Architect]

<current_step>Step 2: Design & Planning</current_step>
<workflow_instructions>
1. Propose specific diffs for skills or workflows.
2. Maintain strict linguistic policy (Internal: English, External: Japanese).
3. Create `implementation_plan.md` and wait for approval.
</workflow_instructions>

- **Design**: Craft guardrails to prevent recurrence.
- **Planning**: Define rationale and integration steps.

## Step 3: Execution & Verification [Role: Agent Architect]

<current_step>Step 3: Execution & Verification</current_step>
<workflow_instructions>
1. Apply changes to the governance directory.
2. Audit related skills and sync workflows.
3. Simulate verification of the new guardrails.
</workflow_instructions>

- **Execution**: Apply approved modifications.
- **Verification**: Demonstrate how the new rule prevents identified failures.

## Step 4: Summary [Role: Agent Architect]

<current_step>Step 4: Summary</current_step>
<workflow_instructions>
1. Present the `walkthrough.md` in Japanese.
2. Highlight the "New Guardrails" added.
</workflow_instructions>

- **Reporting**: Finalize the governance upgrade.
