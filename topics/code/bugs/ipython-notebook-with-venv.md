# Ipython notebook with venv

Selecting a venv environment from a specific path in vscode jupyter notebook seams to be not possible if it does not get suggested.

# Solution:

Choose venv as python interpreter with str shift P -> Python: Select Interpreter -> enter interpreter path -> Find -> select the python3 file in the venv
Then click on the kernel selector again and choose Select another Kernel -> Python environments -> the new venv option that has appeared.
Make sure that you select the normal interpreter again afterwards: str shift P -> Python: Select Interpreter -> Select at workspace level -> /bin/python3