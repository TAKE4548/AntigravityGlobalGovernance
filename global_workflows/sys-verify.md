---
name: sys-verify
description: >
  Integrated system verification and cross-repo E2E testing workflow.
  Command: /sys-verify
---

# System Verification Workflow (/sys-verify)

Final verification to ensure the entire system meets the Acceptance Criteria (AC) of the master REQ after FE/BE implementations are complete.

## Step 0: Identity Activation [Role: System Architect]
- **[MUST [W-SV-0]]**: Read `${GLOBAL_SKILLS}\role-system-architect\SKILL.md`.

## Step 1: Autonomous Readiness Check
- [STRICT] Check the status of child PBIs in FE and BE repositories.
- **Command**: `python ${GLOBAL_SCRIPTS}\pbi_manager.py --action check-status --id REQ-[REQ_ID] --repos ../frontend,../backend`
- **Rule**: If either status is NOT `done`, halt and report in Japanese: "[REQ_ID] の検証を開始できません。FEまたはBEの実装が完了（done）していません。"

## Step 2: Static Integration Audit
- Use `scout_adapter.py` to verify that the FE/BE implementation matches the SSoT.
  - **Command**: `python ${GLOBAL_SCRIPTS}\scout_adapter.py --mode outline --target ../frontend/src/api,../backend/src/controllers`
- Verify that fetch processes and controller interfaces are perfectly aligned with `openapi.yaml`.

## Step 3: Dynamic E2E Verification
- Execute integrated test scripts (e.g., Playwright) if defined in the System repo.
- **Evidence**: Attach recordings or logs from the E2E execution.

## Step 4: Strict AC Compliance & Closure
- **[MUST [G-02]] Compliance Table**: Output a Markdown checkbox table in Japanese within `walkthrough.md` verifying all ACs from the master REQ.
- If all tests pass, update the master PBI status to `done`.
- Announce completion in Japanese.
