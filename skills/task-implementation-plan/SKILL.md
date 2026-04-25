---
name: task-implementation-plan
description: "Create a low-level implementation design from the architect's and UX designer's specifications."
---

# Implementation Plan Task

## 1. Input
- `docs/designs/{feature-name}.md` (Architect's technical design)
- `docs/ui_spec.md` (UX Designer's interaction and layout design, if applicable)

## 2. Output
- **Implementation Sequence** (ordered by dependency).
- **Granular logic updates** (files and functions).
- **Test Design Strategies** (Unit / Manual).
- **Trade-off Disclosure (MANDATORY)**: Following `project-conventions/resources/templates.md`, you must explicitly document downsides, constraints, or side effects of the implementation.

## 3. Steps
0. **SSoT Validation**: Confirm that all relevant Single Source of Truth (SSoT) documents (e.g., `openapi.yaml`, `SPEC.md`, `E2E_BACKLOG.md`) have been updated and approved in a prior "Design Approval Gate". If not, return to the Architecture phase.
1. **Spec Audit**: Read the relevant section of `backlog.md`. List all Requirements and ACs that must be addressed.
2. **Intermediate Design**: If the feature has complexity, create `docs/designs/{feature-name}.md` and/or `docs/ui_spec.md` BEFORE the implementation plan.
3. Break down the high-level designs into concrete coding tasks.
4. Order the tasks based on module dependencies.
5. Determine the testing strategy for each subtask.
6. **Define Red Teaming Scenarios**: Following `project-conventions/resources/templates.md`, include failure scenarios ("How could this feature break?") in the verification plan.
7. **Requirement Mapping**: Create a table in `implementation_plan.md` mapping every single AC from the backlog to a specific implementation detail. **DO NOT paraphrase ACs; quote them exactly.**

## 4. MANDATORY GATE: Approval & Questions
- Strictly follow the **"Universal Integrity Gates"** in `project-conventions/SKILL.md`.
- If the plan contains "Open Questions," you must end your turn immediately and wait for user feedback.

## 5. [PROHIBITED ACTIONS]
- **[MUST [S-IP-1]]**: NEVER paraphrase or summarize Acceptance Criteria in the requirement mapping table. You MUST quote them exactly from the backlog to prevent "slicing off" inconvenient requirements.
- **[MUST [S-IP-2]]**: NEVER skip the "Trade-off Disclosure" section. If you believe there are no downsides, you MUST state the reasons for that belief.
