# Claude Code Custom Marketplace Template

A comprehensive template for creating your own Claude Code plugin marketplace. Perfect for teams, organizations, or projects that want to share custom skills, commands, and agents.

## 🚀 Quick Start

### 1. Use This Template

```bash
# Clone or fork this repository
git clone <your-repo-url>
cd CC_Custom_Marketplace_Setup

# Navigate to the template directory
cd marketplace-template/marketplace-template
```

### 2. Customize Your Marketplace

1. **Update marketplace metadata** in `.claude-plugin/marketplace.json`
2. **Choose a plugin template** from `plugins/` directory
3. **Customize `README.md`** with your marketplace name and details
4. **Update `base_settings.json`** with required permissions

### 3. Install Your Marketplace

```bash
# Add your marketplace to Claude Code (local development)
claude plugin marketplace add file:///path/to/your/marketplace

# Or from GitHub
claude plugin marketplace add your-username/your-marketplace
```

### 4. Browse and Install Plugins

```bash
# Browse available plugins
/plugin

# Install a specific plugin
claude plugin install your-plugin-name@your-marketplace-name
```

## 📁 Repository Structure

```
marketplace-template/marketplace-template/
├── .claude-plugin/
│   └── marketplace.json          # Marketplace catalog (plugins registry)
├── plugins/
│   ├── template-skill-only/      # Simple skill-only plugin
│   ├── template-command-skill/   # Command + skill plugin
│   ├── template-agent/           # Specialized agent plugin
│   ├── template-full/            # Full-featured plugin
│   └── example-github/           # Real-world example plugin
├── base_settings.json            # Shared permissions for all plugins
├── README.md                     # Marketplace documentation
└── CONTRIBUTING.md               # Contributor guide
```

## 🎯 Plugin Templates

| Template | Use Case | Components |
|----------|----------|------------|
| **template-skill-only** | Teaching Claude domain knowledge | Skill only |
| **template-command-skill** | Slash commands with background knowledge | Command + Skill |
| **template-agent** | Specialized subagents for complex workflows | Agent + Skill + Command |
| **template-full** | Complete plugin with all features | Agent + Skill + Command + Hook + MCP |
| **example-github** | Real-world GitHub workflow plugin | Full example implementation |

## 📚 Creating Your First Plugin

### Step 1: Choose Your Template

Start with the template that best matches your needs:

```bash
# Copy a template
cp -r plugins/template-skill-only plugins/my-plugin
cd plugins/my-plugin
```

### Step 2: Create plugin.json

Create `.claude-plugin/plugin.json`:

```json
{
  "name": "my-plugin",
  "version": "0.1.0",
  "description": "Brief description of what your plugin does",
  "author": "Your Name",
  "license": "MIT"
}
```

### Step 3: Customize the Components

Edit the files in your plugin directory:
- `README.md` - Plugin documentation
- `skills/*/SKILL.md` - Skill definitions
- `commands/*.md` - Command definitions
- `agents/*.md` - Agent definitions

### Step 4: Register in Marketplace

Add your plugin to `.claude-plugin/marketplace.json`:

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

### Step 5: Test Your Plugin

```bash
# Install your plugin locally
claude plugin install my-plugin@your-marketplace-name

# Test it works
/my-plugin:command-name
```

## 🔧 Advanced Features

### Hooks

Hooks execute custom logic during Claude Code events:

```python
# hooks/post-tool.py
def main():
    hook_input = json.load(sys.stdin)
    tool_name = hook_input.get("tool_name", "")

    # Custom validation or logging
    if tool_name == "Write" and "config" in tool_input.get("path", ""):
        print("Warning: Modifying configuration file")
        sys.exit(1)  # Surface warning to Claude
```

### MCP (Model Context Protocol)

Connect external tools and data sources:

```json
{
  "mcpServers": {
    "your-service": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-your-service"]
    }
  }
}
```

### Permissions

Control tool access in `base_settings.json`:

```json
{
  "permissions": {
    "allow": [
      "Bash(gh:*)",
      "Skill(your-marketplace:*)",
      "WebFetch(*)"
    ],
    "deny": [
      "Bash(rm:*)"
    ]
  }
}
```

## 📖 Examples

### Example 1: Code Review Skill

```yaml
---
name: code-review
description: >-
  Use when reviewing pull requests, analyzing code quality,
  or providing feedback on code changes.
---

# Code Review Guidelines

## Checklist
- [ ] Code follows team style guide
- [ ] Tests are included and passing
- [ ] Documentation is updated
- [ ] No security vulnerabilities
- [ ] Performance considerations addressed
```

### Example 2: Deployment Command

```yaml
---
name: deploy
description: Deploy to specified environment
argument-hint: [environment]
---

# Deploy Command

## Steps

1. Validate environment argument (dev/staging/prod)
2. Run tests: `npm test`
3. Build application: `npm run build`
4. Deploy: `./scripts/deploy.sh {environment}`
5. Verify deployment health check
```

### Example 3: Testing Agent

```yaml
---
name: test-generator
description: Generate comprehensive tests for code changes
model: inherit
tools: Bash, Read, Write, Edit, Grep
permissionMode: acceptEdits
---

# Test Generator Agent

## Responsibilities
- Analyze code to understand test requirements
- Generate unit tests with good coverage
- Generate integration tests for APIs
- Ensure tests follow project conventions
```

## 🤝 Contributing

See [CONTRIBUTING.md](./marketplace-template/marketplace-template/CONTRIBUTING.md) for detailed instructions on:
- Adding new plugins
- Versioning guidelines
- Best practices
- Testing your plugins

## 📝 Best Practices

### Skill Design
- ✅ Use clear trigger phrases in descriptions
- ✅ Include "When to use" and "When NOT to use" sections
- ✅ Provide concrete examples
- ✅ Keep focused on a single domain

### Command Design
- ✅ Provide clear step-by-step instructions
- ✅ Include error handling guidance
- ✅ Use argument hints for better UX
- ✅ Test thoroughly before publishing

### Agent Design
- ✅ Clearly define responsibilities
- ✅ Specify required tools and permissions
- ✅ Set appropriate permission mode
- ✅ Document any constraints or rules

### Naming Conventions
- Use lowercase with hyphens: `github-workflow` not `GitHubWorkflow`
- Be descriptive: `deploy-kubernetes` not `k8s-deploy`
- Namespace related plugins: `aws-s3`, `aws-lambda`, `aws-ec2`

## 📦 Real-World Examples

Check out the `example-github` plugin for a complete, production-ready example that includes:
- GitHub PR workflow automation
- Code review assistance
- Issue management
- CI/CD integration

## 🔗 Resources

- [Claude Code Documentation](https://docs.anthropic.com/claude-code)
- [Marketplace Best Practices](https://github.com/anthropics/claude-code/blob/main/docs/marketplace.md)
- [Plugin Development Guide](https://github.com/anthropics/claude-code/blob/main/docs/plugins.md)

## 📄 License

MIT License - Feel free to use this template for your own marketplace!

## 🆘 Support

- Open an issue for bugs or feature requests
- Check existing plugins for inspiration
- Review the example plugins in this repository

---

**Ready to build?** Start with `template-skill-only` and expand from there!
