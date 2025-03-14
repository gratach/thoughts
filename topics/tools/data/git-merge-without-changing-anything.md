# Git merge without changing anything

When there are two [[git]] branches that should be merged but one of them is already in a perfect state that needs no changes a fake merge can be conducted without accepting any changes from the other branch. The solution is described in [this discussion](https://stackoverflow.com/questions/47670237/how-to-merge-a-branch-into-master-without-changes).

checkout the branch that is already perfect.

```bash
git merge branch-to-merge
```

If any merge conflicts ignore them and commit

```bash
git add every thing
git commit
```

Get the recent commit hash of the merge

```bash
git log
```

Reset the HEAD to bring the working directory in the perfect state before the merge

```bash
git reset HEAD~ --hard
```

Go back to the merge commit without changing the working directory

```bash
git reset 12345abc --soft
```

Overwrite the merge commit without changing the commit message to the current state of the working directory

```bash
git commit --amend --no-edit
```