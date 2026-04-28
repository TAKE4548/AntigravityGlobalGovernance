---
description: "Cross-repository commit workflow with security guardrails. Command: /commit"
---

# Commit Workflow (/commit)

<current_workflow>/commit</current_workflow>

Safely commit changes after a security audit and AC verification.

## Step 1: Security Audit

<current_step>Step 1: Security Audit</current_step>
<workflow_instructions>
1. Run `pre_commit_linter.py` to check for absolute paths and secrets.
2. Halt if violations are found and report in the `<execution_evidence>` tag.
</workflow_instructions>

- **Action**: Perform deterministic scan.
- **Error Handling**: STOP and report specific violations to the user.

## Step 2: Verification

<current_step>Step 2: Verification</current_step>
<workflow_instructions>
1. Ensure `walkthrough.md` contains the mandatory AC compliance table.
2. Verify table integrity in the `<thinking>` tag.
</workflow_instructions>

- **Audit**: Confirm documentation meets governance standards.

## Step 3: Execution

<current_step>Step 3: Execution</current_step>
<workflow_instructions>
1. Stage files and commit with a structured message (`feat`, `fix`, `docs`, `refactor`, `meta`).
</workflow_instructions>

- **Commands**: `git add .` and `git commit -m "..."`.

## Step 4: Summary

<current_step>Step 4: Summary</current_step>
<workflow_instructions>
1. Confirm commit hash and scan results in Japanese.
</workflow_instructions>

- **Report**: Finalize the commit process.
