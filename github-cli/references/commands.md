# GitHub CLI Command Reference

Complete reference for all GitHub CLI commands.

## Authentication

### gh auth login
Authenticate with GitHub:
```bash
gh auth login
```
Interactive flow: select hostname, auth method (browser/token), protocol (HTTPS/SSH), Git credentials.

### gh auth status
Check authentication status:
```bash
gh auth status
```

### gh auth logout
Log out from GitHub:
```bash
gh auth logout
```

### gh auth setup-git
Configure Git to use GitHub CLI credentials:
```bash
gh auth setup-git
```

## Repository Commands

### gh repo view
View repository information:
```bash
gh repo view                    # Current repo
gh repo view OWNER/REPO         # Specific repo
gh repo view --web              # Open in browser
gh repo view --json name,description,stargazerCount,url
```

### gh repo clone
Clone a repository:
```bash
gh repo clone OWNER/REPO
gh repo clone OWNER/REPO my-project
```

### gh repo create
Create a new repository:
```bash
gh repo create my-repo --public
gh repo create my-repo --private
gh repo create my-repo --clone  # Create and clone
gh repo create --source=. --public --push  # From current directory
```

### gh repo list
List repositories:
```bash
gh repo list                    # Your repos
gh repo list USERNAME           # User's repos
gh repo list ORGANIZATION       # Org repos
gh repo list --limit 10
```

### gh repo fork
Fork a repository:
```bash
gh repo fork OWNER/REPO
gh repo fork OWNER/REPO --clone
```

## Pull Request Commands

### gh pr list
List pull requests:
```bash
gh pr list                      # Open PRs
gh pr list --state all          # All PRs
gh pr list --state closed       # Closed PRs
gh pr list --state merged       # Merged PRs
gh pr list --author USERNAME    # By author
gh pr list --label "enhancement" # By label
gh pr list --limit 20
```

### gh pr view
View pull request:
```bash
gh pr view PR_NUMBER
gh pr view PR_NUMBER --web
gh pr view PR_NUMBER --json title,body,author,reviews
```

### gh pr create
Create pull request:
```bash
gh pr create                    # Interactive
gh pr create --title "Title" --body "Description"
gh pr create --title "Title" --body-file pr-template.md
gh pr create --base main --head feature-branch
gh pr create --draft            # Draft PR
gh pr create --reviewer USER1,USER2
gh pr create --label "enhancement"
```

### gh pr checkout
Checkout pull request locally:
```bash
gh pr checkout PR_NUMBER
gh pr checkout PR_NUMBER --branch my-local-branch
```

### gh pr merge
Merge pull request:
```bash
gh pr merge PR_NUMBER           # Default merge
gh pr merge PR_NUMBER --squash  # Squash merge
gh pr merge PR_NUMBER --rebase  # Rebase merge
gh pr merge PR_NUMBER --delete-branch
```

### gh pr close
Close pull request:
```bash
gh pr close PR_NUMBER
```

### gh pr reopen
Reopen pull request:
```bash
gh pr reopen PR_NUMBER
```

### gh pr review
Review pull request:
```bash
gh pr review PR_NUMBER --approve
gh pr review PR_NUMBER --request-changes --comment "Needs changes"
gh pr review PR_NUMBER --comment "Looks good"
```

### gh pr checks
Check PR status:
```bash
gh pr checks PR_NUMBER
```

### gh pr diff
View PR diff:
```bash
gh pr diff PR_NUMBER
```

### gh pr revert
Revert a pull request:
```bash
gh pr revert PR_NUMBER
gh pr revert PR_NUMBER --title "Revert title" --body "Revert description"
```

## Issue Commands

### gh issue list
List issues:
```bash
gh issue list                   # Open issues
gh issue list --state all       # All issues
gh issue list --state closed    # Closed issues
gh issue list --author USERNAME
gh issue list --label "bug"
gh issue list --limit 20
```

