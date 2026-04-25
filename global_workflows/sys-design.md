---
name: sys-design
description: >
  Cross-repository system design and API contract definition workflow.
  Drives detail through proactive questioning for sequences and payloads.
  Command: /sys-design
---

# System & API Design Workflow (/sys-design)

An interactive workflow for establishing strict interface contracts and sequences, such as frontend-backend integration. This workflow starts from vague user requirements and aims to maximize the resolution of specifications through proactive questioning from the agent.

## Step 0: Identity Activation [Role: System Architect]
- **[MUST [W-SD-0]]**: Read `${GLOBAL_SKILLS}\role-system-architect\SKILL.md` to load cross-repo design and contract protocols.

## Step 1: Vision Hearing [Role: System Architect]
- Receive broad goals or user flows from the user.
- **[MUST [SD-01]]**: NEVER start creating an `implementation_plan.md` or coding at this stage.

## Step 2: Deep Dive Phase (Resolution Improvement) [Role: System Architect]
- To transform user requests into concrete API and sequence specifications, **ALWAYS present questions and refine specifications from the following perspectives**:
  1. **SSoT & State Management**: Which side (Frontend or Backend) owns the master data?
  2. **API Boundaries & Communication**: Synchronous (REST) or Asynchronous (Event-driven, Polling)?
  3. **Payload Structure**: What specific properties should be included in Request/Response (JSON hierarchy, etc.)?
  4. **Error Handling & Edge Cases**: How to handle validation errors and state transitions during timeouts?
  5. **Impact on Existing Contracts**: Use `python ${GLOBAL_SCRIPTS}\openapi_parser.py <path> list-endpoints` to verify if it breaks existing specifications like `openapi.yaml`.

## Step 3: Draft Presentation & Consensus Building (Loop Point)
- When the specification resolution is high enough (types, endpoints, and branches are clear), present the system architecture and user flow drafts textually to obtain final user agreement.
- **[MUST [SD-02]]**: **If agreement is not obtained or additional concerns are raised, immediately return to Step 2 and re-define details through further questioning.** (Loop between Step 2 and Step 3).

## Step 4: Output Generation & Backlog Entry [Role: System Architect]
- Once final agreement is obtained, output the `implementation_plan.md` based on the consensus.
- **[NEW] Backlog Entry**: Run `python ${GLOBAL_SCRIPTS}\pbi_manager.py create "<Title>" "ready"` to record the design outcome.
- The plan MUST include:
  - Specific changes to API specifications like `openapi.yaml`.
  - Structure and updates for sequence diagrams in `docs/system/sequences/` (Mermaid integration).
  - Updates to user experience flows in `docs/system/user_workflows/`.
  - Explicit "Trade-off Disclosure".
