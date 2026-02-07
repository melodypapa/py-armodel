# Merge Pull Request

Check pull request status, merge it (or handle auto-merged PRs), and cleanup branches.

## Usage

```
/merge-pr
```

## What This Command Does

1. **Check PR Status**: Checks if the pull request is already merged or can be merged
2. **Handle Merge**:
   - If PR is **already merged** (by GitHub auto-merge): Cleanup branches directly
   - If PR is **open**: Merge it via GitHub with `gh pr merge --delete-branch`
3. **Switch to Master**: Checks out the master/main branch
4. **Pull Latest**: Pulls the merged changes from origin
5. **Cleanup**: Deletes both remote and local feature branches

## Steps

### 1. Check PR Status
- List open pull requests using `gh pr list`
- Check if the PR for current branch is already merged
- Show the status of the current PR
- Verify CI checks are passing (if not merged)

### 2. Handle Merge or Auto-Merge

**Case A: PR is Already Merged (GitHub Auto-Merge)**
- Skip `gh pr merge` command
- Proceed directly to branch cleanup
- Manually delete remote branch: `git push origin --delete <feature-branch>`
- Update local master/main with merged changes

**Case B: PR is Open (Needs Manual Merge)**
- Use `gh pr merge --delete-branch` to merge the PR directly through GitHub
- The `--delete-branch` flag ensures the remote branch is deleted after merge
- This automatically closes the PR and updates the master branch on GitHub
- Supports merge methods: merge, squash, rebase
- Example: `gh pr merge --merge --delete-branch` or `gh pr merge --squash --delete-branch`

### 3. Switch to Master
- Checkout master/main branch: `git checkout main` (or `master`)
- Ensure we're on the main branch

### 4. Pull Latest Changes
- Pull from origin: `git pull`
- This updates local main/master with the merged changes from GitHub

### 5. Cleanup Branches
- **Remote branch**:
  - Already deleted if merged via `gh pr merge --delete-branch`
  - Manually delete if auto-merged: `git push origin --delete <feature-branch>`
- **Local branch**: Ask if you want to delete the local feature branch
  - Delete local branch: `git branch -d <feature-branch>`
- Confirm branch deletions before executing

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
- Handles **auto-merged PRs** by cleaning up remote and local branches
- Uses `gh pr merge --delete-branch` to merge via GitHub API (cleaner than local merge)
- The `--delete-branch` flag ensures remote branch deletion after merge
- GitHub automatically closes the PR when merged
- Remote branch cleanup:
  - Manual merge via `gh`: Deleted by `--delete-branch` flag
  - Auto-merge by GitHub: Manually deleted with `git push origin --delete`
- Reports any merge conflicts if they occur
- Provides links to the merged PR
- Updates the todo list to track progress

## Auto-Merge Scenario

When GitHub is configured to auto-merge PRs (via branch protection rules or auto-merge settings):

1. **PR gets merged automatically** when CI checks pass
2. **Remote branch remains** on GitHub (not auto-deleted)
3. **This command detects** the PR is already merged
4. **Cleanup actions**:
   - Switch to main/master branch
   - Pull latest changes
   - Delete remote branch: `git push origin --delete <feature-branch>`
   - Delete local branch: `git branch -d <feature-branch>`

This ensures both remote and local feature branches are properly cleaned up after auto-merge.

## Prerequisites

- Must have `gh` CLI installed and authenticated
- Current branch should be the feature branch from the PR
- CI checks should be passing (unless --force is used)
- For open PRs: PR must exist in the repository
- For merged PRs: PR must be successfully merged
