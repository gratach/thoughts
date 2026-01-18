# Pip

You can use a [venv](../technologies/venv.md) to install packages in a separate environment.

Install packages from the [python package index](https://pypi.org/):
```
pip install name-of-the-package
```

To install local packages navigate in the folder of the python package (that contains the `pyproject.toml` file) and run:.

```
pip install .
```

To install a local package in a way that you can make changes to the source code and do not need to install it all the time new run:

```
pip install -e .
```

If you also want to install the dev-dependencies that where included in the `pyproject.toml`file you can run:

```
pip install -e .[dev]
```


## See also

[pytest](pytest.md)