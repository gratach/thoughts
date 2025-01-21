#!/usr/bin/env python3

from sys import argv
from datetime import datetime
from pathlib import Path
import os
from shlex import quote

commitMessage = " ".join(argv[1:]) if len(argv) > 1 else "Updated knowledge base at " + datetime.now().strftime("%Y-%m-%d")
commandsPath = Path(__file__).parent.absolute().resolve()
rootPath = commandsPath.parent

# Commit the changes in the public knowledge base
os.system(f"cd {quote(str(rootPath))} && git add . && git commit -am {quote(commitMessage)}")
# Commit the private knowledge base
os.system(f"python3 {quote(str(commandsPath / 'commit_private_git.py'))} {quote(commitMessage)}")
