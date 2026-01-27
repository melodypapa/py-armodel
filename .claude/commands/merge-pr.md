# Merge Pull Request

Check pull request status, merge it, and return to master branch.

## Usage

```
/merge-pr
```

## What This Command Does

1. **Check PR Status**: Checks if the pull request can be merged (passes CI checks)
2. **Merge PR via GitHub**: Uses `gh pr merge` to merge the PR directly through GitHub
3. **Switch to Master**: Checks out the master branch
4. **Pull Latest**: Pulls the merged changes from origin/master
5. **Cleanup**: Optionally deletes the local feature branch

## Steps

### 1. Check PR Status
- List open pull requests using `gh pr list`
- Show the status of the current PR
- Verify CI checks are passing

### 2. Merge PR via GitHub
- Use `gh pr merge --delete-branch` to merge the PR directly through GitHub
- The `--delete-branch` flag ensures the remote branch is deleted after merge
- This automatically closes the PR and updates the master branch on GitHub
- Supports merge methods: merge, squash, rebase
- Example: `gh pr merge --merge --delete-branch` or `gh pr merge --squash --delete-branch`

### 3. Switch to Master
- Checkout master branch: `git checkout master`
- Ensure we're on master

### 4. Pull Latest Changes
- Pull from origin/master: `git pull origin master`
- This updates local master with the merged changes from GitHub

### 5. Cleanup (Optional)
- Ask if you want to delete the local feature branch
- Delete local branch: `git branch -d <feature-branch>`
- Remote branch is already deleted by `gh pr merge --delete-branch` command

## Arguments

Use `$ARGUMENTS` to accept:
- PR number (if not the current branch's PR)
- Merge method: `--merge`, `--squash`, or `--rebase` (default: merge)
- Skip cleanup (don't delete feature branch)
- Force merge (merge even if CI is not passing)

## Example Usage

```
/merge-pr
/merge-pr 36
/merge-pr --squash
/merge-pr 87 --rebase
/merge-pr --no-cleanup
/merge-pr --force
```

## Notes

- Always confirms before destructive operations (merge, delete)
- Shows progress updates at each step
- Uses `gh pr merge --delete-branch` to merge via GitHub API (cleaner than local merge)
- The `--delete-branch` flag ensures remote branch deletion after merge
- GitHub automatically closes the PR when merged
- Remote branch is deleted by `gh` CLI using the `--delete-branch` flag
- Reports any merge conflicts if they occur
- Provides links to the merged PR
- Updates the todo list to track progress

## Prerequisites

- Must have an open pull request
- Must have `gh` CLI installed and authenticated
- Current branch should be the feature branch from the PR
- CI checks should be passing (unless --force is used)
