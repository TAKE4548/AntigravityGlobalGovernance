---
name: init
description: >
  Workspace initialization workflow.
  Places pointer files according to AntiGravity governance rules.
  Command: /init
---

# Workspace Initialization Workflow (/init)

This workflow initializes a new workspace with AntiGravity governance "pointers" to ensure strict compliance with global rules.

## Step 1: Governance Setup
- Create directory `.agents/rules/` if it doesn't exist.
- Create `.agents/rules/governance.md` with the following content:
  ```markdown
  # Project Governance Pointer

  This project is governed by the AntiGravity Global Governance standards.
  
  **CRITICAL**: All agents MUST strictly follow the rules defined in the global governance file:
  - **Global Rules**: `C:\Users\audih\.gemini\antigravity\governance\GEMINI.md`
  - **Shared Scripts**: `C:\Users\audih\.gemini\antigravity\scripts\` (Use absolute paths ONLY)

  Any local rules in `.agents/` are supplementary and MUST NOT contradict the global governance.
  ```

## Step 2: Skill Pointer Generation
- List all global skills in `C:\Users\audih\.gemini\antigravity\skills\`.
- For each directory `<skill-name>` in the global skills directory:
  - Create directory `.agents/skills/<skill-name>/`.
  - Create `.agents/skills/<skill-name>/SKILL.md` with a pointer to the global definition.
  - **Format**:
    ```markdown
    ---
    name: <skill-name>
    description: "Pointer to global AntiGravity skill: <skill-name>"
    ---
    # <skill-name> (Global Pointer)
    
    This is a pointer to the global AntiGravity skill definition.
    For the latest instructions and protocols, you MUST read the global file:
    `file:///C:/Users/audih/.gemini/antigravity/skills/<skill-name>/SKILL.md`
    ```

## Step 3: Project Conventions Template
- If `.agents/skills/project-conventions/SKILL.md` does not exist:
  - Create it as a template for project-specific rules, ensuring it also points back to the global governance.

## Step 4: Verification
- Verify that the `.agents` structure is correctly created.
- Remind the agent to always use absolute paths for global scripts.
