# Frequently Asked Questions

Common questions and answers about creating and using Claude Code marketplace plugins.

## General Questions

### What is a Claude Code marketplace?

A marketplace is a collection of plugins that extend Claude Code's capabilities. It allows teams and organizations to share custom skills, commands, and agents tailored to their specific workflows.

### When should I create a custom marketplace vs. use the public marketplace?

**Create a custom marketplace when:**
- You have team-specific workflows and standards
- You need proprietary knowledge or tools
- You want to control versioning and updates
- You have internal-only integrations

**Use public marketplace when:**
- You need general-purpose plugins
- You want community-maintained plugins
- You don't need customization

### Can I use multiple marketplaces?

Yes! Claude Code supports multiple marketplaces simultaneously. You can use both public and custom marketplaces:

```bash
# Add multiple marketplaces
claude plugin marketplace add anthropics/marketplace
claude plugin marketplace add my-company/marketplace
claude plugin marketplace add team-a/specialized-plugins
```

## Plugin Development

### What's the difference between skills, commands, and agents?

| Component | Purpose | Invocation | Example |
|-----------|---------|------------|---------|
| **Skill** | Teach Claude domain knowledge | Auto-triggered on context | Code review guidelines |
| **Command** | Specific action to perform | `/plugin:command` | `/github:create-pr` |
| **Agent** | Specialized subagent | Auto-delegated by Claude | PR review analysis |

### How do I decide which components my plugin needs?

Use this decision tree:

1. **Do you need to execute commands or access tools?**
   - No → Skill only
   - Yes → Continue

2. **Is it a simple, single-step action?**
   - Yes → Command + Skill
   - No → Continue

3. **Does it require complex analysis or multi-step workflow?**
   - Yes → Agent + Command + Skill
   - No → Command + Skill

4. **Do you need to intercept or modify Claude's behavior?**
   - Yes → Add Hooks
   - No → You're done

5. **Do you need external data sources or APIs?**
   - Yes → Add MCP
   - No → You're done

### Can a plugin have multiple skills?

Yes! A plugin can have multiple skills, commands, and agents:

```json
{
  "skills": [
    {
      "name": "review-guidelines",
      "path": "skills/review-guidelines/SKILL.md"
    },
    {
      "name": "testing-standards",
      "path": "skills/testing-standards/SKILL.md"
    }
  ]
}
```

### How do I make my skill activate reliably?

1. **Include clear trigger phrases** in the description:
```yaml
description: >-
  Use when "reviewing code", "checking pull requests", or "code review"
```

2. **Include "When to use" section** in the skill:
```markdown
## When to use
- Reviewing pull requests
- Analyzing code changes
- Providing code feedback
```

3. **Test with explicit mentions**:
```
"Use the code-review skill to analyze this"
```

### How do I test my plugin before publishing?

```bash
# 1. Install marketplace locally
claude plugin marketplace add file:///path/to/marketplace

# 2. Install your plugin
claude plugin install my-plugin@local

# 3. Test skill activation
# Try trigger phrases in Claude Code

# 4. Test commands
/my-plugin:my-command

# 5. Verify agents spawn
# Trigger agent scenarios

# 6. Check logs for errors
cat ~/.claude/logs/latest.log
```

## Technical Questions

### What languages can I use for hooks?

Hooks can be written in any executable scripting language:

- **Python** (recommended): Good libraries, easy to read
- **Bash/Shell**: Quick scripts, system commands
- **Node.js**: JavaScript ecosystem
- **Ruby**: Concise and expressive

Just ensure:
1. File has proper shebang (`#!/usr/bin/env python3`)
2. File is executable (`chmod +x hook.py`)
3. Hook reads JSON from stdin and exits with appropriate code

### How do hooks work?

Hooks receive input via stdin and control execution via exit codes:

```python
#!/usr/bin/env python3
import json
import sys

# Read hook input
hook_input = json.load(sys.stdin)
tool_name = hook_input.get("tool_name", "")

# Check condition
if tool_name == "Write" and "sensitive" in hook_input.get("path", ""):
    print("Warning: Editing sensitive file")
    sys.exit(1)  # Show warning to Claude

# Allow execution
sys.exit(0)
```

**Exit codes:**
- `0`: Continue normally
- `1`: Show message to Claude (warning)
- `2`: Block the action completely

### What is MCP and when should I use it?

MCP (Model Context Protocol) connects external tools and data sources to Claude.

