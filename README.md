# PyDOM Sphinx Template Engine

This is how you can use PyDOM as the template engine instead of Jinja:

```sh
pip install pydom-sphinx
```

## Setup
Add the extension in conf.py
```py
extensions = [ "pydom_sphinx" ]
```

## Run
```sh
sphinx-build -b pydom docs build
```
