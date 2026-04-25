---
description: "Implementation phase for single atom-sized tasks. Command: /dev-task"
---

# Development Workflow: Task Implementation Phase (/dev-task)

Use this workflow to implement a single sub-task from the AI Backlog using localized context.

## Phase 0: Identity Activation [Role: Engineer]
- **[MUST [W-DT-0]]**: Read `${GLOBAL_SKILLS}\role-engineer\SKILL.md` to load role-specific instructions and constraints.

## Phase 1: Task Selection & Isolation [Role: Engineer]
- **Select Task**: Load the current PBI's task file from `docs/backlog/task/active/<PBI_ID>.md`.
    - **[MANDATORY TURN-END]**: Present the pending tasks to the user and ask which one to pick.
- **Hermetic Rule (密封ルール)**:
    - **[MANDATORY RESET]**: Ensure a fresh session or cleared context of unrelated PBI history.
    - **[READ ONLY]**: Read ONLY the specific Task Card file.
    - **[PROHIBITED]**: **DO NOT read `docs/design/PBI-xxx.md` or other spec files.** All necessary context MUST be in the task card.
    - **[必須] コンテキスト分離**: タスクカードに記載された情報のみを前提とし、過去の履歴や広範な探索を排除する。
    - **Target Access**: Open the target files directly using the paths provided in the Task Card.

## Phase 2: Implementation (TDD) [Role: Engineer]
- **Constraint Compliance**: Modify ONLY the files defined in the Task Card.
- **[必須 [R-EN-1]] 探索の厳禁**: 欠落している型定義を探すためにリポジトリを `grep` することを厳禁とする。
- **External Discovery**: If type definitions or callers are missing from the Task Card, run `python ${GLOBAL_SCRIPTS}\code_analyzer.py <root> <symbol>` instead of manually searching files.
- **Escalation**: If the Task Card information is insufficient to implement, STOP and escalate to `/dev-design` for a Task Card update. DO NOT attempt to find the information by reading unrelated files.

## Phase 3: Verification & Sync [Role: Engineer]
- **Verify**: Run the specific unit tests for this task.
- **Update Status**: instructions for the user to proceed to next task or `/dev-verify`.
