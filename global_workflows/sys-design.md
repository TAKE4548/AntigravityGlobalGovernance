---
name: sys-design
description: >
  Cross-repository system design and API contract definition workflow.
  Drives detail through scouting existing code and proactive questioning.
  Command: /sys-design
---

# System & API Design Workflow (/sys-design)

An interactive workflow for establishing strict interface contracts and sequences across repositories. This workflow scouts existing code in FE/BE, refines specifications through questioning, and encapsulates the design into a System PBI with an integrated test plan.

## Step 0: Identity Activation [Role: System Architect]
- **[MUST [W-SD-0]]**: Read `${GLOBAL_SKILLS}\role-system-architect\SKILL.md` to load cross-repo design and orchestration protocols.

## Step 1: Requirement Intake & Scouting [Role: System Architect]
- Receive broad goals or user flows.
- **[STRICT] Scouting Phase**: Perform a deterministic extraction of existing specifications and types using `scout_adapter.py`.
  - **Overview**: `python ${GLOBAL_SCRIPTS}\scout_adapter.py --mode outline --target ../frontend,../backend`
  - **Drill-down**: Use `--mode drill-down` for specific files if investigating a bug or complex logic.
- Based on the scouting, identify the impact on existing `openapi.yaml` or state management.

## Step 2: Deep Dive Phase (Resolution Improvement) [Role: System Architect]
- Refine specifications through sharp technical questioning:
  1. **SSoT & State Management**: Which side owns the master data?
  2. **API Boundaries**: Synchronous (REST) or Asynchronous?
  3. **Payload Structure**: Specific properties in JSON Request/Response.
  4. **Error Handling**: Validation errors and timeout behaviors.

## Step 3: PBI-SYS Design & BA-Audit [Role: System Architect]
- Create the System PBI encapsulation: `docs/design/PBI-SYS-[REQ_ID].md`.
- **[MUST [SD-PROC]] Strict Generation Procedure**:
  1. **Format**: Initialize the file using `pbi_manager.py create-template`.
  2. **Content**: Define API contracts, domain models, and the **Integrated Test Plan (E2E Scenarios)**.
  3. **BA-Audit**: Run `python ${GLOBAL_SCRIPTS}\ollama_adapter.py ba-audit --target docs/design/PBI-SYS-[REQ_ID].md`.
  4. **Reflection**: Fix any ambiguities or missing edge cases identified by the audit.
  5. **Final Check**: Ensure all Acceptance Criteria (AC) are covered.

## Step 4: Consensus & Implementation Plan
- Present the system architecture and flow drafts to the user.
- Once agreed, create the `implementation_plan.md` in Japanese.
- **Note**: Do NOT modify FE/BE code at this stage. Only `openapi.yaml` in the System repo may be planned for modification.
