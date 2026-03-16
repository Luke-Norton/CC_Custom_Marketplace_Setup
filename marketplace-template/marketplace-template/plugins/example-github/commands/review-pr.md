---
name: review-pr
description: Perform comprehensive review of a GitHub pull request
argument-hint: <pr-url-or-number>
---

# Review Pull Request

Perform a comprehensive, AI-powered review of a GitHub pull request.

## Steps

### 1. Parse PR identifier

Accept either:
- Full URL: `https://github.com/owner/repo/pull/123`
- Just the number: `123`
- Short format: `owner/repo#123`

Extract:
- Owner
- Repository
- PR number

### 2. Fetch PR metadata

```bash
gh pr view <number> --json \
  title,body,author,createdAt,updatedAt,\
  commits,additions,deletions,changedFiles,\
  reviews,reviewDecision,\
  statusCheckRollup,labels
```

Display key information:
```
PR #123: Title of the PR
Author: @username
Created: 2 days ago
Status: ✓ 2 approvals, ✗ 1 change requested
Files changed: 12 (+234, -56)
CI Status: ✓ All checks passing
```

### 3. Fetch PR diff

```bash
gh pr diff <number>
```

For large PRs (>500 lines), consider:
- Reviewing file by file
- Focusing on specific file types
- Asking user which areas to prioritize

### 4. Analyze the code changes

Review for:

#### Code Quality
- [ ] Code follows project conventions
- [ ] Variable/function names are descriptive
- [ ] Code is readable and maintainable
- [ ] No unnecessary complexity
- [ ] DRY principle followed (no duplication)

#### Functionality
- [ ] Logic is correct and handles edge cases
- [ ] Error handling is appropriate
- [ ] Input validation where needed
- [ ] No obvious bugs

#### Security
- [ ] No hardcoded credentials or secrets
- [ ] Input sanitization for user data
- [ ] No SQL injection vulnerabilities
- [ ] No XSS vulnerabilities
- [ ] Proper authentication/authorization

#### Performance
- [ ] No obvious performance issues
- [ ] Efficient algorithms used
- [ ] Database queries optimized
- [ ] No memory leaks

#### Testing
- [ ] Tests are included
- [ ] Tests cover new functionality
- [ ] Tests cover edge cases
- [ ] Existing tests still pass

#### Documentation
- [ ] Code comments where needed
- [ ] README updated if needed
- [ ] API documentation updated
- [ ] Breaking changes documented

### 5. Check commit history

```bash
gh pr view <number> --json commits
```

Review commits for:
- Meaningful commit messages
- Logical commit grouping
- No merge commits (if squash merge is preferred)
- Conventional commit format if used

### 6. Check CI/CD status

```bash
gh pr checks <number>
```

Report:
- All checks passing or failing
- Which checks failed and why
- Link to check details

### 7. Generate structured review

Provide feedback in this format:

```markdown
## Review Summary

[Overall impression: LGTM, Approve with suggestions, Request changes]

## Strengths
- ✅ Well-structured code
- ✅ Comprehensive tests
- ✅ Clear documentation

## Issues Found

### 🔴 Critical (must fix)
1. **Security: Hardcoded API key** - `src/config.js:12`
   - Found: `const API_KEY = "sk-123..."`
   - Fix: Use environment variables
   ```javascript
   const API_KEY = process.env.API_KEY;
   ```

### 🟡 Important (should fix)
1. **Performance: N+1 query** - `src/services/user.js:45`
   - Issue: Loading relations in a loop
   - Suggestion: Use eager loading
   ```javascript
   const users = await User.findAll({ include: ['posts'] });
   ```

### 🔵 Suggestions (nice to have)
1. **Code style: Prefer const** - `src/utils.js:23`
   - Use `const` instead of `let` for values that don't change

## Detailed Review by File

### src/auth/login.js
**Line 34:** Consider adding rate limiting to prevent brute force attacks
**Line 56:** Missing error handling for database connection failures
**Line 78:** ✅ Good use of async/await

### src/models/user.js
**Line 12:** ✅ Proper input validation
**Line 45:** Consider adding an index on `email` column for faster lookups

### tests/auth.test.js
**Line 23:** ✅ Good test coverage
**Line 67:** Add test case for invalid token format

## Test Plan
- [x] Unit tests pass
- [ ] Suggest adding integration test for auth flow
- [ ] Consider adding performance test for bulk operations

## Overall Recommendation
[APPROVE / REQUEST CHANGES / COMMENT]

This PR [summary of the PR's quality and your recommendation]
```

### 8. Submit review (optional)

If user confirms, submit the review:

```bash
# For approval
gh pr review <number> --approve --body "..."

# For requesting changes
gh pr review <number> --request-changes --body "..."

# For comments only
gh pr review <number> --comment --body "..."
```

### 9. Provide next steps

```
✓ Review complete!

Suggested actions:
- Add inline comments: gh pr review <number> --comment
- Check for updates: gh pr view <number>
- Approve when ready: gh pr review <number> --approve
```

## Advanced Features

### Focus on specific aspects

User can request focused reviews:
- `--focus security` - Security review only
- `--focus performance` - Performance analysis
- `--focus tests` - Test coverage review
- `--focus style` - Code style review

### Compare with base branch

```bash
# Get stats of changes
git diff origin/main...HEAD --stat
git diff origin/main...HEAD --shortstat
```

### Check for common anti-patterns

Look for:
- TODO/FIXME comments being added
- Commented-out code
- Debug statements (console.log, debugger)
- Large functions (>50 lines)
- High cyclomatic complexity

## Error Handling

### PR not found
```
Error: Pull request #123 not found in owner/repo

Check:
1. PR number is correct
2. You have access to the repository
3. Try: gh pr list
```

### No access to repository
```
Error: You don't have access to this repository

Solutions:
1. Check you're authenticated: gh auth status
2. Request access from repository owner
3. Verify repository name is correct
```

### Diff too large
```
⚠️  This PR changes 2,500+ lines across 50 files

Would you like to:
1. Review specific files
2. Get a high-level summary
3. Review file by file interactively
```

## Example Review Output

```
## Review Summary
LGTM with minor suggestions! This is a solid implementation of user authentication.

## Strengths
- ✅ Comprehensive test coverage (95%)
- ✅ Proper error handling throughout
- ✅ Clear, well-structured code
- ✅ Good use of TypeScript types

## Issues Found

### 🟡 Important
1. **Security: Password validation** - `src/auth/register.ts:34`
   Consider adding stronger password requirements:
   - Minimum 12 characters (currently 8)
   - Require special characters
   - Check against common passwords list

### 🔵 Suggestions
1. **Code organization** - `src/auth/service.ts`
   Consider extracting JWT logic into separate module for reusability

2. **Documentation** - `README.md`
   Add example of authentication flow

## Overall Recommendation
**APPROVE** - Great work! The suggestions above are minor and can be addressed in a follow-up PR if needed.
```
