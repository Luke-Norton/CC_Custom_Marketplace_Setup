# Your Marketplace Name

Claude Code plugins for your team or project.

## Installation

```bash
# Add this marketplace to Claude Code
claude plugin marketplace add your-username/your-marketplace

# Browse and install plugins
/plugin
```

## Updating

```bash
# Refresh marketplace catalog
claude plugin marketplace update your-marketplace-name

# Update a specific plugin
claude plugin update your-plugin-name
```

## Repository structure

```
.
├── .claude-plugin/
│   └── marketplace.json          # Marketplace catalog
├── plugins/
│   ├── template-skill-only/      # Skill only
│   ├── template-command-skill/   # Command + skill
│   ├── template-agent/           # Agent + skill + command
│   └── template-full/            # Agent + skill + command + hook + MCP
├── base_settings.json            # Shared permissions
├── README.md
└── CONTRIBUTING.md
```

## Adding new plugins

See [CONTRIBUTING.md](./CONTRIBUTING.md).
