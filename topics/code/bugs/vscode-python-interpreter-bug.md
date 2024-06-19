Strange bug appears when trying to execute python files. Execution does not work.
Deleting one line of the launch.json file sometimes solves the problem:
```"name": "Python: Current File",```

### Tested solutions
removed - `$HOME/.config/Code` and `~/.vscode`. files.
New installation of vscode plugins

Had to deal with [ipython-notebook-with-venv](ipython-notebook-with-venv.md) again after that