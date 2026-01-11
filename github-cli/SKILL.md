---

name: github-cli

description: Comprehensive guide for using GitHub CLI (gh) to interact with GitHub from the command line. Use when (1) Managing GitHub repositories, issues, pull requests, or releases from terminal, (2) Automating GitHub workflows in scripts, (3) Creating or managing pull requests, (4) Working with GitHub issues, (5) Creating releases or managing repository operations, (6) Integrating GitHub operations into development workflows, (7) Using GitHub CLI commands in automation scripts
metadata:
  short-description: GitHub CLI command reference and workflows

---

# GitHub CLI (gh)

GitHub CLI (`gh`) enables terminal-based interaction with GitHub for managing repositories, issues, pull requests, and releases.

## Quick Start

**Authentication:**

```bash
gh auth login          # First-time setup
gh auth status         # Check authentication
```

**Basic operations:**

```bash
gh repo view                    # View current repository
gh pr list                      # List pull requests
gh issue list                   # List issues
gh pr create                    # Create pull request
```

## Core Workflows

### Repository Operations

**View repository:**

```bash
gh repo view OWNER/REPO
gh repo view --web              # Open in browser
```

**Clone and create:**

```bash
gh repo clone OWNER/REPO
gh repo create my-repo --public
gh repo create my-repo --private --clone
```

**List repositories:**

```bash
gh repo list                    # Your repos
gh repo list USERNAME           # User's repos
gh repo list --limit 10
```

### Pull Request Workflow

**Create PR:**

```bash
# Interactive
gh pr create

# Direct
gh pr create --title "feat: feature" --body "description"
gh pr create --draft            # Draft PR
gh pr create --base main --head feature-branch
```

**Manage PRs:**

```bash
gh pr list                      # List PRs
gh pr view PR_NUMBER            # View PR
gh pr checkout PR_NUMBER        # Checkout locally
gh pr merge PR_NUMBER           # Merge PR
gh pr close PR_NUMBER           # Close PR
gh pr review PR_NUMBER --approve # Review
```

**PR status and diff:**

```bash
gh pr checks PR_NUMBER          # Check status
gh pr diff PR_NUMBER            # View diff
gh pr view PR_NUMBER --web      # Open in browser
```

### Issue Management

**Create and list:**

```bash
gh issue create --title "Bug: title" --body "description"
gh issue list                   # List open issues
gh issue list --state all       # All issues
gh issue list --label "bug"     # Filter by label
```

**Manage issues:**

```bash
gh issue view ISSUE_NUMBER
gh issue close ISSUE_NUMBER --comment "Fixed"
gh issue reopen ISSUE_NUMBER
gh issue edit ISSUE_NUMBER --title "New title"
```

### Release Management

**Create release:**

```bash
gh release create v1.0.0 --title "v1.0.0" --notes "Release notes"
gh release create v1.0.0 --notes-file CHANGELOG.md
gh release create v1.0.0 --prerelease  # Pre-release
gh release create v1.0.0 dist/*.zip    # With assets
```

**Manage releases:**

```bash
gh release list
gh release view TAG_NAME
gh release download TAG_NAME
gh release delete TAG_NAME
```

## Configuration

**Set editor:**

```bash
gh config set editor "code -w"  # VS Code
gh config set editor "vim"
```

**Create aliases:**

```bash
gh alias set prl "pr list"
gh alias set prd "pr create --draft"
gh alias set il "issue list"
gh alias list                  # View aliases
```

**Git credentials:**

```bash
gh auth setup-git
```

## Advanced Usage

### JSON Output and Filtering

**JSON output:**

```bash
gh pr list --json number,title,author
gh repo view --json name,stargazerCount,url
gh issue view ISSUE_NUMBER --json title,body,comments
```

**With jq filtering:**

```bash
gh pr list --json number,title,author --jq '.[] | select(.author.login == "username")'
```

### Automation Scripts

**Create PR script:**

```bash
#!/bin/bash
BRANCH=$(git branch --show-current)
gh pr create --title "feat: feature" --body "Description" --base main --head "$BRANCH"
```

**Check PR status:**

```bash
#!/bin/bash
STATUS=$(gh pr view $1 --json state --jq '.state')
echo "PR #$1 status: $STATUS"
```

### Search

```bash
gh search repos "language:python stars:>1000"
gh search issues "is:open label:bug"
gh search code "function_name"
```

## Common Patterns

**Daily development:**

```bash
git checkout -b feature/new-feature
git push -u origin feature/new-feature
gh pr create --title "feat: new feature" --body "Description"
# After merge:
git checkout main && git pull && git branch -d feature/new-feature
```

**Review PR:**

```bash
gh pr list
gh pr view PR_NUMBER
gh pr checkout PR_NUMBER        # Test locally
gh pr review PR_NUMBER --approve
```

**Batch operations:**

```bash
# Close all open issues (use with caution)
gh issue list --state open --json number --jq '.[].number' | xargs -I {} gh issue close {}
```

## Troubleshooting

**Authentication:**

```bash
gh auth status                 # Check status
gh auth login                  # Re-authenticate
gh auth logout                 # Clear auth
```

**Environment variables:**

```bash
export GITHUB_TOKEN=your_token  # Linux/Mac
$env:GITHUB_TOKEN="token"      # Windows PowerShell
```

## References

For detailed command reference and advanced workflows, see:

- [commands.md](references/commands.md) - Complete command reference
- [workflows.md](references/workflows.md) - Common workflow scenarios

