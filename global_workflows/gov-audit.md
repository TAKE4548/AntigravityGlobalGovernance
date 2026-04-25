---
name: gov-audit
description: "Governance & Rule Audit workflow. Used to list current rules and promote them to MUST status. Role: Agent Architect"
---

# Governance Audit Workflow (/gov-audit)

Used when the user wants to review the current set of rules, roles, and workflows to refine their importance (Must/Want).

## Step 0: Identity Activation [Role: Agent Architect]
- **[MUST [W-GA-0]]**: Read `C:\Users\audih\.gemini\antigravity\skills\role-agent-architect\SKILL.md` to load governance audit protocols.

## Step 1: Inventory [Role: Agent Architect]
- Scan all global and local instructions (`GEMINI.md`, `skills/`, `workflows/`).
- Generate a granular list of rules and activities with unique IDs (e.g., G-xx, R-xx, W-xx).
- Use a table format in Japanese to present the inventory.

## Step 2: Selection & Promotion [Role: Agent Architect]
- Ask the user to identify which IDs should be promoted to **Must** (Mandatory) status.
- **Linguistic Check**: For each Must item, verify if it has a corresponding "Prohibited Action" (Shall Not) definition. If not, propose one.

## Step 3: Deployment [Role: Agent Architect]
- Once the selection is confirmed, transition to the `/agent-fix` workflow Step 2/3 to apply the changes to the system.
- Ensure all "Must" items are explicitly documented as prohibitions in the relevant instructions.

## Step 4: Verification
- Output a summary table of the newly promoted Must items and their impact on the system's guardrails.
