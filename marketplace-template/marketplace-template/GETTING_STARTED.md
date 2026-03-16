# Getting Started with Your Custom Marketplace

This guide will walk you through setting up your first custom Claude Code marketplace and creating your first plugin.

## 📋 Prerequisites

Before you begin, make sure you have:

- Claude Code installed and configured
- Git installed and configured
- Basic understanding of:
  - Markdown formatting
  - YAML frontmatter
  - Command-line tools (optional, depending on your plugin)

## 🎯 Part 1: Set Up Your Marketplace

### Step 1: Fork or Clone This Repository

```bash
# Option A: Clone directly
git clone https://github.com/your-username/your-marketplace
cd your-marketplace/marketplace-template/marketplace-template

# Option B: Use as template on GitHub
# Click "Use this template" button on GitHub
```

### Step 2: Customize Marketplace Metadata

Edit `.claude-plugin/marketplace.json`:

```json
{
  "name": "my-company-marketplace",
  "version": "1.0.0",
  "description": "Claude Code plugins for My Company workflows",
  "author": "My Company",
  "repository": "https://github.com/my-company/claude-marketplace",
  "plugins": []
}
```

### Step 3: Update README

Edit `README.md` and replace:
- "Your Marketplace Name" → Your actual marketplace name
- "your-username/your-marketplace" → Your GitHub repository path
- Add your company/team specific information

### Step 4: Test Installation

```bash
# Add your marketplace locally
claude plugin marketplace add file://$(pwd)

# Verify it's added
claude plugin marketplace list
```

You should see your marketplace listed!

## 🚀 Part 2: Create Your First Plugin

Let's create a simple "code-review" plugin that teaches Claude your team's code review standards.

### Step 1: Choose and Copy Template

```bash
# Copy the skill-only template
cp -r plugins/template-skill-only plugins/code-review
cd plugins/code-review
```

### Step 2: Create plugin.json

Create `.claude-plugin/plugin.json`:

```json
{
  "name": "code-review",
  "version": "0.1.0",
  "description": "Code review guidelines and best practices for our team",
  "author": "Your Name",
  "license": "MIT",
  "skills": [
    {
      "name": "code-review-guidelines",
      "path": "skills/code-review-guidelines/SKILL.md"
    }
  ]
}
```

### Step 3: Create the Skill

Rename and edit the skill directory:

```bash
mv skills/your-skill skills/code-review-guidelines
```

Edit `skills/code-review-guidelines/SKILL.md`:

```yaml
---
name: code-review-guidelines
description: >-
  Use when reviewing code, analyzing pull requests, or providing code feedback.
  Trigger phrases: "review this code", "check my changes", "code review",
  "what do you think about this code", "review PR".
---

# Code Review Guidelines

Apply our team's code review standards when analyzing code.

## When to use

- Reviewing pull requests
- Analyzing code changes
- Providing code feedback
- Checking code quality

## When NOT to use

- Writing new code (use language-specific skills)
- Debugging runtime errors (use debugging skills)
- Performance profiling (use performance skills)

## Code Review Checklist

### 1. Code Quality

#### Readability
- [ ] Variable and function names are descriptive
- [ ] Code is well-organized and follows logical structure
- [ ] Complex logic has explanatory comments
- [ ] No magic numbers (use named constants)

#### Maintainability
- [ ] Functions are focused and single-purpose (< 50 lines)
- [ ] No code duplication (DRY principle)
- [ ] Error handling is appropriate
- [ ] No overly complex conditionals (cyclomatic complexity)

### 2. Security

- [ ] No hardcoded secrets or credentials
- [ ] Input validation for user-provided data
- [ ] SQL queries use parameterized statements
- [ ] No eval() or similar dangerous functions
- [ ] Proper authentication and authorization checks

### 3. Testing

- [ ] Unit tests are included for new functionality
- [ ] Tests cover edge cases and error conditions
- [ ] Test names clearly describe what they test
- [ ] Existing tests still pass

### 4. Documentation

- [ ] README updated if needed
- [ ] API documentation for new public methods
- [ ] Complex algorithms have explanatory comments
- [ ] Breaking changes are documented

### 5. Team Standards

Apply our specific standards:
- Use TypeScript strict mode
- Follow ESLint rules
- Maximum file size: 300 lines
- Use async/await instead of .then()
- Prefer functional over imperative style

## Review Process

When reviewing code, follow these steps:

### 1. Understand the Context

```bash
# Get PR details
gh pr view <number>

# Review the diff
gh pr diff <number>
```

### 2. Check High-Level Design

- Does the approach make sense?
- Are there simpler alternatives?
- Does it fit our architecture?

### 3. Review Implementation Details

Go through each file:
- Logic correctness
- Error handling
- Edge cases
- Code quality

### 4. Provide Structured Feedback

Use this format:

**Critical Issues (Must Fix)**
- Issues that could cause bugs or security problems

**Suggestions (Should Consider)**
- Improvements to code quality or maintainability

**Nitpicks (Optional)**
- Minor style or convention improvements

**Praise**
- What was done well (always include!)

## Common Issues to Watch For

### Issue: Large Functions

```javascript
// ❌ Too large and complex
function processUser(user) {
  // 100+ lines of logic
}

