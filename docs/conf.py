# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys, os
sys.path.insert(0, os.path.abspath(".."))

project = "PyDOM"
copyright = "2024, Xpo Development"
author = "Xpo Development"
version = "0.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "pydom_sphinx"
]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_favicon = "_static/images/favicon.ico"
html_logo = "_static/images/favicon.svg"
html_static_path = ["_static"]
html_title = "PyDOM Documentation"

html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/xpodev/seamless",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "PyPI",
            "url": "https://pypi.org/project/python-seamless",
            "icon": "fa-brands fa-python",
        },
    ],
}

html_css_files = [
    'css/custom.css',
]

rst_prolog = f"""
.. |version| replace:: {version}
.. |br| raw:: html

   <br />
"""