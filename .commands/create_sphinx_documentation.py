#!/usr/bin/env python3

# Creates a Sphinx documentation at the path .commands/sphinx/output

import os
from pathlib import Path
from shutil import rmtree, copytree, copy

commandsPath = Path(__file__).parent.absolute().resolve()
rootPath = commandsPath.parent
tempPath = commandsPath / "temp"
buildFilesPath = commandsPath / "sphinx_build"
outputPath = commandsPath / "output"

# Remove the temp folder if it already exists and create a new one
if tempPath.exists():
    rmtree(str(tempPath))
tempPath.mkdir()

# Remove the output folder if it already exists
if outputPath.exists():
    rmtree(str(outputPath))

# Copy the relevant files of the obsidian project to the temp folder
for content in rootPath.iterdir():
    if not (content.name.startswith(".") or content.name in ["private"]):
        if content.is_dir():
            copytree(str(content), str(tempPath / content.name))
        else:
            copy(str(content), str(tempPath / content.name))

# Copy the build files to the temp folder
for content in buildFilesPath.iterdir():
     if content.is_dir():
         copytree(str(content), str(tempPath / content.name))
     else:
        copy(str(content), str(tempPath / content.name))

# Create an table of content tree
def makeTocTreeRecursive(path, name):
    directoryContent = [x for x in path.iterdir()]
    directoryContent.sort(key=lambda x: ("0" if x.is_file() else "1") + x.name.lower())
    content_names = []
    for content in directoryContent:
        if content.is_dir():
            makeTocTreeRecursive(content, content.name)
            content_names.append(content.name + "/index")
        elif content.is_file() and content.suffix == ".md":
            content_names.append(content.name)
    with (path / "index.rst").open("w") as f:
        f.write(name + "\n")
        f.write("=" * len(name) + "\n")
        f.write("\n\n")
        f.write(".. toctree::\n    :maxdepth: 2\n    :caption: Contents:\n    \n")
        for name in content_names:
            f.write("    " + name + "\n")
makeTocTreeRecursive(tempPath, "index")


# Run the sphinx build command
os.system(f"sphinx-build {tempPath} {outputPath}")

# Remove the temp folder
rmtree(str(tempPath))

print(f"Documentation created at {outputPath}")

