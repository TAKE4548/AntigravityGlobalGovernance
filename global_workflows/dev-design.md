---
description: "Architectural design and task decomposition phase. Command: /dev-design"
---

# Development Workflow: Design Phase (/dev-design)

Use this workflow to perform architectural design and task decomposition based on SSoT (Single Source of Truth) principles.

## Phase 0: Identity Activation [Role: Architect]
- **[MUST [W-DD-0]]**: Read `${GLOBAL_SKILLS}\role-architect\SKILL.md` to load role-specific instructions and constraints.

## Phase 1: Environment Audit & Requirement Intake [Role: Architect]
- **Item Selection**: Run `python ${GLOBAL_SCRIPTS}\pbi_manager.py list-ready`.
    - **[MANDATORY TURN-END]**: Present the list to the user in Japanese and ask which PBI ID to proceed with. DO NOT proceed to Phase 2 until the user responds.
- **Environment Check**: Run `python ${GLOBAL_SCRIPTS}\env_check.py`.
    - **[LOCAL OVERRIDE]**: Check `.agents/context.md` at the repository root.
- **Requirement Verification**: Load the target PBI file from `docs/backlog/pbi/active/<PBI_ID>.md`.

## Phase 2: Detailed Design [Role: Architect]
- **Design Creation**: Build or update `docs/design/<PBI_ID>.md`.
    - **[SSoT Impact Analysis]**: Run `python ${GLOBAL_SCRIPTS}\doc_mapper.py docs/ <related_source_path>` to identify any existing common documentation that requires updates.
    - **API Reference (Surgical Extraction)**:
        1. Run `python ${GLOBAL_SCRIPTS}\openapi_parser.py ${API_SPEC_PATH} list-endpoints` to identify target endpoints.
        2. Run `python ${GLOBAL_SCRIPTS}\openapi_parser.py ${API_SPEC_PATH} get-endpoint <path> <method>` to extract the full definition (including resolved $refs).
        3. **[TOKEN OPTIMIZATION]**: Embed only the extracted snippets into the Task Card.
- **Verification Design**: Create or update `docs/design/<PBI_ID>-test-plan.md`.
    - **[STRICT FORMAT]**: The test plan MUST NOT contain qualitative manual steps. It MUST consist of explicit CLI commands (`npm test`, `pytest`) and assertions based on exact values, DOM selectors, or console logs.

## Phase 3: Task Decomposition & Planning [Role: Architect]
- **Scaffolding**: Run `python ${GLOBAL_SCRIPTS}\pbi_manager.py init-task <PBI_ID> --symbol <TargetSymbol>` and `init-test-plan <PBI_ID>`.
- **Atom-sized Constraint**: Each task MUST be small enough to modify a **maximum of 3 source files**.
- **[MANDATORY ENCAPSULATION]**: Embed all necessary logic, type definitions, and code snippets from related files into the task card. The Engineer MUST be able to implement without opening the PBI spec or searching for type definitions.
- **[MUST EXTRACT]**: Architect MUST use `read_file` or `code_analyzer.py` to physically read the target source code and type definitions BEFORE writing the Task Card. Do not hallucinate code snippets.
- **Implementation Planning**: Create `implementation_plan.md` in **Japanese** to present:
    1. Proposed architectural changes and the breakdown of tasks.
2. **[MANDATORY] Impacted Documents List**: List docs identified by `doc_mapper.py`.

## Phase 4: Pre-Audit & Hand-off [Role: Architect]
- **Ollama Audit (Engineer View)**: Run `python ${GLOBAL_SCRIPTS}\ollama_adapter.py engineer-audit docs/backlog/task/active/<PBI_ID>.md`.
- **Ollama Audit (QA View)**: Run `python ${GLOBAL_SCRIPTS}\ollama_adapter.py qa-audit docs/design/PBI-<PBI_ID>-test-plan.md`.
- **Feedback Loop**: Apply feedback from audits to the task card and test plan.
- **Governance Check**: Run `python ${GLOBAL_SCRIPTS}\artifact_linter.py docs/`.
- **Audit**: Run `python ${GLOBAL_SCRIPTS}\workflow_validator.py design-end <PBI_ID>`.
- **Status Update**: instruct the user to start implementation via `/dev-task`.
