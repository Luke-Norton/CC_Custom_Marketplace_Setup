---
name: github-workflow
description: >-
  Use when working with GitHub pull requests, code reviews, issues, or repository workflows.
  Trigger phrases: "create a PR", "review pull request", "check GitHub issues",
  "update PR", "merge pull request", "create GitHub issue", "analyze PR diff".
---

# GitHub Workflow Best Practices

This skill provides comprehensive guidance for GitHub workflows using the `gh` CLI and Git.

## When to use

- Creating or updating pull requests
- Reviewing code changes and PRs
- Managing GitHub issues
- Working with GitHub Actions
- Checking repository status
- Analyzing PR diffs and commits

## When NOT to use

- GitLab or Bitbucket workflows (different CLI tools)
- Manual Git operations without GitHub integration
- Local-only Git operations that don't involve GitHub

## Core Principles

### 1. Always verify prerequisites
Before any GitHub operation:
```bash
# Check gh CLI is installed and authenticated
gh auth status

# Verify we're in a git repository
git rev-parse --git-dir

# Check for remote repository
git remote -v
```

### 2. Provide clear user feedback
- Show what you're doing at each step
- Display success/failure clearly
- Provide actionable error messages

### 3. Use the gh CLI, not web scraping
Always use `gh` commands for GitHub operations:
```bash
# ✅ Good
gh pr view 123

# ❌ Bad
curl https://api.github.com/repos/...
```

## Pull Request Workflow

### Creating a PR

1. **Check for uncommitted changes**
```bash
git status
```

2. **Review commit history from base branch**
```bash
git log origin/main..HEAD --oneline
git diff origin/main...HEAD
```

3. **Generate meaningful title and description**
- Title: Short summary (< 70 chars) of the change
- Body: Include ## Summary, ## Changes, ## Test Plan

4. **Create the PR**
```bash
gh pr create --title "..." --body "$(cat <<'EOF'
## Summary
- Key change 1
- Key change 2

## Changes
Detailed description of what changed and why

## Test Plan
- [ ] Unit tests pass
- [ ] Manual testing completed
- [ ] Documentation updated
EOF
)"
```

### Reviewing a PR

1. **Fetch PR details**
```bash
gh pr view <number> --json title,body,author,commits,reviews,statusCheckRollup
```

2. **Get the diff**
```bash
gh pr diff <number>
```

3. **Analyze the changes**
- Check code quality
- Look for security issues
- Verify tests are included
- Check documentation updates
- Review commit messages

4. **Provide structured feedback**
Use categories:
- **Critical**: Must fix before merge
- **Important**: Should fix
- **Suggestion**: Nice to have
- **Question**: Needs clarification

### Merging a PR

1. **Check PR status**
```bash
gh pr checks <number>
```

2. **Verify approvals**
```bash
gh pr view <number> --json reviewDecision
```

3. **Merge with appropriate strategy**
```bash
# Squash for feature branches
gh pr merge <number> --squash

# Merge commit for release branches
gh pr merge <number> --merge

# Rebase for clean history
gh pr merge <number> --rebase
```

## Issue Management

### Creating an issue

```bash
gh issue create --title "..." --body "$(cat <<'EOF'
## Problem
Description of the issue

## Expected Behavior
What should happen

## Actual Behavior
What currently happens

## Steps to Reproduce
1. Step one
2. Step two

## Environment
- OS: ...
- Version: ...
EOF
)"
```

### Linking issues to PRs

```bash
# In PR description
Closes #123
Fixes #456
Resolves #789
```

## Common Patterns

### Pattern: Safe branch switching

```bash
# Check for uncommitted changes
if ! git diff-index --quiet HEAD --; then
  echo "Warning: You have uncommitted changes"
  # Ask user what to do
fi

# Switch branch
git checkout branch-name
```

### Pattern: Update PR from feedback

```bash
# Make changes based on review
# ... edit files ...

# Commit with --fixup
git commit --fixup=<original-commit-sha>

# Auto-squash when updating PR
git rebase -i --autosquash origin/main
git push --force-with-lease
```

### Pattern: Check CI status before merge

```bash
# Get CI status
gh pr checks <number>

# Wait for pending checks
gh pr checks <number> --watch

# Only proceed if all checks pass
```

## Error Handling

### Common errors and solutions

**Error: "gh: not found"**
```
Solution: Install GitHub CLI
- macOS: brew install gh
- Linux: Follow https://cli.github.com/
- Windows: winget install GitHub.cli
```

**Error: "authentication required"**
```
Solution: Authenticate with GitHub
gh auth login
```

**Error: "no pull request found"**
```
Solution: Verify PR number/URL is correct
gh pr list
```

**Error: "refusing to merge"**
```
Solution: Check PR status and approvals
gh pr view <number> --json reviewDecision,statusCheckRollup
```

## Quick Reference

| Task | Command |
|------|---------|
| Create PR | `gh pr create --title "..." --body "..."` |
| View PR | `gh pr view <number>` |
| Review PR | `gh pr review <number> --approve` |
| Get PR diff | `gh pr diff <number>` |
| Check CI status | `gh pr checks <number>` |
| Merge PR | `gh pr merge <number> --squash` |
| Create issue | `gh issue create --title "..." --body "..."` |
| List issues | `gh issue list` |
| View issue | `gh issue view <number>` |
| Close issue | `gh issue close <number>` |
| List PRs | `gh pr list` |
| List my PRs | `gh pr list --author @me` |

## Examples

### Example 1: Complete PR creation flow

```bash
# 1. Check status
git status

# 2. Review commits
git log origin/main..HEAD

# 3. Get diff stats
git diff origin/main...HEAD --stat

# 4. Create PR
gh pr create --title "Add user authentication" --body "$(cat <<'EOF'
## Summary
- Implement JWT-based authentication
- Add login/logout endpoints
- Update user model

## Test Plan
- [x] Unit tests for auth service
- [x] Integration tests for endpoints
- [x] Manual testing with Postman
EOF
)"
```

### Example 2: Comprehensive PR review

```bash
# 1. Get PR info
gh pr view 123 --json title,author,body

# 2. Check files changed
gh pr diff 123 --name-only

# 3. Get full diff
gh pr diff 123

# 4. Check CI
gh pr checks 123

# 5. Provide review
gh pr review 123 --comment --body "LGTM! Just one suggestion: consider adding error handling in line 42"
```

### Example 3: Issue creation from PR discussion

```bash
# Create follow-up issue
gh issue create --title "Refactor authentication module" --body "$(cat <<'EOF'
## Context
During PR #123 review, we identified that the authentication module could be refactored.

## Proposal
- Extract auth logic into separate service
- Add caching for token validation
- Improve error messages

Related to: #123
EOF
)"
```

## Tips for Success

1. **Always push to remote before creating PR**
   ```bash
   git push -u origin branch-name
   gh pr create
   ```

2. **Use draft PRs for work in progress**
   ```bash
   gh pr create --draft
   ```

3. **Add labels for better organization**
   ```bash
   gh pr create --label "enhancement,high-priority"
   ```

4. **Request specific reviewers**
   ```bash
   gh pr create --reviewer username1,username2
   ```

5. **Keep PR descriptions updated**
   ```bash
   gh pr edit <number> --add-label "ready-for-review"
   ```
