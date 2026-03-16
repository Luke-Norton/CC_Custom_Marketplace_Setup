# template-full

Replace with your plugin description.

## Installation

```bash
claude plugin install template-full@your-marketplace-name
```

## Prerequisites

- List required tools
- List required credentials or access

## Configuration

```bash
export YOUR_API_KEY="your-key-here"
```

Then run the setup command:

```
/template-full:setup
```

## What's included

| Component | File | Invocation |
|-----------|------|------------|
| Agent | `agents/your-agent.md` | Delegated automatically |
| Skill | `skills/your-skill/SKILL.md` | Auto-triggered |
| Setup command | `commands/setup.md` | `/template-full:setup` |
| Command | `commands/your-command.md` | `/template-full:your-command` |
| Hook | `hooks/post-tool.py` | Runs after every tool call |
| MCP | `.mcp.json` | Loaded with plugin |
