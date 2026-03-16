# Claude Code Marketplace Quick Reference

A one-page reference for creating and using Claude Code marketplaces.

## 🏗️ Marketplace Structure

```
marketplace/
├── .claude-plugin/
│   └── marketplace.json          ← Catalog of all plugins
├── plugins/
│   └── my-plugin/
│       ├── .claude-plugin/
│       │   └── plugin.json       ← Plugin metadata
│       ├── skills/               ← Domain knowledge
│       ├── commands/             ← Slash commands
│       ├── agents/               ← Specialized subagents
│       ├── hooks/                ← Event handlers
│       ├── .mcp.json            ← External integrations
│       └── README.md
├── base_settings.json            ← Shared permissions
└── README.md
```

## 🎯 Component Types

| Component | Purpose | Trigger | Example |
|-----------|---------|---------|---------|
| **Skill** | Teach Claude | Auto on context | Code review rules |
| **Command** | Execute action | `/plugin:cmd` | Create PR |
| **Agent** | Complex workflow | Auto-delegated | Analyze PR |
| **Hook** | Intercept events | Auto on event | Validate before write |
| **MCP** | External data | Auto-loaded | GitHub API |

## 📝 File Templates

### marketplace.json
```json
{
  "name": "my-marketplace",
  "version": "1.0.0",
  "description": "Description",
  "plugins": [
    {
      "name": "plugin-name",
      "version": "1.0.0",
      "source": "./plugins/plugin-name",
      "description": "What it does"
    }
  ]
}
```

### plugin.json
```json
{
  "name": "my-plugin",
  "version": "1.0.0",
  "description": "What it does",
  "author": "Your Name",
  "license": "MIT",
  "skills": [{"name": "skill", "path": "skills/skill/SKILL.md"}],
  "commands": [{"name": "cmd", "path": "commands/cmd.md"}],
  "agents": [{"name": "agent", "path": "agents/agent.md"}]
}
```

### SKILL.md
```yaml
---
name: my-skill
description: >-
  When to use: "trigger phrase 1", "trigger phrase 2"
---

# Skill Name

## When to use
- Situation 1
- Situation 2

## When NOT to use
- Out of scope

## Guidelines
Step-by-step or rules

## Examples
Concrete examples
```

### command.md
```yaml
---
name: my-command
description: What this does
argument-hint: [arg]
---

# Command Name

## Steps
1. Step 1
2. Step 2

## Error Handling
Common errors and solutions
```

### agent.md
```yaml
---
name: my-agent
description: When to spawn this agent
model: inherit
tools: Bash, Read, Write, Edit
permissionMode: acceptEdits
---

# Agent Name

## Responsibilities
- What it does
- What it doesn't do

## Rules
- Always do X
- Never do Y
```

## 🚀 Common Commands

### Marketplace Management
```bash
# Add marketplace
claude plugin marketplace add username/repo

# List marketplaces
claude plugin marketplace list

# Update catalog
claude plugin marketplace update name

# Remove marketplace
claude plugin marketplace remove name
```

### Plugin Management
```bash
# Install plugin
claude plugin install name@marketplace

# List plugins
claude plugin list

# Update plugin
claude plugin update name

# Uninstall plugin
claude plugin uninstall name

# Check for updates
claude plugin outdated
```

### Testing Locally
```bash
# Add local marketplace
claude plugin marketplace add file:///path/to/marketplace

# Install from local
claude plugin install plugin@local
```

## 🔒 Permissions Format

```json
{
  "permissions": {
    "allow": [
      "Bash(tool:*)",           // All tool commands
      "Bash(tool:specific)",    // Specific command
      "Skill(namespace:*)",     // All skills in namespace
      "Agent(agent-name)",      // Specific agent
      "WebFetch(*)"            // All web requests
    ],
    "deny": [
      "Bash(rm:*)",            // Block rm
      "Bash(sudo:*)"           // Block sudo
    ]
  }
}
```

## 📊 Versioning (Semantic Versioning)

| Change | Version | Example |
|--------|---------|---------|
| Bug fix | PATCH | 1.0.0 → 1.0.1 |
| New feature | MINOR | 1.0.0 → 1.1.0 |
| Breaking change | MAJOR | 1.0.0 → 2.0.0 |

**Update in:**
1. `.claude-plugin/plugin.json`
2. `.claude-plugin/marketplace.json`

## 🎨 Naming Conventions

✅ **Good:**
- `github-workflow`
- `code-review`
- `deploy-production`