**Use MCP when you need:**
- External API integration (GitHub, Jira, etc.)
- Database access
- File system access beyond local
- Custom tool implementations

**Example MCP server:**
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

### How do I handle sensitive data like API keys?

**Never hardcode secrets!** Use environment variables:

```python
# ❌ Bad
API_KEY = "sk-123..."

# ✅ Good
import os
API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY environment variable not set")
```

For MCP servers:
```json
{
  "env": {
    "API_KEY": "${API_KEY}"
  }
}
```

Users set environment variables before starting Claude Code:
```bash
export API_KEY="sk-..."
claude code
```

## Permissions

### How do permissions work?

Permissions control which tools Claude can use. They're defined in `base_settings.json`:

```json
{
  "permissions": {
    "allow": [
      "Bash(gh:*)",      // Allow gh CLI
      "Skill(github:*)", // Allow github skills
      "Agent(reviewer)"  // Allow reviewer agent
    ],
    "deny": [
      "Bash(rm:*)"       // Block rm commands
    ]
  }
}
```

### What's the format for permission patterns?

Format: `Tool(scope:action)`

**Examples:**
- `Bash(gh:*)` - All gh commands
- `Bash(git:push)` - Only git push
- `Skill(team:*)` - All skills in team namespace
- `Agent(*)` - All agents
- `WebFetch(https://api.example.com/*)` - Specific domain

### Can I set different permissions per plugin?

The marketplace `base_settings.json` applies to all plugins. For plugin-specific permissions, users can override in their `~/.claude/settings.json`:

```json
{
  "plugins": {
    "my-plugin": {
      "permissions": {
        "allow": ["Bash(custom-tool:*)"]
      }
    }
  }
}
```

## Versioning and Updates

### How does versioning work?