// ✅ Split into smaller functions
function processUser(user) {
  validateUser(user);
  enrichUserData(user);
  saveUser(user);
}
```

### Issue: Missing Error Handling

```javascript
// ❌ No error handling
const data = await fetchData(url);

// ✅ Proper error handling
try {
  const data = await fetchData(url);
} catch (error) {
  logger.error('Failed to fetch data:', error);
  throw new APIError('Data fetch failed');
}
```

### Issue: Hardcoded Values

```javascript
// ❌ Magic numbers
if (status === 3) { ... }

// ✅ Named constants
const Status = { ACTIVE: 3, INACTIVE: 4 };
if (status === Status.ACTIVE) { ... }
```

## Example Review

### Good Review Comment

```markdown
**Performance: N+1 Query** - `src/services/posts.js:45`

Issue: Loading comments in a loop causes multiple database queries.

Impact: This will be slow with many posts (>100).

Solution:
```javascript
// Instead of:
for (const post of posts) {
  post.comments = await Comment.find({ postId: post.id });
}

// Use eager loading:
const posts = await Post.findAll({
  include: [{ model: Comment }]
});
```

This reduces N+1 queries to a single query with JOIN.
```

## Quick Reference

| Check | Command/Pattern |
|-------|----------------|
| View PR | `gh pr view <number>` |
| Get diff | `gh pr diff <number>` |
| Check tests | `npm test` |
| Lint code | `npm run lint` |
| Type check | `npm run type-check` |

## Tips

1. **Be constructive**: Explain why, not just what
2. **Provide examples**: Show better alternatives
3. **Praise good code**: Recognition motivates
4. **Focus on impact**: Prioritize critical issues
5. **Ask questions**: Understand before criticizing
```

Save this file.

### Step 4: Update Plugin README

Edit `README.md`:

```markdown
# Code Review Plugin

Code review guidelines and best practices for our team.

## Installation

```bash
claude plugin install code-review@my-company-marketplace
```

## Usage

This skill automatically activates when you:
- Say "review this code"
- Ask to "check my changes"
- Mention "code review"
- Request feedback on code

## What It Does

The plugin teaches Claude to review code according to our team standards:
- Code quality and readability checks
- Security vulnerability detection
- Testing coverage verification
- Documentation requirements
- Team-specific coding standards

## Example

```
You: "Can you review the changes in this PR?"

Claude: [code-review-guidelines skill activates]
"I'll review this PR according to our team standards. Let me analyze the changes..."

