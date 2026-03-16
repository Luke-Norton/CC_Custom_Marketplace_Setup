# Contributing

How to add new plugins to this marketplace.

## Quick start

1. Copy the closest template from `plugins/` to `plugins/your-plugin-name/`
2. Fill in the contents
3. Register it in `.claude-plugin/marketplace.json`
4. Open a pull request

## Choose your template

| Template | Use when |
|----------|----------|
| `template-skill-only` | You only need to teach Claude domain knowledge |
| `template-command-skill` | You need a slash command + background knowledge |
| `template-agent` | You need a specialized subagent for complex tasks |
| `template-full` | You need everything — agent, skill, command, hook, and MCP |

## Plugin structure

```
plugins/your-plugin-name/
├── .claude-plugin/
│   └── plugin.json           # Required
├── skills/                   # Optional
│   └── your-skill/
│       └── SKILL.md
├── commands/                 # Optional
│   └── your-command.md
├── agents/                   # Optional
│   └── your-agent.md
├── hooks/                    # Optional
│   └── post-tool.py
├── .mcp.json                 # Optional
└── README.md
```

## Register in marketplace.json

Add your plugin to `.claude-plugin/marketplace.json`:

```json
{
  "name": "your-plugin-name",
  "version": "0.1.0",
  "source": "./plugins/your-plugin-name",
  "description": "What your plugin does"
}
```

## Versioning

- `PATCH` (0.1.0 → 0.1.1): Bug fixes, typo corrections
- `MINOR` (0.1.0 → 0.2.0): New skills, commands, or features
- `MAJOR` (0.1.0 → 1.0.0): Breaking changes

Always bump both the plugin's `plugin.json` and the entry in `marketplace.json`.

## Permissions

If your plugin needs tool permissions, add them to `base_settings.json`:

```json
{
  "permissions": {
    "allow": [
      "Bash(your-tool:*)",
      "Skill(your-plugin-name:*)"
    ]
  }
}
```

## Naming conventions

- Lowercase with hyphens: `my-plugin` not `MyPlugin`
- Be descriptive: `github-workflow` not `gh`
