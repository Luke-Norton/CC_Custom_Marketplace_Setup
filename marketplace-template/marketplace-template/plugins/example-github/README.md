# GitHub Workflow Plugin

A production-ready example plugin for GitHub workflow automation, PR reviews, and issue management.

## Installation

```bash
claude plugin install example-github@your-marketplace-name
```

## Prerequisites

- `gh` CLI installed and authenticated
- Git configured with your credentials
- Access to the GitHub repositories you want to work with

## Configuration

Run the setup command to verify your environment:

```bash
/github:setup
```

## What's Included

| Component | File | Invocation | Purpose |
|-----------|------|------------|---------|
| PR Review Agent | `agents/pr-reviewer.md` | Auto-delegated | Analyzes PRs and provides detailed reviews |
| GitHub Skill | `skills/github-workflow/SKILL.md` | Auto-triggered | Best practices for GitHub workflows |
| Setup Command | `commands/setup.md` | `/github:setup` | Verify GitHub CLI setup |
| Review Command | `commands/review-pr.md` | `/github:review-pr <url>` | Review a specific PR |
| Create PR Command | `commands/create-pr.md` | `/github:create-pr` | Create PR from current branch |

## Usage Examples

### Review a Pull Request

```bash
# Review a PR with comprehensive analysis
/github:review-pr https://github.com/owner/repo/pull/123
```

The agent will:
- Fetch PR details and diff
- Analyze code changes
- Check for common issues
- Provide actionable feedback
- Suggest improvements

### Create a Pull Request

```bash
# Create a PR from current branch
/github:create-pr
```

The command will:
- Check for uncommitted changes
- Analyze commit history
- Generate PR title and description
- Create the PR with proper formatting

### Auto-Triggered Skills

The GitHub workflow skill automatically activates when you:
- Mention "create a PR"
- Ask to "review changes"
- Want to "check GitHub issues"
- Need to "update a pull request"

## Features

### Comprehensive PR Reviews
- Code quality analysis
- Security vulnerability detection
- Style and convention checking
- Performance considerations
- Test coverage assessment

### Smart PR Creation
- Automatic title generation
- Structured description with summary
- Test plan generation
- Proper base branch detection

### Issue Management
- Create issues from conversations
- Link related issues
- Update issue status
- Add labels and assignees

## Best Practices Implemented

1. **Error Handling**: Graceful handling of API failures
2. **Validation**: Checks prerequisites before operations
3. **User Feedback**: Clear progress updates and error messages
4. **Idempotency**: Safe to run commands multiple times
5. **Documentation**: Inline help and examples

## Example Workflow

```bash
# 1. Make code changes
# ... edit files ...

# 2. Let Claude review your changes
"Can you review my changes before I commit?"

# 3. Create a commit
"Create a commit with a good message"

# 4. Create a PR
/github:create-pr

# 5. Get AI review of the PR
/github:review-pr <pr-url>
```

## Permissions Required

This plugin requires:
- `Bash(gh:*)` - GitHub CLI commands
- `Bash(git:*)` - Git operations
- `Skill(github:*)` - GitHub workflow skill activation

These are pre-configured in the marketplace `base_settings.json`.

## Troubleshooting

### "gh: command not found"

Install the GitHub CLI:
```bash
# macOS
brew install gh

# Linux
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install gh

# Windows
winget install GitHub.cli
```

### "gh: authentication required"

Authenticate with GitHub:
```bash
gh auth login
```

## Advanced Usage

### Custom Review Prompts

You can customize the review focus:
```
/github:review-pr <url> --focus security
/github:review-pr <url> --focus performance
/github:review-pr <url> --focus style
```

### Integration with CI/CD

The plugin respects CI status:
- Warns about failing checks
- Suggests waiting for CI completion
- Can trigger re-runs if needed

## Contributing

This is an example plugin demonstrating best practices. Use it as inspiration for your own plugins!

## License

MIT
