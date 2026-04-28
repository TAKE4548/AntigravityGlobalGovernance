---
description: "Implementation phase for single atom-sized tasks. Command: /dev-task"
---

# Development Workflow: Task Implementation Phase (/dev-task)

<current_workflow>/dev-task</current_workflow>

Use this workflow to implement a single sub-task from the AI Backlog using localized context.

## Phase 0: Identity Activation [Role: Engineer]

<current_step>Phase 0: Identity Activation</current_step>
<workflow_instructions>
1. Read `${GLOBAL_SKILLS}\role-engineer\SKILL.md` to load role instructions.
2. Initialize implementation analysis in the `<thinking>` tag.
</workflow_instructions>

- **[MUST [W-DT-0]]**: Load role-specific instructions and constraints.

## Phase 1: Task Selection & Isolation [Role: Engineer]

<current_step>Phase 1: Task Selection & Isolation</current_step>
<workflow_instructions>
1. Present pending tasks to the user and ask for selection.
2. Load the Task Card into the `<target_task_card>` tag.
3. Perform a mandatory context reset.
</workflow_instructions>

- **Select Task**: Load the current PBI's task file.
    - **[MANDATORY TURN-END]**: Ask the user which task to pick.
- **Hermetic Rule (密封ルール)**:
    - **[READ ONLY]**: Read ONLY the specific Task Card file.
    - **[PROHIBITED]**: DO NOT read PBI specs or unrelated files.
    - **Isolation**: Use strictly the information within the `<target_task_card>`.

## Phase 2: Implementation (TDD) [Role: Engineer]

<current_step>Phase 2: Implementation (TDD)</current_step>
<workflow_instructions>
1. Modify ONLY the files defined in the Task Card.
2. Follow the Red-Green-Refactor cycle.
3. Use `code_analyzer.py` if symbol definitions are missing from the Task Card.
</workflow_instructions>

- **Constraint Compliance**: Modify ONLY specified files.
- **[PROHIBITED]**: NEVER use `grep` or `read_file` for exploration.
- **Escalation**: If info is insufficient, STOP and escalate to `/dev-design`.

## Phase 3: Verification & Sync [Role: Engineer]

<current_step>Phase 3: Verification & Sync</current_step>
<workflow_instructions>
1. Run unit tests for the current task.
2. Isolate test results in the `<execution_evidence>` tag.
3. Update status and instruct the user to proceed.
</workflow_instructions>

- **Verify**: Run unit tests.
- **Update Status**: Prepare for the next task or `/dev-verify`.
