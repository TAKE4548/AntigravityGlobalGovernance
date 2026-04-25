---
name: commit
description: "Cross-repository commit workflow with security guardrails. Command: /commit"
---

# Commit Workflow (/commit)

Use this workflow to safely commit changes after a security audit.

## Step 1: Security Audit
- **Action**: Run the pre-commit linter to check for absolute paths and secrets.
- **Command**: `python ${GLOBAL_SCRIPTS}\pre_commit_linter.py .`
- **Error Handling**: If the command fails (exit code 1), STOP and report the specific file and line to the user. DO NOT proceed to commit.

## Step 2: Verification
- **Audit Table**: Ensure the `walkthrough.md` contains the AC compliance table as per `GEMINI.md`.

## Step 3: Execution
- **Action**: Stage files and commit with a structured message.
- **Commands**:
    - `git add .`
    - `git commit -m "<type>(<scope>): <subject>"`
- **Message Convention**:
    - `feat`: New feature
    - `fix`: Bug fix
    - `docs`: Documentation only changes
    - `refactor`: Code change that neither fixes a bug nor adds a feature
    - `meta`: Agent governance or workflow changes

## Step 4: Summary
- **Report**: Confirm the commit hash and the result of the security scan.
