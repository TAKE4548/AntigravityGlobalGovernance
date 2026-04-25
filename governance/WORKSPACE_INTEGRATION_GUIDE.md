# workspace-integration-guide

This document provides a reference for configuring workspace-local `.agents/` definitions to complement the generalized global governance. Since global rules are port- and framework-agnostic, each repository MUST specify its own constraints to ensure agent reliability.

---

## 1. Streamlit Repositories (Monolithic / Hybrid)

For projects using Streamlit as the primary UI and logic runner.

### Recommended Local Rules (`.agents/rules/governance.md`)
- **Port Constraint**: Explicitly state that the dev server runs on `localhost:8501`.
- **State Management**: Rule to prevent agents from bypassing `st.session_state` for cross-widget communication.
- **Widget Keys**: Rule for using unique, deterministic keys (e.g., based on item IDs) to prevent `StreamlitDuplicateElementKey` errors.

### Recommended Skill Updates (`.agents/skills/backend-conventions/SKILL.md`)
- Focus on integrating Vision logic directly into Streamlit callbacks if decoupled services aren't used yet.

---

## 2. Backend API Repositories (FastAPI / Python)

For decoupled backend services providing APIs for Vision or general data management.

### Recommended Local Rules (`.agents/rules/governance.md`)
- **Port Constraint**: Explicitly state that the API server runs on `localhost:8000`.
- **Async Integrity**: Rule mandating `async/await` for I/O bound operations (especially Vision inference) to prevent blocking the event loop.
- **SSoT Compliance**: Reference `docs/system/API_CONTRACT.md` as the source of truth for all Pydantic models.

### Recommended Skill Updates (`.agents/skills/backend-conventions/SKILL.md`)
- Mandate the use of the Service/Core layered architecture.
- Prohibit mixing routing logic with business logic.

---

## 3. Frontend Web Repositories (Vite + React / Tailwind)

For decoupled frontend applications.

### Recommended Local Rules (`.agents/rules/governance.md`)
- **Port Constraint**: Explicitly state that the dev server runs on `localhost:5173`.
- **Design Token Compliance**: Rule strictly prohibiting ad-hoc hex codes in JSX/CSS. All colors/spacing MUST use tokens from `src/index.css` or the specific design system file.
- **Mock-First Development**: Rule to use mock data or MSW if the backend API is not yet available, ensuring frontend progress doesn't stall.

### Recommended Skill Updates (`.agents/skills/role-ux-designer/SKILL.md`)
- Focus on component modularity and reuse.
- Mandate the definition of "Non-Ideal States" for every major view.

---

## 4. Universal Workspace Checks

Every workspace should ensure its `.agents/scripts/` directory contains:
- `backlog_linter.py`: To verify compliance with the `task-backlog-management` header format.
- `artifact_linter.py`: To check for mandatory Japanese deliverables (`implementation_plan.md`, `walkthrough.md`).
