---
description: "Governance & Rule Audit workflow. Used to list current rules and promote them to MUST status. Role: Agent Architect"
---

# Governance Audit Workflow (/gov-audit)

<current_workflow>/gov-audit</current_workflow>

Used for reviewing and refining system rules and protocols.

## Step 0: Identity Activation [Role: Agent Architect]

<current_step>Step 0: Identity Activation</current_step>
<workflow_instructions>
1. Read `${GLOBAL_SKILLS}\role-agent-architect\SKILL.md`.
2. Initialize rule inventory analysis in the `<thinking>` tag in English.
</workflow_instructions>

- **[MUST [W-GA-0]]**: Activate Agent Architect identity.

## Step 1: Inventory [Role: Agent Architect]

<current_step>Step 1: Inventory</current_step>
<workflow_instructions>
1. Scan instructions and generate a list of rules with unique IDs.
2. Present the inventory table in Japanese.
</workflow_instructions>

- **Inventory**: Categorize current rules, roles, and workflows.

## Step 2: Selection & Promotion [Role: Agent Architect]

<current_step>Step 2: Selection & Promotion</current_step>
<workflow_instructions>
1. Ask the user which rules to promote to "Must" status.
2. Verify that each "Must" has a corresponding "Prohibited Action" in the `<thinking>` tag.
</workflow_instructions>

- **Promotion**: Elevate rule importance and define prohibitions.

## Step 3: Deployment [Role: Agent Architect]

<current_step>Step 3: Deployment</current_step>
<workflow_instructions>
1. Transition to `/agent-fix` to apply confirmed changes.
2. Ensure explicit documentation of new prohibitions.
</workflow_instructions>

- **Execution**: Apply refined governance to the system.

## Step 4: Verification [Role: Agent Architect]

<current_step>Step 4: Verification</current_step>
<workflow_instructions>
1. Output a summary of promoted rules and their impact.
</workflow_instructions>

- **Report**: Finalize the governance audit.
