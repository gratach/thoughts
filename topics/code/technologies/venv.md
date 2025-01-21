# Venv

For different python programs different sets of libraries can be installed. This can be achieved by using a virtual environment like venv or conda.

Create a venv directory
```
python3 -m venv nameOfTheVenvDirectory
```
Activate the venv in the current shell session.
```
source nameOfTheVenvDirectory/bin/activate
```
Within the venv python python packages can now be installed with
```
pip install nameOfThePythonPackage
```
The venv can be left by using the command
```
deactivate
```



[select-venv-in-vscode](../../tools/editor/select-venv-in-vscode.md)
[ipython notebook with venv bug](../bugs/ipython-notebook-with-venv.md)