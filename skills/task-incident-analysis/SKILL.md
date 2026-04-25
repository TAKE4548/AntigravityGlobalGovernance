---
name: task-incident-analysis
description: >
  Deep dive investigation for reported bugs. 
  Focuses on root cause isolation and classification.
---

# Incident Analysis Task

Your goal is to pinpoint the root cause of a reported issue and classify it without suggesting solutions.

## 1. Compliance (CRITICAL)
- **STRICT READ-ONLY**: You are prohibited from making any changes to the source code.
- **EVIDENCE-DRIVEN**: Every conclusion must be backed by a log entry, a line of code, or a specification document.

## 2. Investigation Protocol

1.  **Fact Gathering**:
    - Identify the failing screen/component.
    - Collect reproduction steps.
    - Run `${GLOBAL_SCRIPTS}\ollama_adapter.py` on logs if provided.
2.  **Logic Tracing**:
    - Use `code_analyzer.py` to find the relevant logic.
    - Compare the actual behavior with the expected behavior defined in `docs/`.
3.  **Classification**:
    - **Type A**: Code != SSoT.
    - **Type B**: Code == SSoT, but SSoT is inadequate.
4.  **Impact Analysis**:
    - Does this affect other components?
    - Does it span multiple repositories?

## 3. Reporting Requirements
The report (in Japanese) MUST include:
- **Reproduced**: Yes/No
- **Evidence**: Specific line numbers or log snippets.
- **Classification**: Type A or Type B.
- **Routing Suggestion**: Which workflow to start next (/dev-design, /wish, or /sys-design).

## 4. Boundaries
- Do not provide code snippets for the fix.
- Do not update the implementation plan.
