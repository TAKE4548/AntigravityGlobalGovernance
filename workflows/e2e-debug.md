---
name: e2e-debug
description: >
  Cross-repository debugging workflow.
  Systematically isolates and resolves bugs where the Frontend/Backend boundary is unclear.
  Command: /e2e-debug
---

# E2E Verification & Debugging Workflow (/e2e-debug)

A workflow for systematically resolving cross-repository bugs where the cause (Frontend, Backend, or specification deficiency) is unclear.

## Step 0: Prerequisites
- **[MUST [W-E2E-0]]**: In `docs/system/E2E_BACKLOG.md`, both **Frontend (Stub)** and **Backend (Driver)** Gates for the target scenario must be checked.
- **Strictly Prohibited**: Do not start integration (real-device verification) unless both Gates are checked. If incomplete, prioritize unit development in the respective repository.

---

## Step 1: Isolation & Evidence [Role: Tester/Reviewer]
- **[MUST [W-E2E-1]]**: Read `C:\Users\audih\.gemini\antigravity\skills\role-tester-reviewer\SKILL.md` to load verification protocols.
- **Environment Setup**: Start both `mhws-vision-client` and `mhws-vision-server` in the development environment.
- **Browser Reproduction**: Reproduce the issue in the browser and capture API Request/Response (JSON) from the Network tab.
- **Evidence Collection**: Collect server-side logs and browser console logs.

## Step 2: Classification [Role: Architect]
- **[MUST [W-E2E-2]]**: Read `C:\Users\audih\.gemini\antigravity\skills\role-architect\SKILL.md` to prepare for architectural analysis.
Based on the collected evidence, classify the issue into one of the following:
1.  **Unit Bug**: API Request/Response complies with specifications (`openapi.yaml`), but the UI fails or the Backend crashes internally.
    - **Action**: Transition to `/dev` workflows in the respective repository.
2.  **Contract Bug (Specification Inconsistency)**: Frontend request format or Backend response format contradicts `openapi.yaml` or sequence diagrams.
    - **Action**: **[STOP] Immediately cease E2E verification and proceed to Step 3.**

## Step 3: Specification Reconstruction (Lead: Backend) [Role: System Architect]
- **[MUST [W-E2E-3]]**: Read `C:\Users\audih\.gemini\antigravity\skills\role-system-architect\SKILL.md` to handle cross-repo contract design.
In case of a Contract Bug, perform the following in the **Backend repository**, which holds system authority:
- Update documents under `docs/system/` (`openapi.yaml`, sequences, etc.).
- Create specific backlog items (tasks) for each repository based on the fix.
- Present the plan to the user and **obtain approval**.

## Step 4: Task Distribution & Unit Re-fix [Role: Engineer]
- **[MUST [W-E2E-4]]**: Read `C:\Users\audih\.gemini\antigravity\skills\role-engineer\SKILL.md` to load implementation constraints.
Process tasks in each repository based on the approved specifications.
- **[MUST]**: Do not re-integrate until Step 0 (Gate check) is cleared again.

## Step 5: Verification (Re-integration) [Role: Tester]
- Once all Gates pass again, resume real-device integration.
- Update the Status in `E2E_BACKLOG.md` to `[VERIFIED]`.

## Step 6: Final Reporting [Role: Agent Architect]
- **[MUST [W-E2E-6]]**: Read `C:\Users\audih\.gemini\antigravity\skills\role-agent-architect\SKILL.md` to conduct the final governance audit.
- Run `artifact_linter.py` to verify quality, then submit the walkthrough.
