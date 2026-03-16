# Contributing to the Marketplace

Thank you for contributing! This guide will help you create high-quality plugins for this marketplace.

## 🚀 Quick Start

### Option 1: From Template (Recommended)

1. **Choose a template** based on your needs (see table below)
2. **Copy the template**:
   ```bash
   cp -r plugins/template-skill-only plugins/my-plugin
   cd plugins/my-plugin
   ```
3. **Customize the plugin** (see detailed steps below)
4. **Register in marketplace** (see registration section)
5. **Test locally** (see testing section)
6. **Open a pull request**

### Option 2: From Example

Study the `example-github` plugin as a reference for a production-ready implementation.

## 🎯 Choose Your Template

| Template | Use When | Components | Complexity |
|----------|----------|------------|------------|
| **template-skill-only** | Teaching Claude domain knowledge only | Skill | ⭐ Simple |
| **template-command-skill** | Need slash commands with context | Command + Skill | ⭐⭐ Medium |
| **template-agent** | Need specialized subagent | Agent + Command + Skill | ⭐⭐⭐ Advanced |
| **template-full** | Need all features | Agent + Skill + Command + Hook + MCP | ⭐⭐⭐⭐ Expert |

### Decision Tree

```
Do you need to execute external commands?
├─ No → Start with template-skill-only
└─ Yes
   └─ Do you need a specialized subagent for complex workflows?
      ├─ No → Use template-command-skill
      └─ Yes
         └─ Do you need hooks or MCP integration?
            ├─ No → Use template-agent
            └─ Yes → Use template-full
```

## 📝 Step-by-Step Plugin Creation

### Step 1: Set Up Plugin Structure

```bash
# Copy template
cp -r plugins/template-skill-only plugins/my-plugin
cd plugins/my-plugin

# Create plugin.json
cat > .claude-plugin/plugin.json <<EOF
{
  "name": "my-plugin",
  "version": "0.1.0",
  "description": "Brief description of what your plugin does",
  "author": "Your Name",
  "license": "MIT",
  "skills": [
    {
      "name": "my-skill",
      "path": "skills/my-skill/SKILL.md"
    }
  ]
}
EOF
```

### Step 2: Create Your Skill

Edit `skills/my-skill/SKILL.md`:

```yaml
---
name: my-skill
description: >-
  Clear description of when this skill should activate.
  Include trigger phrases: "do X", "help with Y", "run Z workflow".
---

# Your Skill Name

Brief overview of what this skill teaches Claude.

## When to use

- Specific situation 1
- Specific situation 2
- Specific situation 3

## When NOT to use

- Out-of-scope situation 1
- Similar but different use case

## Guidelines

### Core Principles

1. **Principle 1**: Explanation and why it matters
2. **Principle 2**: Explanation and why it matters

### Step-by-Step Process

When [situation], follow these steps:

1. **Step 1**: Do this
   ```bash
   # Example command
   command --flag argument
   ```

2. **Step 2**: Then do this
   - Sub-step A
   - Sub-step B

### Common Patterns

#### Pattern 1: [Pattern Name]

Description of the pattern:
```
# Code example
```

## Quick Reference

| Task | How |
|------|-----|
| Task 1 | `command for task 1` |
| Task 2 | `command for task 2` |

## Examples

### Example 1: [Use Case]

```bash
# Step 1
command1

# Step 2
command2
```

Expected output:
```
Success message
```
```

### Step 3: Create Commands (if needed)

Edit `commands/my-command.md`:

```yaml
---
name: my-command
description: What this command does
argument-hint: [optional-arg]
---

# Command Name

What happens when `/my-plugin:my-command` is invoked.

## Steps

### 1. Validate prerequisites

Check that required tools/files exist:
```bash
# Check tool is available
command --version
```

### 2. Perform main action

```bash
# Main command
command --do-something
```

### 3. Display result

Show clear success/failure message:
```
✓ Operation completed successfully!

Next steps:
  - Do this next
  - Or try this