### gh issue view
View issue:
```bash
gh issue view ISSUE_NUMBER
gh issue view ISSUE_NUMBER --web
gh issue view ISSUE_NUMBER --json title,body,author,comments
```

### gh issue create
Create issue:
```bash
gh issue create                 # Interactive
gh issue create --title "Bug: title" --body "Description"
gh issue create --title "Bug" --body-file issue-template.md
gh issue create --title "Bug" --body "Desc" --label "bug,urgent"
gh issue create --title "Bug" --body "Desc" --assignee USERNAME
gh issue create --title "Bug" --body "Desc" --draft
```

### gh issue close
Close issue:
```bash
gh issue close ISSUE_NUMBER
gh issue close ISSUE_NUMBER --comment "Fixed"
```

### gh issue reopen
Reopen issue:
```bash
gh issue reopen ISSUE_NUMBER
```

### gh issue edit
Edit issue:
```bash
gh issue edit ISSUE_NUMBER --title "New title" --body "New body"
```

## Release Commands

### gh release list
List releases:
```bash
gh release list
gh release list --limit 10
```

### gh release view
View release:
```bash
gh release view TAG_NAME
gh release view TAG_NAME --web
```

### gh release create
Create release:
```bash
gh release create               # Interactive
gh release create v1.0.0 --title "v1.0.0" --notes "Release notes"
gh release create v1.0.0 --notes-file CHANGELOG.md
gh release create v1.0.0 --prerelease
gh release create v1.0.0 --draft
gh release create v1.0.0 --title "v1.0.0" --notes "Notes" dist/*.zip
```

### gh release delete
Delete release:
```bash
gh release delete TAG_NAME
```

### gh release download
Download release assets:
```bash
gh release download             # Latest release
gh release download TAG_NAME
gh release download --pattern "*.zip"
```

## Configuration Commands

### gh config set
Set configuration:
```bash
gh config set editor "code -w"
gh config set editor "vim"
gh config set git_protocol https
```

### gh config list
List configuration:
```bash
gh config list
```

### gh config get
Get configuration value:
```bash
gh config get editor
```

## Alias Commands

### gh alias set
Create alias:
```bash
gh alias set prl "pr list"
gh alias set prd "pr create --draft"
gh alias set il "issue list"
```

### gh alias list
List aliases:
```bash
gh alias list
```

### gh alias delete
Delete alias:
```bash
gh alias delete prl
```

## Search Commands

### gh search repos
Search repositories:
```bash
gh search repos "language:python stars:>1000"
gh search repos "user:username"
```

### gh search issues
Search issues:
```bash
gh search issues "is:open label:bug"
gh search issues "repo:owner/repo is:open"
```

### gh search code
Search code:
```bash
gh search code "function_name"
gh search code "language:python def function"
```

## Utility Commands

### gh help
Get help:
```bash
gh help                        # All commands
gh <command> --help            # Command help
gh issue --help
gh pr --help
```

### gh --version
Check version:
```bash
gh --version
```

### gh upgrade
Upgrade GitHub CLI:
```bash
gh upgrade
```

## JSON Output Fields

Common JSON fields for different resources:

**Repository:**
- `name`, `description`, `url`, `stargazerCount`, `forkCount`, `openIssuesCount`, `isPrivate`, `createdAt`, `updatedAt`

**Pull Request:**
- `number`, `title`, `body`, `state`, `author`, `reviews`, `mergeable`, `mergedAt`, `createdAt`, `updatedAt`

**Issue:**
- `number`, `title`, `body`, `state`, `author`, `comments`, `labels`, `assignees`, `createdAt`, `updatedAt`

**Release:**
- `name`, `tagName`, `body`, `publishedAt`, `assets`, `isPrerelease`, `isDraft`

## Environment Variables

- `GITHUB_TOKEN` - Authentication token
- `GH_HOST` - GitHub Enterprise hostname
- `GH_ENTERPRISE_TOKEN` - Enterprise authentication token
- `HTTP_PROXY` / `HTTPS_PROXY` - Proxy settings
