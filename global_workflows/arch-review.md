---
description: >
  Architecture Review for structural debt and complex design decisions.
  Distills "Concerns" into long-term plans.
---

# Architecture Review Workflow (/arch-review)

<current_workflow>/arch-review</current_workflow>

Used to address structural problems and complex technical debt.

## Step 0: Identity Activation [Role: Architect]

<current_step>Step 0: Identity Activation</current_step>
<workflow_instructions>
1. Read `${GLOBAL_SKILLS}\role-architect\SKILL.md`.
2. Initialize architectural analysis in the `<thinking>` tag in English.
</workflow_instructions>

- **[MUST [W-AR-0]]**: Activate Architect identity.

## Step 1: Context Analysis [Role: Architect]

<current_step>Step 1: Context Analysis</current_step>
<workflow_instructions>
1. Analyze `ARCH` items and `Concerns` in the backlog.
2. Evaluate impact on the current architecture using the `<thinking>` tag.
</workflow_instructions>

- **Analysis**: Read `docs/backlog.md` and `docs/architecture.md`.

## Step 2: Option Generation [Role: Architect]

<current_step>Step 2: Option Generation</current_step>
<workflow_instructions>
1. Propose multiple options (Minimal, Recommended, Ideal).
2. Detail trade-offs and record them in the `<design_decisions>` tag.
</workflow_instructions>

- **Options**: Present 2-3 paths with clear pros/cons.

## Step 3: USER Decision [Role: Dev Coordinator]

<current_step>Step 3: USER Decision</current_step>
<workflow_instructions>
1. Present choices to the user in Japanese.
2. Wait for explicit approval of a path.
</workflow_instructions>

- **Consensus**: Secure user decision before proceeding.

## Step 4: Backlog Refinement [Role: Architect]

<current_step>Step 4: Backlog Refinement</current_step>
<workflow_instructions>
1. Update backlog items to reflect the decision.
2. Create necessary implementation REQs.
</workflow_instructions>

- **Deployment**: Transform decision into actionable backlog items.
