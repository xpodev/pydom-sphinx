import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from sphinx.application import Sphinx

from builder import PyDOMBuilder
from ui.components.sphinx_component import SphinxComponent as Component


def setup(app: Sphinx):
    app.add_builder(PyDOMBuilder)
    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
