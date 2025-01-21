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
     copy(str(content), str(tempPath / content.name))

# Run the sphinx build command
os.system(f"sphinx-build {tempPath} {outputPath}")

# Remove the temp folder
rmtree(str(tempPath))

print(f"Documentation created at {outputPath}")

