---
description: >
  Cross-repository system design and API contract definition workflow.
  Drives detail through scouting existing code and proactive questioning.
  Command: /sys-design
---

# System & API Design Workflow (/sys-design)

<current_workflow>/sys-design</current_workflow>

An interactive workflow for establishing strict interface contracts and sequences across repositories.

## Step 0: Identity Activation [Role: System Architect]

<current_step>Step 0: Identity Activation</current_step>
<workflow_instructions>
1. Read `${GLOBAL_SKILLS}\role-system-architect\SKILL.md` to load protocols.
2. Initialize thinking process in English.
</workflow_instructions>

- **[MUST [W-SD-0]]**: Activate System Architect identity and load constraints.

## Step 1: Requirement Intake & Scouting [Role: System Architect]

<current_step>Step 1: Requirement Intake & Scouting</current_step>
<workflow_instructions>
1. Receive broad goals and perform a deterministic extraction using `scout_adapter.py`.
2. Analyze existing specifications and types across frontend/backend.
3. Identify impact on `openapi.yaml` within the `<thinking>` tag.
</workflow_instructions>

- **Scouting Phase**: Use `scout_adapter.py` to outline FE/BE specifications.
- **Impact Identification**: Identify changes required in state management or API contracts.

## Step 2: Deep Dive Phase (Resolution Improvement) [Role: System Architect]

<current_step>Step 2: Deep Dive Phase (Resolution Improvement)</current_step>
<workflow_instructions>
1. Refine specifications through sharp technical questioning (SSoT, State, Boundaries, Payloads, Errors).
2. Use the `<thinking>` tag to analyze sequence logic and interface boundaries.
</workflow_instructions>

- **Technical Questioning**: Define data ownership, API boundaries, and payload structures.
- **Detail Demand**: Refuse implementation plan creation until resolution is high.

## Step 3: PBI-SYS Design & BA-Audit [Role: System Architect]

<current_step>Step 3: PBI-SYS Design & BA-Audit</current_step>
<workflow_instructions>
- [ ] **Step 3-2: Create PBI-SYS**
    - Create `docs/design/PBI-SYS-[REQ_ID].md`.
    - **[MUST]** Use XML tags for distribution:
        - `<system_context>`: Common specs.
        - `<frontend_pbi_spec>`: FE requirements.
        - `<backend_pbi_spec>`: BE requirements.
    - Reference: `GEMINI.md#8-6`.
3. Run `ollama_adapter.py ba-audit` and reflect findings.
</workflow_instructions>

- **Design Creation**: Initialize and populate the System PBI.
- **BA-Audit**: Obtain objective feedback on design ambiguities and fix them.

## Step 4: Consensus & Implementation Plan [Role: System Architect]

<current_step>Step 4: Consensus & Implementation Plan</current_step>
<workflow_instructions>
1. Present the system architecture and flow drafts to the user.
2. Create the `implementation_plan.md` in Japanese after consensus.
</workflow_instructions>

- **Consensus**: Ensure the user approves the overall architecture.
- **Implementation Planning**: Define the roadmap for System-repo modifications and cross-repo dispatch.
