#!/usr/bin/env python3
"""
PostToolUse hook — runs after every tool call.

Hook input via stdin as JSON:
{
  "tool_name": "...",
  "tool_input": { ... },
  "tool_response": { ... }
}

Exit 0 to continue normally.
Exit 1 + print to stdout to surface a message to Claude.
Exit 2 to block the action entirely.
"""
import json
import sys


def main():
    hook_input = json.load(sys.stdin)
    tool_name = hook_input.get("tool_name", "")
    tool_input = hook_input.get("tool_input", {})

    # Example: warn before writing to a sensitive file
    # if tool_name == "Write":
    #     path = tool_input.get("path", "")
    #     if "sensitive-file.js" in path:
    #         print("Warning: you are editing a sensitive file.")
    #         sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
