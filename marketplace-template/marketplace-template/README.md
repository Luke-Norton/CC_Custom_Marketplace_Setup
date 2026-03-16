# Your Marketplace Name

Custom Claude Code plugins for your team or organization. This marketplace provides skills, commands, and agents tailored to your workflows.

## 🚀 Quick Start

### Installation

```bash
# Add this marketplace to Claude Code
claude plugin marketplace add your-username/your-marketplace

# Browse available plugins
/plugin

# Install a specific plugin
claude plugin install plugin-name@your-marketplace-name
```

### First-Time Setup

1. **Browse plugins**: Use `/plugin` to see what's available
2. **Install what you need**: Install plugins relevant to your work
3. **Try commands**: Use `/plugin-name:command` to invoke plugin commands
4. **Let skills activate**: Skills trigger automatically based on context

## 📦 Available Plugins

### Template Plugins (For Development)

| Plugin | Description | Components |
|--------|-------------|------------|
| **template-skill-only** | Simple skill template | Skill |
| **template-command-skill** | Command with background knowledge | Command + Skill |
| **template-agent** | Specialized subagent template | Agent + Command + Skill |
| **template-full** | Full-featured plugin example | All components |

### Example Plugins

| Plugin | Description | Use Case |
|--------|-------------|----------|
| **example-github** | GitHub workflow automation | PR reviews, issue management, CI/CD |

## 🎯 Updating Plugins

### Update All Plugins

```bash
# Refresh marketplace catalog
claude plugin marketplace update your-marketplace-name

# Update all installed plugins from this marketplace
claude plugin update --marketplace your-marketplace-name
```

### Update Specific Plugin

```bash
# Update a specific plugin
claude plugin update plugin-name
```

### Check for Updates

```bash
# List installed plugins and their versions
claude plugin list

# Check for available updates
claude plugin outdated
```

## 📁 Repository Structure

```
marketplace-template/marketplace-template/
├── .claude-plugin/
│   └── marketplace.json          # Marketplace catalog (plugin registry)
├── plugins/
│   ├── template-skill-only/      # Template: Skill only
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── skills/
│   │   │   └── your-skill/
│   │   │       └── SKILL.md
│   │   └── README.md
│   ├── template-command-skill/   # Template: Command + Skill
│   ├── template-agent/           # Template: Agent + Command + Skill
│   ├── template-full/            # Template: All features
│   └── example-github/           # Example: Real-world implementation
├── base_settings.json            # Shared permissions for all plugins
├── README.md                     # This file
├── CONTRIBUTING.md               # How to add plugins
└── .gitignore
```

## 🛠️ Plugin Components Explained

### Skills
Teach Claude domain knowledge and best practices. They activate automatically based on context.

**Example trigger**: When you say "review this PR", the GitHub skill activates.

### Commands
Slash commands for specific actions: `/plugin-name:command-name`

**Example**: `/github:create-pr` creates a pull request.

### Agents
Specialized subagents for complex workflows. Claude delegates to them automatically.

**Example**: PR review agent analyzes code changes comprehensively.

### Hooks
Custom logic that runs during Claude Code events (e.g., before/after tool calls).

**Example**: Warn before editing sensitive files.

### MCP (Model Context Protocol)
Connect external tools and data sources to Claude.

**Example**: Integrate with your company's internal APIs.

## 📖 Usage Examples

### Example 1: Using a Skill

```
You: "I need to create a pull request for my changes"

Claude: [github-workflow skill activates automatically]
"I'll help you create a PR. Let me first review your changes..."
```

### Example 2: Using a Command

```bash
# Direct command invocation
/github:create-pr

# With arguments
/github:create-pr develop
```

### Example 3: Agent Delegation

```
You: "Review this PR: https://github.com/owner/repo/pull/123"

Claude: [Delegates to pr-reviewer agent]
Agent analyzes the PR comprehensively and provides structured feedback...
```

## 🤝 Adding New Plugins

Want to add your own plugins? See [CONTRIBUTING.md](./CONTRIBUTING.md) for:
- Step-by-step plugin creation guide
- Template selection guide
- Best practices and conventions
- Testing and versioning guidelines

## 🔧 Configuration

### Permissions

Plugin permissions are managed in `base_settings.json`. Common patterns:

```json
{
  "permissions": {
    "allow": [
      "Bash(gh:*)",              // GitHub CLI
      "Bash(git:*)",             // Git commands
      "Skill(github:*)",         // GitHub skills
      "WebFetch(*)",             // Web requests
      "Agent(pr-reviewer)"       // Specific agent
    ],
    "deny": [
      "Bash(rm:*)",              // Prevent deletions
      "Bash(sudo:*)"             // Prevent sudo
    ]
  }
}
```

### MCP Servers

Plugins can include MCP servers for external integrations. Configure in the plugin's `.mcp.json`:

```json
{
  "mcpServers": {
    "your-service": {
      "command": "node",
      "args": ["path/to/server.js"],
      "env": {
        "API_KEY": "${YOUR_API_KEY}"
      }
    }
  }
}
```

## 🎓 Learning Resources

### For Plugin Users
- Browse available plugins: `/plugin`
- Get plugin help: `/plugin-name:help`
- Check plugin version: `claude plugin list`

### For Plugin Developers
- [CONTRIBUTING.md](./CONTRIBUTING.md) - Development guide
- [Template Plugins](./plugins/) - Reference implementations
- [Example GitHub Plugin](./plugins/example-github/) - Production-quality example

## 💡 Best Practices

### For Users
- ✅ Install only plugins you need
- ✅ Keep plugins updated
- ✅ Read plugin documentation
- ✅ Report issues to plugin maintainers

### For Developers
- ✅ Follow naming conventions (lowercase-with-hyphens)
- ✅ Provide clear documentation
- ✅ Include usage examples
- ✅ Test thoroughly before publishing
- ✅ Use semantic versioning
- ✅ Keep plugins focused (single responsibility)

## 🆘 Troubleshooting

### Plugin not found
```bash
# Refresh marketplace
claude plugin marketplace update your-marketplace-name

# List available plugins
claude plugin list --marketplace your-marketplace-name
```

### Command not working
```bash
# Check plugin is installed
claude plugin list

# Reinstall plugin
claude plugin uninstall plugin-name
claude plugin install plugin-name@your-marketplace-name
```

### Skill not activating
- Check skill trigger phrases in plugin documentation
- Verify plugin is installed and enabled
- Try explicitly mentioning the trigger phrase

## 📝 Support

- **Issues**: Open an issue in this repository
- **Questions**: Check plugin README files
- **Contributions**: See [CONTRIBUTING.md](./CONTRIBUTING.md)

## 📄 License

This marketplace template is MIT licensed. Individual plugins may have different licenses.

---

**Ready to get started?** Install a plugin with `/plugin` or start developing your own!