❌ **Bad:**
- `GitHubWorkflow` (PascalCase)
- `gh` (too short)
- `plugin` (not descriptive)

**Rules:**
- Lowercase with hyphens
- Descriptive, not abbreviated
- Action-oriented for commands

## 🧪 Testing Checklist

- [ ] Plugin installs without errors
- [ ] Commands work: `/plugin:command`
- [ ] Skills activate on trigger phrases
- [ ] Agents spawn appropriately
- [ ] Permissions configured correctly
- [ ] Documentation complete
- [ ] Examples work as described

## 🐛 Quick Troubleshooting

### Skill not activating
```bash
# Check installed
claude plugin list

# Reinstall
claude plugin uninstall name
claude plugin install name@marketplace

# Try explicit: "Use skill-name skill to..."
```

### Command not found
```bash
# Check commands
/help

# Update plugin
claude plugin update name

# Verify in plugin.json
```

### Changes not taking effect
```bash
# Update marketplace
claude plugin marketplace update name

# Update plugin
claude plugin update name

# Restart Claude Code
```

## 📚 Decision Trees

### Choose Template
```
Do you need to execute commands?
├─ No → template-skill-only
└─ Yes
   └─ Complex multi-step workflow?
      ├─ No → template-command-skill
      └─ Yes → template-agent or template-full
```

### Choose Component
```
What do you need?

Teach knowledge → Skill
Execute action → Command
Complex analysis → Agent
Intercept behavior → Hook
External data → MCP
```

## 💡 Best Practices

### Skills
- ✅ Clear trigger phrases in description
- ✅ Concrete examples with code
- ✅ "When NOT to use" section
- ✅ Keep focused (one domain)

### Commands
- ✅ Step-by-step instructions
- ✅ Error handling section
- ✅ Clear success/failure messages
- ✅ Argument hints

### Agents
- ✅ Clear responsibilities
- ✅ Minimal required tools
- ✅ Explicit rules (do/don't)
- ✅ Appropriate permission mode

### Documentation
- ✅ Installation instructions
- ✅ Usage examples
- ✅ Prerequisites listed
- ✅ Troubleshooting section

## 🔐 Security Checklist

- [ ] No hardcoded secrets
- [ ] Use environment variables
- [ ] Minimal permissions requested
- [ ] Input validation
- [ ] Safe default behaviors

### Example: Secure Credentials
```python
# ❌ Bad
API_KEY = "sk-123..."

# ✅ Good
import os
API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY not set")
```

## 📦 Publishing Checklist

- [ ] All files present (plugin.json, README, etc.)
- [ ] Version bumped correctly
- [ ] Documentation complete
- [ ] Examples work
- [ ] Tested locally
- [ ] Git committed and pushed
- [ ] Marketplace.json updated

## 🎯 Quick Start (30 seconds)

```bash
# 1. Copy template
cp -r plugins/template-skill-only plugins/my-plugin

# 2. Create plugin.json
cat > plugins/my-plugin/.claude-plugin/plugin.json <<EOF
{
  "name": "my-plugin",
  "version": "0.1.0",
  "description": "What it does",
  "author": "Me",
  "skills": [{"name": "skill", "path": "skills/skill/SKILL.md"}]
}
EOF

# 3. Register in marketplace.json (add to plugins array)

# 4. Test
claude plugin marketplace add file://$(pwd)
claude plugin install my-plugin@local
```

## 📖 Essential Documentation

1. **README.md** - Overview
2. **GETTING_STARTED.md** - Tutorial
3. **CONTRIBUTING.md** - Development guide
4. **FAQ.md** - Q&A
5. **example-github/** - Reference implementation

## 🆘 Get Help

- Check FAQ.md
- Study example-github plugin
- Read CONTRIBUTING.md
- Open GitHub issue

---

## 🎓 Learning Path

**Beginner:** Read README → Follow GETTING_STARTED → Create first skill
**Intermediate:** Add commands → Study examples → Create full plugin
**Advanced:** Implement agents → Add hooks → MCP integration

---

## 📊 At a Glance

| Task | Time | Difficulty |
|------|------|------------|
| Install marketplace | 1 min | ⭐ |
| Create skill plugin | 30 min | ⭐⭐ |
| Add command | 15 min | ⭐⭐ |
| Create agent | 1 hour | ⭐⭐⭐ |
| Add hooks | 30 min | ⭐⭐⭐ |
| MCP integration | 1 hour | ⭐⭐⭐⭐ |

---

**Print this page for quick reference!**
