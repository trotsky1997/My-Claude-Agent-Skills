# GitHub CLI Workflow Scenarios

Common workflow patterns and scenarios for using GitHub CLI.

## Daily Development Workflow

### Feature Development

**1. Create feature branch:**
```bash
git checkout -b feature/new-feature
```

**2. Develop and commit:**
```bash
git add .
git commit -m "feat: add new feature"
git push -u origin feature/new-feature
```

**3. Create pull request:**
```bash
gh pr create --title "feat: new feature" --body "Description of changes"
```

**4. After merge, clean up:**
```bash
git checkout main
git pull
git branch -d feature/new-feature
```

### Hotfix Workflow

**1. Create hotfix branch:**
```bash
git checkout -b hotfix/critical-bug main
```

**2. Fix and commit:**
```bash
# Make fixes
git add .
git commit -m "fix: critical bug"
git push -u origin hotfix/critical-bug
```

**3. Create PR:**
```bash
gh pr create --title "fix: critical bug" --body "Urgent fix" --label "urgent"
```

**4. Merge and tag:**
```bash
gh pr merge PR_NUMBER
gh release create v1.0.1 --title "v1.0.1" --notes "Hotfix release"
```

## Pull Request Review Workflow

### Reviewing PRs

**1. List PRs to review:**
```bash
gh pr list --label "needs-review"
```

**2. View PR details:**
```bash
gh pr view PR_NUMBER
gh pr diff PR_NUMBER
```

**3. Checkout locally for testing:**
```bash
gh pr checkout PR_NUMBER
# Test the changes
```

**4. Review and approve:**
```bash
gh pr review PR_NUMBER --approve
# Or request changes:
gh pr review PR_NUMBER --request-changes --comment "Please fix X"
```

**5. Merge after approval:**
```bash
gh pr merge PR_NUMBER --squash --delete-branch
```

### Managing Your PRs

**1. Check PR status:**
```bash
gh pr checks PR_NUMBER
gh pr view PR_NUMBER
```

**2. Update PR:**
```bash
# Make changes and push
git add .
git commit -m "fix: address review comments"
git push

# PR automatically updates
```

**3. Respond to review:**
```bash
gh pr comment PR_NUMBER --body "Thanks, fixed!"
```

## Issue Management Workflow

### Creating and Tracking Issues

**1. Create issue:**
```bash
gh issue create --title "Bug: description" --body "Steps to reproduce..." --label "bug"
```

**2. List your issues:**
```bash
gh issue list --author @me
gh issue list --label "bug"
```

**3. View issue:**
```bash
gh issue view ISSUE_NUMBER
```

**4. Create PR to fix issue:**
```bash
# After fixing
gh pr create --title "fix: #ISSUE_NUMBER description" --body "Fixes #ISSUE_NUMBER"
```

**5. Close issue when PR merged:**
```bash
# Usually automatic if PR description includes "Fixes #ISSUE_NUMBER"
# Or manually:
gh issue close ISSUE_NUMBER --comment "Fixed in PR #PR_NUMBER"
```

### Bug Triage

**1. List all open bugs:**
```bash
gh issue list --label "bug" --state open
```

**2. Assign issues:**
```bash
gh issue edit ISSUE_NUMBER --add-assignee USERNAME
```

**3. Add labels:**
```bash
gh issue edit ISSUE_NUMBER --add-label "priority:high"
```

## Release Workflow

### Creating a Release

**1. Prepare release notes:**
```bash
# Update CHANGELOG.md
# Tag the release commit
git tag v1.0.0
git push origin v1.0.0
```

**2. Build release assets:**
```bash
# Build your project
npm run build
# Create distribution files
tar -czf dist/app-v1.0.0.tar.gz dist/
zip -r dist/app-v1.0.0.zip dist/
```

**3. Create release:**
```bash
gh release create v1.0.0 \
  --title "v1.0.0" \
  --notes-file CHANGELOG.md \
  dist/app-v1.0.0.tar.gz \
  dist/app-v1.0.0.zip
```

**4. Verify release:**
```bash
gh release view v1.0.0
gh release view v1.0.0 --web
```

### Pre-release Testing

