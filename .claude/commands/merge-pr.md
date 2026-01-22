# Merge Pull Request

Check pull request status and prepare for merge. This command does NOT perform the actual merge - it verifies CI checks are passing and switches to the master branch.

## Usage

```
/merge-pr
```

## What This Command Does

1. **Check PR Status**: Checks if the pull request can be merged (passes CI checks)
2. **Switch to Master**: Checks out the master branch
3. **Pull Latest**: Pulls the latest changes from origin/master
4. **Cleanup**: Optionally deletes the feature branch

## Steps

### 1. Check PR Status
- List open pull requests using `gh pr list`
- Show the status of the current PR
- Verify CI checks are passing

### 2. Switch to Master
- Checkout master branch: `git checkout master`
- Ensure we're on master

### 3. Pull Latest Changes
- Pull from origin/master: `git pull origin master`
- Ensure local master is up to date

### 4. Cleanup (Optional)
- Ask if you want to delete the feature branch
- Delete local branch: `git branch -d <feature-branch>`
- Delete remote branch: `git push origin --delete <feature-branch>`

## Arguments

Use `$ARGUMENTS` to accept:
- PR number (if not the current branch's PR)
- Skip cleanup (don't delete feature branch)
- Force merge (merge even if CI is not passing)

## Example Usage

```
/merge-pr
/merge-pr 36
/merge-pr --no-cleanup
/merge-pr --force
```

## Notes

- This command does NOT perform the actual merge or push - use GitHub UI or `gh pr merge` for that
- Confirms before destructive operations (branch delete)
- Shows progress updates at each step
- Reports PR status and CI check results
- Provides links to the PR
- Updates the todo list to track progress

## Prerequisites

- Must have an open pull request
- Must have `gh` CLI installed and authenticated
- Current branch should be the feature branch from the PR
- CI checks should be passing (unless --force is used)
