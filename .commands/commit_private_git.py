#!/usr/bin/env python3

from pathlib import Path
import os
from shlex import quote
from shutil import rmtree, move
from shutil import copytree, copy
from sys import argv

commitMessage = " ".join(argv[1:]) if len(argv) > 1 else "Update private_git"

commandsPath = Path(__file__).parent.absolute().resolve()
rootPath = commandsPath.parent
privateGitDirPath = commandsPath / "private_git"
privateGitPath = privateGitDirPath / ".git"
tempPath = commandsPath / "temp"

# Create the private_git repository if it doesn't exist
if not privateGitDirPath.exists():
    print(f"Create {privateGitDirPath}")
    privateGitDirPath.mkdir()
if not privateGitPath.exists():
    print(f"Create new git repository at {privateGitPath}")
    os.system(f"cd {quote(str(privateGitDirPath))} && git init")

# Remove the temp folder if it already exists and create a new one
if tempPath.exists():
    rmtree(str(tempPath))
tempPath.mkdir()

# Copy the relevant files to the temp folder
for content in rootPath.iterdir():
    if not (content.name.startswith(".")):
        if content.is_dir():
            copytree(str(content), str(tempPath / content.name))
        else:
            copy(str(content), str(tempPath / content.name))

# Move the private_git files to the temp folder
move(str(privateGitPath), str(tempPath / ".git"))
copy(str(privateGitDirPath / "gitignore.txt"), str(tempPath / ".gitignore"))

# Commit the changes
os.system(f"cd {quote(str(tempPath))} && git add . && git commit -m {quote(commitMessage)}")

# Move the private_git files back to the private_git folder
move(str(tempPath / ".git"), str(privateGitPath))

# Remove the temp folder
rmtree(str(tempPath))

