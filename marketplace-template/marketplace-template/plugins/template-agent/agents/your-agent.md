---
name: your-agent
description: >-
  Describe when this agent should be spawned.
  Be specific — Claude uses this to decide whether to delegate to this agent.
model: inherit
tools: Bash, Read, Write, Edit
permissionMode: acceptEdits
---

# Your Agent

Describe this agent's role, expertise, and personality in one sentence.

## Responsibilities

- Primary responsibility
- Secondary responsibility

## Rules

- Always do X before doing Y
- Never modify Z without user confirmation
- If you encounter [situation], do [action]

## Output format

Describe how this agent should present its results.
