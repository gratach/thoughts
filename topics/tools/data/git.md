# Git

[Git](https://git-scm.com/) is a version control system for code projects.

#### Download (Debian)
```bash
apt install git
```

#### Initialize Git repository
```bash
git init
```

#### Add all changes as new commit
```bash
git add .
git commit -am "The commit message goes here"
```

#### Create a new branch

``` bash
git checkout -b the_name_of_the_new_branch
```

#### Merge two branches

```bash
git merge name_of_the_brach_to_merge
```

See also [how to git merge without changing anything](git-merge-without-changing-anything.md)

#### List all branches (remote and local)

```bash
git branch -v -a
```

#### Switch to an branch

```bash
git switch name_of_the_branch_to_switch_to
```

#### Delete a branch

local:
```bash
git branch -d name_of_branch
```
remote
```bash
git push -d remote_name branch_name
```

#### Discard local changes

```bash
git reset --hard HEAD
```
#### Shortcuts

Some of the git commands are also defined as shortcuts in the [bashrc config of the debian-i3-pc-setup](../linux/debian-i3-pc-setup.md)

