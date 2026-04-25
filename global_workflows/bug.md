---
name: bug
description: "Triage for reported bugs or unexpected behavior. Determines if it is a regression or a latent bug. Command: /bug"
---

# Bug Triage Workflow (/bug)

Used when the user reports errors, broken features, or regressions.

## Step 0: Identity Activation [Role: Hotfix Triager]
- **[MUST [W-BG-0]]**: Read `C:\Users\audih\.gemini\antigravity\skills\role-hotfix-triager\SKILL.md` to load triage protocols.

## Step 1: Fact Finding [Role: Hotfix Triager]
- Use `task-hotfix-triage` to collect symptoms and context (Which screen? What action?).
- Read logs or recent `done` REQs to identify the cause.

## Step 2: Classification
- **Regression**: Caused by a recent `done` REQ. Revert that REQ to `fix-needed`.
- **Latent Bug**: Existed before recent changes. Create a new `REQ` with `Type: defect`.
- **By Design**: Explain the specification to the user. If they wish to change it, switch to the `/wish` workflow.

## Step 3: Routing & Documentation
- **[MUST [W-BG-2]]**: NEVER provide a temporary patch that only hides the symptom. You MUST identify the root cause (logic error, spec mismatch, environment issue) and document it.
- Update `docs/backlog.md` with triage notes.
- Guide the user in Japanese to start the `/dev` workflow for the fix.
