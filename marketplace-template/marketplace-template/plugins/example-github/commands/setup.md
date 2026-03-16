---
name: setup
description: Verify GitHub CLI setup and authentication
---

# GitHub Setup

Verify that your environment is properly configured for GitHub workflows.

## Steps

### 1. Check if gh CLI is installed

```bash
if command -v gh &> /dev/null; then
    echo "✓ GitHub CLI is installed"
    gh --version
else
    echo "✗ GitHub CLI is not installed"
fi
```

If not installed, provide installation instructions based on the platform:

**macOS:**
```bash
brew install gh
```

**Linux (Debian/Ubuntu):**
```bash
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install gh
```

**Windows:**
```bash
winget install GitHub.cli
```

### 2. Check authentication status

```bash
gh auth status
```

If not authenticated, guide the user to login:

```bash
gh auth login
```

Follow the prompts:
1. Choose GitHub.com or GitHub Enterprise
2. Select authentication method (browser or token)
3. Complete authentication

### 3. Verify git configuration

```bash
# Check git is installed
git --version

# Check user configuration
git config --global user.name
git config --global user.email
```

If not configured:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 4. Test GitHub CLI access

```bash
# Test basic API access
gh api user --jq '.login'

# Test repo access (if in a repo)
if git rev-parse --git-dir > /dev/null 2>&1; then
    gh repo view
fi
```

### 5. Display setup summary

Print a summary of the configuration:

```
✓ GitHub CLI installed: gh version X.Y.Z
✓ Authenticated as: <username>
✓ Git configured: <name> <email>
✓ API access: Working

Your GitHub workflow environment is ready!

Try these commands:
  /github:create-pr - Create a pull request
  /github:review-pr <url> - Review a pull request
  "review my changes" - Get AI-powered code review
```

### 6. Optional: Check for common tools

```bash
# Check for useful tools
echo "Optional tools:"
command -v jq &> /dev/null && echo "✓ jq installed" || echo "✗ jq not installed (recommended for JSON parsing)"
command -v delta &> /dev/null && echo "✓ delta installed" || echo "✗ delta not installed (recommended for better diffs)"
```

## Error Handling

If any step fails:
1. Provide clear error message
2. Suggest specific solution
3. Offer to help with next steps

## Success Criteria

All checks must pass:
- [x] GitHub CLI installed
- [x] Authenticated with GitHub
- [x] Git configured
- [x] API access working
