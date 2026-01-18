
# Pytest

## Basic usage

Install the [pytest](https://pypi.org/project/pytest/) package in the [venv](../technologies/venv.md) that you use for running the package.

Structure your python project like:

```
your-package/
│
├─ pyproject.toml
├─ src/
│   └─ ...
└─ tests/
    ├─ test_1.py
    └─ test_2.py

```
Add to the `pyproject.toml` file:
```
[project.optional-dependencies]
dev = [
	"pytest",
	"pytest-cov",
]

[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["src"]
```

Run the tests using `python3 -m pytest`

## Usage with vscode

Add an additional `.vscode`directory to the project with the following content:

```
your-package/
│
├─ .vscode
│   └─ settings.json
│
...
```
The `settings.json` should contain the following lines:
```
{
	"python.testing.pytestArgs": [
		"tests"
	],
	"python.testing.unittestEnabled": false,
	"python.testing.pytestEnabled": true
}
```
The [correct venv should be selected in vscode](../../tools/editor/select-venv-in-vscode.md) that contains the dependencies such as pytest.

Tests can be then run by selecting the test tube symbol in the left sidebar and clicking on `run tests`or `debug tests` under the correct project.

## Tracking the code coverage of the tests

Its nice to keep track of which lines of the code where executed by the tests. This can be done by using the [pytest-cov](https://pypi.org/project/pytest-cov/) package that can be installed with [pip](pip.md) using the dev-dependencies.

The coverage test can be run with:
```
pytest --cov=src
```
Where src is the folder that contains the source code.

It is nice to create a visual overview over all code lines that where executed. This can be done by executing:

```
pytest --cov=src --cov-report=html
```

This will create a `htmlcov` directory in the project folder that contains a `index.html`file that can be opened in the browser to show a visual overview.

Instead of `pytest-cov` the same result can also be achieved with the `coverage` package and:

```
coverage run -m pytest
coverage html
```

## Example projects that use pytest

[digital-voting](https://github.com/gratach/digital-voting)




