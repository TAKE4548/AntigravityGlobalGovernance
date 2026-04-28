---
description: >
  System implementation and cross-repo task dispatch workflow.
  Command: /sys-task
---

# System Implementation & Dispatch Workflow (/sys-task)

<current_workflow>/sys-task</current_workflow>

Read the encapsulated `PBI-SYS`, update the SSoT in the System repository, and dispatch tasks to child repos.

## Step 0: Identity Activation [Role: System Architect]

<current_step>Step 0: Identity Activation</current_step>
<workflow_instructions>
1. Read `${GLOBAL_SKILLS}\role-system-architect\SKILL.md`.
2. Prepare for SSoT modification and task dispatch.
</workflow_instructions>

- **[MUST [W-ST-0]]**: Activate System Architect identity.

## Step 1: SSoT Implementation [Role: System Architect]

<current_step>Step 1: SSoT Implementation</current_step>
<workflow_instructions>
1. Read the `PBI-SYS` and update managed files (e.g., `openapi.yaml`) in the System repo.
2. Commit changes using the `/commit` workflow BEFORE dispatching.
</workflow_instructions>

- **Implementation**: Physically update API contracts and designs in the System repo.
- **[MUST [G-ST-1]]**: Changes MUST be committed before proceeding to dispatch.

## Step 2: Cross-Repo Dispatch [Role: System Architect]

<current_step>Step 2: Cross-Repo Dispatch</current_step>
<workflow_instructions>
1.- [ ] **Step 1-2: Automated Dispatching**
    - Run `python ${GLOBAL_SCRIPTS}\pbi_dispatcher.py --source docs/design/PBI-SYS-[REQ_ID].md --targets ../frontend,../backend`.
    - **[CHECK]** Verify `<dispatch_report>` for any missing specs.
</workflow_instructions>

- **Dispatch**: Create `ready` child PBIs in target repositories.
- **[STRICT]**: If dispatcher fails, declare [IMPASSE].

## Step 3: Hand-off Announcement [Role: System Architect]

<current_step>Step 3: Hand-off Announcement</current_step>
<workflow_instructions>
1. List created child PBIs and instruct the user to start `/dev-design` in child repos.
2. Output final message in Japanese.
</workflow_instructions>

- **Announcement**: Formally hand off tasks to the next phase in child repositories.