[Provides structured review with:
- Critical issues (security, bugs)
- Suggestions (code quality)
- Nitpicks (style)
- Praise (what's done well)]
```

## Customization

Edit `skills/code-review-guidelines/SKILL.md` to:
- Add your team's specific standards
- Include your preferred coding patterns
- Add language-specific checks
- Customize the review format
```

### Step 5: Register Plugin in Marketplace

Edit `.claude-plugin/marketplace.json` and add your plugin:

```json
{
  "name": "my-company-marketplace",
  "version": "1.0.0",
  "description": "Claude Code plugins for My Company workflows",
  "author": "My Company",
  "repository": "https://github.com/my-company/claude-marketplace",
  "plugins": [
    {
      "name": "code-review",
      "version": "0.1.0",
      "source": "./plugins/code-review",
      "description": "Code review guidelines and best practices for our team"
    }
  ]
}
```

### Step 6: Test Your Plugin

```bash
# Go back to marketplace root
cd ../..

# Update marketplace
claude plugin marketplace update my-company-marketplace

# Install your plugin
claude plugin install code-review@my-company-marketplace

# Test it
# In Claude Code, try: "Can you review this code?"
```

### Step 7: Commit and Push

```bash
git add .
git commit -m "feat(plugin): add code-review plugin"
git push origin main
```

## 🎓 Part 3: Advanced - Add a Command

Let's enhance our plugin with a command for quick code reviews.

### Step 1: Update Plugin Template

Copy the command-skill template:

```bash
# Copy command template
cp plugins/template-command-skill/commands/your-command.md plugins/code-review/commands/quick-review.md
```

### Step 2: Create the Command

Edit `plugins/code-review/commands/quick-review.md`:

```yaml
---
name: quick-review
description: Quick code quality check on current changes
argument-hint: [file-path]
---

# Quick Review

Perform a rapid code quality check on uncommitted changes or a specific file.

## Steps

### 1. Determine what to review

If file path provided:
```bash
# Review specific file
git diff <file-path>
```

If no argument:
```bash
# Review all uncommitted changes
git diff
```

### 2. Run quick checks

Check for common issues:

**Security**
```bash
# Check for potential secrets
grep -r "api[_-]key\|password\|secret" <files> || echo "No obvious secrets found"
```

**Code Quality**
```bash
# Check file sizes
find <files> -type f -exec wc -l {} \; | awk '$1 > 300 {print "⚠️  "$2" is "$1" lines (>300)"}'
```

**Testing**
```bash
# Check if test files exist for changed files
# Logic to check for corresponding test files
```

### 3. Provide Summary

Display results in this format:

```
Quick Review Results
====================

Files reviewed: 3
Lines changed: +142, -38

✓ No hardcoded secrets detected
✓ File sizes are reasonable
⚠️  Missing tests for: src/new-feature.js

Recommendations:
1. Add unit tests for new-feature.js
2. Consider extracting large function in utils.js (150 lines)

Run full review: /code-review:full-review
```

## Error Handling

### No changes to review
```
No uncommitted changes found.

Try:
- Make some changes first
- Specify a file: /code-review:quick-review src/file.js
- Review a PR instead: /github:review-pr <url>
```
```

### Step 3: Update plugin.json

Edit `.claude-plugin/plugin.json`:

```json
{
  "name": "code-review",
  "version": "0.2.0",
  "description": "Code review guidelines and best practices for our team",
  "author": "Your Name",
  "license": "MIT",
  "commands": [
    {
      "name": "quick-review",
      "path": "commands/quick-review.md"
    }
  ],
  "skills": [
    {
      "name": "code-review-guidelines",
      "path": "skills/code-review-guidelines/SKILL.md"
    }
  ]
}
```

### Step 4: Update marketplace version

Edit `.claude-plugin/marketplace.json`:

```json
{
  "plugins": [
    {
      "name": "code-review",
      "version": "0.2.0",
      "source": "./plugins/code-review",
      "description": "Code review guidelines and best practices for our team"
    }
  ]
}
```

### Step 5: Test the command

```bash
# Update plugin
claude plugin update code-review

# Test command
/code-review:quick-review
```

## 📚 Part 4: Publishing Your Marketplace

### Option 1: GitHub (Recommended)

1. **Push to GitHub**:
```bash
git push origin main
```

2. **Users install with**:
```bash
claude plugin marketplace add your-username/your-repo
```

### Option 2: Self-Hosted

1. **Host on web server**:
```bash
# Upload marketplace directory to server
scp -r marketplace-template/* user@server:/var/www/marketplace/
```

2. **Users install with**:
```bash
claude plugin marketplace add https://your-domain.com/marketplace
```

## 🎯 Next Steps

### Create More Plugins

Now that you have your first plugin, create more:

1. **Deployment Plugin**: Automate your deployment process
2. **Testing Plugin**: Testing best practices and automation
3. **Documentation Plugin**: Documentation standards and generation

### Enhance Existing Plugins

- Add more commands
- Create specialized agents
- Add hooks for automation
- Integrate MCP servers

### Share with Team

- Document your marketplace
- Create usage guides
- Collect feedback
- Iterate and improve

## 💡 Ideas for Plugins

### By Domain

- **DevOps**: deployment, monitoring, incident response
- **Testing**: test generation, coverage analysis, QA automation
- **Documentation**: doc generation, API docs, changelog
- **Security**: security scanning, vulnerability checks, compliance
- **Code Quality**: linting, formatting, code review

### By Tool

- **GitHub**: PR workflows, issue management
- **Jira**: ticket creation, status updates
- **Slack**: notifications, team updates
- **Kubernetes**: deployment, monitoring
- **AWS/GCP/Azure**: cloud operations

### By Workflow

- **Onboarding**: new developer setup
- **Release**: release process automation
- **Hotfix**: emergency fix workflow
- **Code Review**: review standards and automation

## 🆘 Troubleshooting

### Plugin not activating

1. Check plugin is installed:
```bash
claude plugin list
```

2. Verify skill trigger phrases match what you're saying

3. Try explicit trigger:
```
"Use the code-review-guidelines skill to review this"
```

### Command not found

1. Check command is in plugin.json
2. Verify file path is correct
3. Update plugin:
```bash
claude plugin update code-review
```

### Changes not taking effect

1. Update marketplace:
```bash
claude plugin marketplace update my-company-marketplace
```

2. Update plugin:
```bash
claude plugin update code-review
```

3. Restart Claude Code if needed

## 📖 Additional Resources

- [README.md](./README.md) - Marketplace documentation
- [CONTRIBUTING.md](./CONTRIBUTING.md) - Detailed contribution guide
- [example-github](./plugins/example-github/) - Production-quality example
- [Claude Code Docs](https://docs.anthropic.com/claude-code) - Official documentation

## 🎉 Success!

You now have:
- ✅ A custom marketplace
- ✅ Your first plugin
- ✅ Command added to plugin
- ✅ Published for team use

Keep building and improving your plugins based on team feedback!

---

**Questions?** Check the [CONTRIBUTING.md](./CONTRIBUTING.md) for more details or open an issue.
