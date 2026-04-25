---
name: sys-task
description: >
  System implementation and cross-repo task dispatch workflow.
  Command: /sys-task
---

# System Implementation & Dispatch Workflow (/sys-task)

Read the encapsulated `PBI-SYS` designed in `/sys-design`, physically update the SSoT (e.g., `openapi.yaml`) in the System repository, and dispatch implementation tasks to the FE and BE repositories.

## Step 0: Identity Activation [Role: System Architect]
- **[MUST [W-ST-0]]**: Read `${GLOBAL_SKILLS}\role-system-architect\SKILL.md`.

## Step 1: SSoT Implementation
- Read `docs/design/PBI-SYS-[REQ_ID].md`.
- Update managed files (like `openapi.yaml`) in the System repo as per the design.
- **[MUST [G-ST-1]]**: Modified files MUST be committed to Git using `/commit` workflow before dispatching.

## Step 2: Cross-Repo Dispatch
- Create child PBIs in the FE/BE repositories in `ready` state.
- **Command**: `python ${GLOBAL_SCRIPTS}\pbi_dispatcher.py --source docs/design/PBI-SYS-[REQ_ID].md --targets ../frontend,../backend`
- **[STRICT]**: If the dispatcher fails, declare an [IMPASSE] and report in Japanese. Do NOT force completion.

## Step 3: Hand-off Announcement
- Instruction for User (Output in Japanese):
  - List the successfully created child PBIs (e.g., `REQ-XXX-FE`, `REQ-XXX-BE`).
  - Instruct the user: "FE/BEリポジトリ側で `/dev-design` を開始してください" (Please start `/dev-design` in the FE/BE repositories).
