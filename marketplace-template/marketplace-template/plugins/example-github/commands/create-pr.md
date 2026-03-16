---
name: create-pr
description: Create a GitHub pull request from the current branch
argument-hint: [base-branch]
---

# Create Pull Request

Create a well-formatted GitHub pull request from the current branch.

## Steps

### 1. Verify prerequisites

```bash
# Check we're in a git repository
git rev-parse --git-dir

# Check gh CLI is authenticated
gh auth status

# Get current branch
CURRENT_BRANCH=$(git branch --show-current)
echo "Current branch: $CURRENT_BRANCH"
```

If on main/master branch, warn the user:
```
⚠️  You are on the main branch. Create a feature branch first:
git checkout -b feature/your-feature-name
```

### 2. Check for uncommitted changes

```bash
# Check for staged changes
git diff --cached --stat

# Check for unstaged changes
git diff --stat

# Check for untracked files
git ls-files --others --exclude-standard
```

If there are uncommitted changes, ask the user:
- Commit them now
- Stash them
- Continue anyway

### 3. Check remote status

```bash
# Check if branch has upstream
git rev-parse --abbrev-ref --symbolic-full-name @{u} 2>/dev/null

# If no upstream, need to push first
git push -u origin $CURRENT_BRANCH
```

### 4. Analyze changes for PR content

```bash
# Get base branch (default to main, or use argument)
BASE_BRANCH="${1:-main}"

# Get commit history
git log origin/$BASE_BRANCH..HEAD --oneline

# Get diff statistics
git diff origin/$BASE_BRANCH...HEAD --stat

# Get full diff for analysis (first 200 lines)
git diff origin/$BASE_BRANCH...HEAD | head -200
```

### 5. Generate PR title

Based on the commits and changes:
- Use conventional commit format if applicable (feat:, fix:, docs:, etc.)
- Keep under 70 characters
- Be descriptive but concise
- Focus on the "what" not the "how"

Examples:
- "Add user authentication with JWT"
- "Fix memory leak in data processing"
- "Update documentation for API endpoints"

### 6. Generate PR description

Create a structured description:

```markdown
## Summary
- Bullet point 1 (key change)
- Bullet point 2 (key change)
- Bullet point 3 (key change)

## Motivation
Why this change is needed and what problem it solves.

## Changes
Detailed description of what changed:
- Added X
- Modified Y
- Removed Z

## Test Plan
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing completed
- [ ] Documentation updated
- [ ] No breaking changes (or migration guide provided)

## Screenshots (if applicable)
[Add screenshots for UI changes]

## Related Issues
Closes #123
Related to #456
```

### 7. Create the PR

```bash
gh pr create \
  --title "Your PR Title" \
  --body "$(cat <<'EOF'
## Summary
...

## Motivation
...

## Changes
...

## Test Plan
...
EOF
)" \
  --base "$BASE_BRANCH"
```

### 8. Display result

```bash
# Get the created PR URL
PR_URL=$(gh pr view --json url --jq '.url')

echo "✓ Pull request created successfully!"
echo ""
echo "PR URL: $PR_URL"
echo ""
echo "Next steps:"
echo "  - Request reviewers: gh pr edit --add-reviewer username"
echo "  - Add labels: gh pr edit --add-label enhancement"
echo "  - Check CI status: gh pr checks"
```

## Advanced Options

### Add draft PR
```bash
gh pr create --draft --title "..." --body "..."
```

### Add reviewers immediately
```bash
gh pr create --reviewer username1,username2 --title "..." --body "..."
```

### Add labels
```bash
gh pr create --label "enhancement,high-priority" --title "..." --body "..."
```

### Specify different base branch
```bash
/github:create-pr develop
```

## Error Handling

### Error: No changes to create PR

```
There are no commits on this branch compared to main.
Make some changes first:
1. Edit files
2. git add <files>
3. git commit -m "Your changes"
4. Then try again
```

### Error: Push rejected

```
Your branch is behind the remote. Pull first:
git pull origin $CURRENT_BRANCH --rebase
```

### Error: PR already exists

```
A pull request already exists for this branch: <url>
Would you like to:
1. Update the existing PR
2. Close it and create a new one
3. View the existing PR
```

## Best Practices Applied

1. ✅ Check all prerequisites before starting
2. ✅ Provide clear status updates
3. ✅ Generate meaningful PR content
4. ✅ Follow conventional commit format
5. ✅ Include test plan by default
6. ✅ Display actionable next steps
