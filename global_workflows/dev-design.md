---
description: "Architectural design and task decomposition phase. Command: /dev-design"
---

# Development Workflow: Design Phase (/dev-design)

<current_workflow>/dev-design</current_workflow>

Use this workflow to perform architectural design and task decomposition based on SSoT (Single Source of Truth) principles.

## Phase 0: Identity Activation [Role: Architect]

<current_step>Phase 0: Identity Activation</current_step>
<workflow_instructions>
1. Read `${GLOBAL_SKILLS}\role-architect\SKILL.md` to load instructions.
2. Initialize thinking process in English.
</workflow_instructions>

- **[MUST [W-DD-0]]**: Activate the Architect identity and load constraints.

## Phase 1: Environment Audit & Requirement Intake [Role: Architect]

<current_step>Phase 1: Environment Audit & Requirement Intake</current_step>
<workflow_instructions>
1. Run `pbi_manager.py list-ready` to present candidates.
2. Run `env_check.py` and check `.agents/context.md`.
3. Load the target PBI and analyze it within the `<thinking>` tag.
</workflow_instructions>

- **Item Selection**: Run `python ${GLOBAL_SCRIPTS}\pbi_manager.py list-ready`.
    - **[MANDATORY TURN-END]**: Present the list to the user and ask for the PBI ID.
- **Environment Check**: Run `python ${GLOBAL_SCRIPTS}\env_check.py`.
- **Requirement Verification**: Load the target PBI file from `docs/backlog/pbi/active/<PBI_ID>.md`.

## Phase 2: Detailed Design [Role: Architect]

<current_step>Phase 2: Detailed Design</current_step>
<workflow_instructions>
1. Build/update `docs/design/<PBI_ID>.md`.
2. Run `doc_mapper.py` for SSoT impact analysis.
3. Use `openapi_parser.py` for surgical API extraction.
4. Document the design and test plan using the `<ssot_reference>` and `<thinking>` tags.
</workflow_instructions>

- **Design Creation**: Build or update `docs/design/<PBI_ID>.md`.
- **SSoT Impact Analysis**: Run `doc_mapper.py` to identify required document updates.
- **API Reference**: Use `openapi_parser.py` to extract resolved endpoints.
- **Verification Design**: Create or update `docs/design/<PBI_ID>-test-plan.md` with explicit CLI commands.

## Phase 3: Task Decomposition & Planning [Role: Architect]

<current_step>Phase 3: Task Decomposition & Planning</current_step>
<workflow_instructions>
1. Run `pbi_manager.py init-task` and `init-test-plan`.
2. Ensure each task is atom-sized (max 3 files).
3. Embed all necessary context into Task Cards (No manual search allowed for Engineer).
4. Create the `implementation_plan.md` in Japanese.
</workflow_instructions>

- **Scaffolding**: Run `pbi_manager.py` to initialize tasks and test plans.
- **[MANDATORY ENCAPSULATION]**: Embed all logic, types, and snippets into the Task Card.
- **Implementation Planning**: Create `implementation_plan.md` in Japanese including architectural changes and impacted docs.

## Phase 4: Pre-Audit & Hand-off [Role: Architect]

<current_step>Phase 4: Pre-Audit & Hand-off</current_step>
<workflow_instructions>
1. Run `ollama_adapter.py` for engineer-audit and qa-audit.
2. Run `artifact_linter.py` and `workflow_validator.py`.
3. Inform the user to start `/dev-task`.
</workflow_instructions>

- **Ollama Audit**: Run audits to verify Task Card and Test Plan quality.
- **Governance Check**: Run `artifact_linter.py` and `workflow_validator.py`.
- **Status Update**: Instruct the user to proceed to `/dev-task`.
