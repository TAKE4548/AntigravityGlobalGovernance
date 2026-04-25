---
name: dev
description: "Formal development session workflow. Tracks progress via session.md. (v1.7)"
---

# Development Workflow (/dev) [DEPRECATED]

> [!CAUTION]
> **[DEPRECATED] 3セッション分離モデルへの移行**
> このワークフローはコンテキスト汚染を招く可能性があるため非推奨となりました。
> 今後は以下の新しいワークフローを順次実行してください：
> 1. **`/dev-design`**: 設計・タスク分解
> 2. **`/dev-task`**: 独立タスクの個別実装（タスクごとに破棄）
> 3. **`/dev-verify`**: 統合検証・クローズ処理

## Step 0: Session Initialization [Role: Dev Coordinator]
- **Environment Check**: Ensure the application's development server is running. (e.g., FastAPI at 8000, Vite at 5173, or Streamlit at 8501). If not, start it using the repository's standard start script (e.g., `./start.ps1`, `npm run dev`, or `start.bat`).
- **Deterministic Check**: Run all Linters under `.agents/scripts/` (backlog, asset, doc_link). Propose fixes if deficiencies are found before proceeding.
- Read `docs/session.md` and `docs/backlog.md`.
- **Resumption Logic**: If `docs/session.md` is `active`, confirm with the user whether to resume or start a new session.
- **Protocol**: Transition state to `active` and record the target REQ in `session.md`.

## Step 1: Item Selection & Setup [Role: Dev Coordinator]
- **[MUST [W-DV-1]]**: NEVER propose a new plan or path until you have fully ingested the current project state (backlog, latest PRs, and `docs/`).
- Present `ready` or `fix-needed` items for the user to select a REQ.
- **Git Setup**: Run `git checkout -b <feat/fix>/REQ-XXX`.
- **Path Selection**: Choose Step 3 (Architect) for new features/large fixes, or Step 4 (UX) for minor UI changes.

## Step 2: Handoff Verification [Role: Dev Coordinator]
- Verify that the AC for the REQ is clear and hand off to the next role.

## Step 3: High-Level Design & SSoT Update [Role: Architect]
- **UX Strategy Integration**: For UI/UX-related tasks, consult with the **UX Designer** at this stage to solidify the core user experience.
- **[MUST [W-DV-2]] SSoT Priority**: BEFORE proposing an implementation plan, you MUST identify and update the relevant SSoT documents (e.g., `docs/system/openapi.yaml`, `SPEC.md`, `E2E_BACKLOG.md`).
- Perform impact analysis and create designs (e.g., `docs/designs/*.md`) including these specification updates.
- **Trade-off Disclosure**: A "Trade-offs and Constraints" section is MANDATORY in the plan.
- **UX Review**: Receive audit feedback from the UX Designer after design completion.

## Step 3.5: Design Approval Gate [Role: Dev Coordinator]
- **[MANDATORY TURN-END]**: Present the **Specification/Doc changes ONLY** to the user in Japanese. 
- You MUST obtain explicit approval for the *Interface and Architecture* before proceeding to the `implementation_plan.md` (Step 5).
- Use `ask_question` to ensure the user has reviewed the doc changes.

## Step 4: UI/UX Specification [Role: UX Designer]
- *Condition: Only if UI changes are involved.*
- Create specific visual specifications (`docs/ui_spec.md`).
- As an expert, actively propose improvements or dissent against user requests if they compromise UX.

## Step 5: Approval Gate [Role: Dev Coordinator]
- Present the design and implementation plan to the user in Japanese.
- **[MUST [W-DV-3]]**: After presenting the `implementation_plan.md`, the agent MUST NOT use any file modification tools (Write/Edit) until receiving explicit user approval ("Approve", "OK", etc.).
- **MANDATORY TURN-END**: You MUST set `RequestFeedback: true` in the `implementation_plan.md` artifact metadata OR output a direct question using the `ask_question` tool.
- DO NOT proceed to Step 6 until explicit user approval is received.

## Step 6: Implementation [Role: Engineer]
- Perform code implementation, unit testing, and browser verification.
- **Evidence Management**: Save evidence images to `.gemini/` outside the repository and link them in the Walkthrough.
- **Design Discrepancy Reporting**: If implementation deviates from the original design (due to technical constraints or UX findings), the Engineer MUST create a **DDS (Design Discrepancy Summary)** at the end of this step.
- **AC Checklist**: Include an AC verification table in the completion report as per the template.

## Step 6.5: Document Sync & Approval [Role: Architect / UX Designer]
- *Condition: Required if a DDS was reported or significant trial-and-error occurred.*
- **Doc Update Proposal**: Based on the DDS, the Architect/UX Designer creates an `implementation_plan.md` (or similar proposal) to update the relevant specification files in `docs/`.
- **Approval Gate**: Present the proposal to the user in Japanese.
- **Execution**: Upon approval, update the specification documents to align with the final implementation.
- **MANDATORY**: Ensure the SSoT is updated BEFORE handing off to the Tester.

## Step 7: Verification & Review [Role: Tester/Reviewer]
- **SSoT Compliance Audit**: Verify that the implementation matches the **latest updated specifications** (from Step 6.5). Discrepancies between code and docs result in a FAIL.
- **Red Teaming**: Audit the implementation from a "How to break it" perspective and present the AC verification table.
- **Verdict**: Issue PASS / FAIL / CONCERNS. If deficiencies are found, return to Step 6.
- **MANDATORY TURN-END**: End your turn immediately after issuing the verdict.

## Step 8: Finalization & SSoT Verification [Role: Dev Coordinator]
- **Linter Final Check**: Run all Linter scripts again (including doc-link checks) to ensure absolute consistency.
- **Backlog Sync**: Change status to `done` and add the completion date (YYYY-MM-DD).
- **Session Exit**: Reset `session.md` to `inactive` and close the session.
- Present the Walkthrough in Japanese and provide instructions for merging the branch.

---

## Escalation Path (IMPASSE Branch)
- If an `[IMPASSE]` occurs in Step 3 or 6, the Coordinator changes the session state to `escalated` and discusses countermeasures (requirement relaxation, archiving, etc.) with the user.