```

## Error Handling

### Error: [Common Error]
```
Solution: [How to fix]
```
```

### Step 4: Create Agent (if needed)

Edit `agents/my-agent.md`:

```yaml
---
name: my-agent
description: When this agent should be spawned
model: inherit
tools: Bash, Read, Write, Edit, Grep
permissionMode: acceptEdits
---

# Agent Name

Your role and expertise.

## Responsibilities

- Primary responsibility 1
- Primary responsibility 2

## Rules

### Always Do
- ✅ Rule 1
- ✅ Rule 2

### Never Do
- ❌ Anti-pattern 1
- ❌ Anti-pattern 2

## Process

1. **Gather context**: How to start
2. **Analyze**: What to look for
3. **Take action**: What to do
4. **Report**: How to communicate results
```

### Step 5: Update Plugin README

Edit `README.md` with:
- Installation instructions
- Prerequisites
- Usage examples
- Troubleshooting

### Step 6: Register in Marketplace

Add to `.claude-plugin/marketplace.json`:

```json
{
  "plugins": [
    {
      "name": "my-plugin",
      "version": "0.1.0",
      "source": "./plugins/my-plugin",
      "description": "Brief description of what your plugin does"
    }
  ]
}
```

### Step 7: Add Permissions (if needed)

If your plugin needs specific permissions, add to `base_settings.json`:

```json
{
  "permissions": {
    "allow": [
      "Bash(my-tool:*)",
      "Skill(my-plugin:*)",
      "Agent(my-agent)"
    ]
  }
}
```

## 🧪 Testing Your Plugin

### Test Locally

```bash
# From marketplace root
cd ../..

# Add marketplace locally
claude plugin marketplace add file://$(pwd)

# Install your plugin
claude plugin install my-plugin@local

# Test it works
/my-plugin:command-name
```

### Test Checklist

- [ ] Plugin installs without errors
- [ ] Commands invoke successfully
- [ ] Skills activate on trigger phrases
- [ ] Agents spawn when appropriate
- [ ] Permissions are correctly configured
- [ ] README is clear and complete
- [ ] Examples in README work as described

### Common Issues

**Issue: Skill not activating**
- Check trigger phrases are clear
- Verify skill is listed in plugin.json
- Test with explicit trigger phrases

**Issue: Command not found**
- Check command is listed in plugin.json
- Verify file path is correct
- Check command name matches file

**Issue: Permission denied**
- Add required permissions to base_settings.json
- Use correct permission format: `Tool(scope:*)`

## 📋 Plugin Structure Reference

```
plugins/your-plugin-name/
├── .claude-plugin/
│   └── plugin.json           # Required: Plugin metadata
├── skills/                   # Optional: Domain knowledge
│   └── skill-name/
│       └── SKILL.md
├── commands/                 # Optional: Slash commands
│   └── command-name.md
├── agents/                   # Optional: Specialized subagents
│   └── agent-name.md
├── hooks/                    # Optional: Event handlers
│   ├── pre-tool.py          # Before tool execution
│   ├── post-tool.py         # After tool execution
│   └── user-prompt.py       # Before user prompt
├── .mcp.json                 # Optional: MCP server config
└── README.md                 # Required: Documentation
```

## 📦 Versioning Guidelines