Follow [Semantic Versioning](https://semver.org/):

- **MAJOR** (1.0.0 → 2.0.0): Breaking changes
- **MINOR** (1.0.0 → 1.1.0): New features, backward compatible
- **PATCH** (1.0.0 → 1.0.1): Bug fixes

**Update version in:**
1. `.claude-plugin/plugin.json` (plugin version)
2. `.claude-plugin/marketplace.json` (catalog entry)

### How do users get updates?

```bash
# Check for updates
claude plugin outdated

# Update all plugins
claude plugin update --all

# Update specific plugin
claude plugin update my-plugin

# Update marketplace catalog
claude plugin marketplace update my-marketplace
```

### Can I have breaking changes?

Yes, but:
1. Bump MAJOR version
2. Document breaking changes in README
3. Provide migration guide
4. Consider deprecation period

```markdown
## Breaking Changes in v2.0.0

- Command `/plugin:old-command` removed
  - Migration: Use `/plugin:new-command` instead

- Skill trigger phrase changed
  - Old: "do review"
  - New: "review code"
```

## Troubleshooting

### My skill isn't activating

**Check:**
1. Skill is listed in `plugin.json`
2. Plugin is installed: `claude plugin list`
3. Trigger phrases are clear in description
4. Try explicit trigger: "Use the [skill-name] skill to..."

**Debug:**
```bash
# Check plugin installation
claude plugin list

# Reinstall plugin
claude plugin uninstall my-plugin
claude plugin install my-plugin@marketplace-name

# Check logs
tail -f ~/.claude/logs/latest.log
```

### My command isn't found

**Check:**
1. Command is in `plugin.json`
2. File path is correct
3. Command name matches filename
4. Plugin is updated

**Try:**
```bash
# List all commands
/help

# Update plugin
claude plugin update my-plugin

# Reinstall if needed
claude plugin uninstall my-plugin && claude plugin install my-plugin
```

### My agent isn't spawning

**Check:**
1. Agent is in `plugin.json`
2. Agent description clearly states when to spawn
3. Tools are correctly specified
4. Permission mode is set

**Agent won't spawn if:**
- Description is too vague
- Required tools not available
- Permissions denied
- Task doesn't match agent expertise

### Changes aren't taking effect

**Solution:**
```bash
# 1. Update marketplace catalog
claude plugin marketplace update marketplace-name

# 2. Update plugin
claude plugin update plugin-name

# 3. Restart Claude Code (if needed)
# Close and reopen Claude Code

# 4. Verify version
claude plugin list
```

### Permission denied errors

**Check `base_settings.json`:**
```json
{
  "permissions": {
    "allow": [
      "Bash(tool-name:*)"  // Add required permission
    ]
  }
}
```

**Update and reinstall:**
```bash
claude plugin marketplace update marketplace-name
claude plugin update plugin-name
```

## Best Practices

### How should I structure my plugin documentation?

Every plugin should have:

1. **README.md**:
   - Installation instructions
   - Prerequisites
   - Usage examples
   - Troubleshooting

2. **Skill SKILL.md**:
   - When to use / not use
   - Guidelines and rules
   - Examples
   - Quick reference

3. **Command .md**:
   - What it does
   - Step-by-step process
   - Error handling
   - Examples

### How detailed should skills be?

**Balance is key:**

✅ **Good - Specific and actionable:**
```markdown
When creating a PR:
1. Check for uncommitted changes: `git status`
2. Review commit history: `git log origin/main..HEAD`
3. Generate title (< 70 chars)
4. Create structured description with Summary, Changes, Test Plan
```

❌ **Too vague:**
```markdown
Create PRs the right way following best practices.
```

❌ **Too detailed:**
```markdown
[1000+ lines of every possible scenario]
```

### Should I create one big plugin or many small ones?

**Prefer small, focused plugins:**

✅ **Good:**
- `github-pr-workflow` - PR creation and review
- `github-issue-management` - Issue tracking
- `github-actions` - CI/CD workflows

❌ **Too broad:**
- `github-everything` - All GitHub features

**Benefits of focused plugins:**
- Easier to maintain
- Users install only what they need
- Clearer purpose and documentation
- Simpler testing

### How often should I update my plugins?

**Update when:**
- Bug fixes (PATCH)
- New features (MINOR)
- Breaking changes (MAJOR)
- Security issues (immediate)

**Don't update too often:**
- Let changes accumulate
- Batch related improvements
- Consider user update fatigue
- Document changes in CHANGELOG

## Publishing

### How do I publish my marketplace?

**GitHub (Recommended):**
```bash
# 1. Push to GitHub
git push origin main

# 2. Users install with
claude plugin marketplace add username/repo
```

**Self-hosted:**
```bash
# 1. Host marketplace directory
# 2. Users install with
claude plugin marketplace add https://example.com/marketplace
```

### Should I publish publicly or keep private?

**Public (GitHub public repo):**
- Open source contribution
- Community feedback
- Wider usage

**Private (GitHub private repo or self-hosted):**
- Proprietary knowledge
- Internal tools only
- Controlled access

Both work with Claude Code!

### How do I handle contributions?

1. **CONTRIBUTING.md** - Clear guidelines
2. **PR template** - Structured submissions
3. **Code review** - Quality standards
4. **Testing** - Require tests
5. **Documentation** - Require examples

## Advanced Topics

### Can plugins depend on other plugins?

Not directly, but you can:
1. Document prerequisites in README
2. Check for other plugins in commands/hooks
3. Recommend installing related plugins

```markdown
## Prerequisites

This plugin works best with:
- `github-workflow` plugin
- `code-review` plugin
```

### Can I use plugins programmatically?

Plugins integrate through Claude Code interface. For programmatic access:
- Use underlying tools directly (gh CLI, etc.)
- Create MCP server for custom logic
- Write hooks for automation

### How do I migrate users to a new plugin version?

1. **Document breaking changes** in README
2. **Provide migration guide**
3. **Consider backward compatibility period**
4. **Deprecate gradually**

```markdown
## Migration Guide v1 → v2

### Breaking Changes
- Command `/old:command` removed

### Migration Steps
1. Replace `/old:command` with `/new:command`
2. Update trigger phrase from "do X" to "perform X"
3. Review new configuration options

### Compatibility
- v1 supported until 2024-12-31
- Both versions can coexist during migration
```

## Getting Help

### Where can I get help?

1. **Documentation**:
   - README.md
   - CONTRIBUTING.md
   - GETTING_STARTED.md

2. **Examples**:
   - Template plugins
   - example-github plugin

3. **Community**:
   - Open GitHub issue
   - Discussion forums
   - Team chat

### How do I report bugs?

Open an issue with:
- Plugin name and version
- Expected behavior
- Actual behavior
- Steps to reproduce
- Logs (if available)

### How do I request features?

Open an issue with:
- Use case description
- Proposed solution
- Alternative approaches
- Why it's valuable

---

**Still have questions?** Open an issue or discussion!