**1. Create pre-release:**
```bash
gh release create v1.0.0-beta.1 \
  --title "v1.0.0-beta.1" \
  --notes "Beta release for testing" \
  --prerelease \
  dist/app-v1.0.0-beta.1.tar.gz
```

**2. After testing, create final release:**
```bash
gh release create v1.0.0 \
  --title "v1.0.0" \
  --notes "Final release" \
  dist/app-v1.0.0.tar.gz
```

## Automation Scripts

### Automated PR Creation

**Script: `create-pr.sh`:**
```bash
#!/bin/bash
BRANCH=$(git branch --show-current)
TITLE="feat: $(git log -1 --pretty=%B)"
BODY="Automated PR from branch $BRANCH"

gh pr create --title "$TITLE" --body "$BODY" --base main --head "$BRANCH"
```

### PR Status Checker

**Script: `check-pr-status.sh`:**
```bash
#!/bin/bash
PR_NUMBER=$1

if [ -z "$PR_NUMBER" ]; then
    echo "Usage: $0 <PR_NUMBER>"
    exit 1
fi

STATUS=$(gh pr view $PR_NUMBER --json state --jq '.state')
CHECKS=$(gh pr checks $PR_NUMBER)

echo "PR #$PR_NUMBER Status: $STATUS"
echo "$CHECKS"
```

### Batch Issue Operations

**Close all stale issues:**
```bash
#!/bin/bash
# Get issues older than 90 days
gh issue list --state open --json number,createdAt --jq '.[] | select(.createdAt < "2024-01-01") | .number' | \
while read issue_num; do
    gh issue close $issue_num --comment "Closing stale issue"
done
```

### Release Automation

**Script: `release.sh`:**
```bash
#!/bin/bash
VERSION=$1

if [ -z "$VERSION" ]; then
    echo "Usage: $0 <version>"
    exit 1
fi

# Build
npm run build

# Create release
gh release create "v$VERSION" \
  --title "v$VERSION" \
  --notes-file CHANGELOG.md \
  dist/*.zip dist/*.tar.gz

echo "Release v$VERSION created"
```

## Integration Workflows

### CI/CD Integration

**GitHub Actions workflow using gh:**
```yaml
name: Create PR
on:
  push:
    branches: [ feature/* ]

jobs:
  create-pr:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
      - name: Create PR
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          gh pr create --title "Auto PR" --body "Automated PR"
```

### Local Development Integration

**Pre-commit hook:**
```bash
#!/bin/bash
# .git/hooks/pre-push

# Check if PR exists
BRANCH=$(git branch --show-current)
PR_EXISTS=$(gh pr list --head "$BRANCH" --json number --jq '.[0].number // empty')

if [ -z "$PR_EXISTS" ]; then
    echo "No PR found for branch $BRANCH"
    read -p "Create PR? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        gh pr create --title "feat: $BRANCH" --body "Auto-created PR"
    fi
fi
```

## Advanced Patterns

### Multi-Repository Operations

**Update multiple repos:**
```bash
#!/bin/bash
REPOS=("repo1" "repo2" "repo3")

for repo in "${REPOS[@]}"; do
    echo "Processing $repo..."
    gh repo clone owner/$repo
    cd $repo
    # Make changes
    git push
    gh pr create --title "Update" --body "Changes"
    cd ..
    rm -rf $repo
done
```

### PR Template Workflow

**Using PR template:**
```bash
# Create PR with template
gh pr create --title "feat: feature" --body-file .github/pull_request_template.md
```

### Issue Linking

**Link issues in PR:**
```bash
gh pr create --title "fix: bug" --body "Fixes #123, #124, #125"
```

### Draft PR Workflow

**Create draft for early feedback:**
```bash
gh pr create --draft --title "WIP: feature" --body "Early draft for feedback"
# Later, mark as ready:
gh pr ready PR_NUMBER
```

## Troubleshooting Workflows

### Authentication Issues

**Check and fix auth:**
```bash
gh auth status
gh auth login --web
gh auth refresh
```

### Permission Issues

**Verify permissions:**
```bash
gh api user
gh api repos/OWNER/REPO
```

### Network/Proxy Issues

**Set proxy:**
```bash
export HTTP_PROXY=http://proxy.example.com:8080
export HTTPS_PROXY=http://proxy.example.com:8080
gh repo list
```
