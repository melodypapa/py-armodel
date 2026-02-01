# GitHub Workflow Automation

Automate the complete GitHub workflow for creating issues, feature branches, commits, and pull requests.

## Workflow Steps

When the user runs `/gh-workflow`, perform the following steps in order:

### 1. Quality Checks (Must Pass Before Proceeding)
- Run linting with flake8: `flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics`
- Run tests with pytest: `pytest`
- Install package: `pip install -e .`
- **All checks must pass** before proceeding to next step
- If any checks fail, report errors and ask user if they want to:
  - Abort the workflow
  - Fix issues and retry
  - Continue anyway (not recommended)
- Display quality gate summary table:
  ```
  Check        Status    Details
  ───────────────────────────────────
  Flake8       ✅ Pass    No E9,F63,F7,F82 errors
  Pytest       ✅ Pass    All tests passed
  ```

### 2. Analyze Current Changes
- Run `git status` to see modified files
- Run `git diff` to review unstaged changes
- Ask the user for a brief summary of the changes if not clear from the diff

### 3. Create GitHub Issue
- Create a GitHub issue using `gh issue create`
- Title format: `"<type>: <brief description>"` (type can be: feat, fix, docs, refactor, test, chore)
- Include sections: Summary, Changes, Files Modified, Test Coverage, Requirements (if applicable)
- Capture the issue number (e.g., #20)

### 4. Create Feature Branch
- Create and checkout a new feature branch
- Branch naming convention: `feature/<requirement-id>-short-description` or `feature/<type>-short-description`
- Example: `feature/swr-writer-00006-class-file-structure` or `feature/add-new-parser`

### 5. Stage and Commit Changes
- Stage all relevant modified files
- Create a commit with:
  - Conventional commit format: `<type>: <description>`
  - Detailed commit body describing changes
  - Reference to the issue (e.g., `Closes #20`)
  - **Important**: Do NOT add Claude as co-author (no `Co-Authored-By` line)

### 6. Push to GitHub Only
- Push the branch to GitHub remote (origin)
- **Important**: Do NOT push to gitee remote
- Use explicit GitHub URL if needed: `git push git@github.com:melodypapa/autosar-pdf.git`

### 7. Create Pull Request
- Create a pull request using `gh pr create`
- Include comprehensive PR description with:
  - Summary section
  - Changes section
  - Files Modified list
  - Test Coverage information
  - Requirements traceability (if applicable)
  - Reference to the issue being closed
- Use `--head` flag if branch tracking is not properly set up

## Commit Types

Use these conventional commit types:
- `feature`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

## Arguments

Use `$ARGUMENTS` to accept optional context:
- Issue title/description
- Branch name (if different from auto-generated)
- Specific files to include/exclude
- Commit type override

## Example Usage

```
/gh-workflow
/gh-workflow Implement new parser for AUTOSAR models
/gh-workflow feat: Add support for base class extraction
```

## Notes

- Always confirm with the user before executing destructive operations
- Show progress updates at each step
- Report any errors and ask for guidance
- Provide links to the created issue and pull request
- Update the todo list to track progress