Follow [Semantic Versioning](https://semver.org/):

### PATCH (0.1.0 → 0.1.1)
- Bug fixes
- Typo corrections
- Documentation updates
- No API changes

### MINOR (0.1.0 → 0.2.0)
- New skills
- New commands
- New features
- Backward-compatible changes

### MAJOR (0.1.0 → 1.0.0)
- Breaking changes
- Removed commands/skills
- Changed command signatures
- Incompatible updates

**Important**: Update version in BOTH:
1. `.claude-plugin/plugin.json`
2. `.claude-plugin/marketplace.json`

## 🎨 Naming Conventions

### Plugin Names
- ✅ `github-workflow` (lowercase, hyphenated)
- ✅ `aws-s3-backup` (descriptive, clear)
- ❌ `GitHubWorkflow` (no PascalCase)
- ❌ `gh` (too abbreviated)

### Skill Names
- ✅ `code-review` (action-oriented)
- ✅ `deployment-process` (clear purpose)
- ❌ `skill1` (not descriptive)

### Command Names
- ✅ `create-pr` (verb-object)
- ✅ `deploy-production` (clear action)
- ❌ `pr` (too brief)

### Agent Names
- ✅ `pr-reviewer` (role-based)
- ✅ `test-generator` (purpose-based)
- ❌ `agent` (not specific)

## 📚 Best Practices

### Skill Design

1. **Clear Triggers**: Include specific trigger phrases in description
   ```yaml
   description: >-
     Use when "creating a pull request", "reviewing code", or "managing GitHub issues"
   ```

2. **Focused Scope**: One skill = one domain
   - ✅ `github-workflow` (focused)
   - ❌ `devops-everything` (too broad)

3. **Concrete Examples**: Provide code examples, not just theory
   ```markdown
   ### Example: Create PR
   ```bash
   gh pr create --title "..." --body "..."
   ```
   ```

4. **When NOT to use**: Help Claude know boundaries
   ```markdown
   ## When NOT to use
   - For GitLab (use gitlab-workflow skill instead)
   - For local-only Git operations (no GitHub integration)
   ```

### Command Design

1. **Step-by-Step**: Break down complex operations
2. **Error Handling**: Include common errors and solutions
3. **Clear Output**: Always show success/failure clearly
4. **Argument Hints**: Use `argument-hint` for better UX

### Agent Design

1. **Clear Responsibilities**: Define what the agent should/shouldn't do
2. **Required Tools**: List minimal tools needed
3. **Permission Mode**: Choose appropriate mode:
   - `ask` - Ask for each action
   - `acceptEdits` - Auto-approve file edits
   - `acceptAll` - Auto-approve everything (use carefully)

### Documentation

1. **README Structure**:
   - Installation
   - Prerequisites
   - Usage examples
   - Troubleshooting
   - License

2. **Code Examples**: Always include working examples
3. **Screenshots**: Add for UI-related features
4. **Links**: Reference external docs when helpful

## 🔐 Security Guidelines

1. **No Hardcoded Secrets**: Use environment variables
2. **Input Validation**: Validate all user inputs
3. **Permission Principle**: Request minimal permissions needed
4. **Safe Defaults**: Default to safer options

Example:
```python
# ❌ Bad
API_KEY = "sk-123..."

# ✅ Good
API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    print("Error: API_KEY environment variable not set")
    sys.exit(1)
```

## 🤝 Pull Request Process

1. **Create a branch**: `git checkout -b add-my-plugin`
2. **Make changes**: Follow guidelines above
3. **Test thoroughly**: Complete test checklist
4. **Commit**: Use conventional commits
   ```bash
   git commit -m "feat(plugin): add my-plugin for X workflow"
   ```
5. **Push**: `git push origin add-my-plugin`
6. **Open PR**: Include:
   - Description of the plugin
   - Use cases
   - Testing performed
   - Screenshots (if applicable)

### PR Checklist

- [ ] Plugin follows naming conventions
- [ ] README is complete
- [ ] Examples work as described
- [ ] Tested locally
- [ ] Permissions documented
- [ ] Versioning is correct
- [ ] No hardcoded secrets
- [ ] CONTRIBUTING.md followed

## 📖 Resources

- **Template Plugins**: Browse `plugins/template-*` for structure
- **Example Plugin**: Study `plugins/example-github` for best practices
- **Claude Code Docs**: [docs.anthropic.com/claude-code](https://docs.anthropic.com/claude-code)

## 💬 Getting Help

- **Questions**: Open a discussion
- **Issues**: Report bugs or feature requests
- **Examples**: Check existing plugins

---

**Ready to contribute?** Pick a template and start building!
