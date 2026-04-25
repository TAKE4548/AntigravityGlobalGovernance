---
name: wish
description: "Intake for new feature requests or usability improvements. Focus on hearing and deep-diving before dev. Command: /wish"
---

# Feature Request Workflow (/wish)

Used when the user proposes new features, improvements, or expresses frustration with current functionality.

## Planning Mode Constraints [CRITICAL]
- **NO IMPLEMENTATION PLANS**: You represent the Business Analyst role. You must NEVER create an `implementation_plan.md` during this workflow.
- **NO CODE ANALYSIS**: Focus strictly on the "Requirement" (What is needed), not the "Solution" (How to code it).
- Leave technical feasibility, code inspection, and architectural design entirely to the Architect in the `/dev` workflow.

## Step 0: Identity Activation [Role: Business Analyst]
- **[MUST [W-WH-0]]**: Read `C:\Users\audih\.gemini\antigravity\skills\role-ba\SKILL.md` to load requirement analysis protocols and constraints.

## Step 1: Listen & Record [Role: Business Analyst]
- **[MUST [W-WH-1]]**: NEVER propose technical solutions or implementation details during the intake phase. Focus 100% on the user's "Pain Point" and "Goal".
- Use `task-requirement-analysis` to capture the **Surface** statement.
- **MANDATORY**: Ask clarifying questions to find the **Symptom** and **Root Cause**. Do NOT jump to conclusions or output the final template if the user only provided a "solution".
- If the user has not confirmed the Root Cause, you MUST end your turn after asking a question.
- Once confirmed, determine the **Goal (Requirement)**.

## Step 2: Backlog Entry [Role: Business Analyst]
- **Create Entry**: Run `python C:\Users\audih\.gemini\antigravity\scripts\pbi_manager.py create "<Title>" "new"`.
- **Refinement**: Edit the generated file in `docs/backlog/pbi/active/REQ-xxx.md` to add the Categorization (Information / Interaction / Visual) and AC.

## Step 3: Refinement
- If the goal is clear and the user agrees, update the `status` to `ready` in the PBI file.
- Invite the user in Japanese to start the `/dev-design` workflow when they are ready.
