import importlib
import importlib.util

from docutils.nodes import document, Node, Element
from sphinx.builders import Builder

from pydom import Component, Fragment, render

TEMPLATE_COMPONENTS = {
    "paragraph": "Paragraph",
    "document": "Document",
}


class PyDOMBuilder(Builder):
    name = "pydom"

    def init(self):
        self.components = {
            name: self._import_template(name) for name in TEMPLATE_COMPONENTS.keys()
        }

    def prepare_writing(self, docnames: set[str]) -> None:
        return

    def get_outdated_docs(self) -> list:
        return []

    def write_doc(self, docname: str, doctree: document) -> None:
        rendered = render(self.as_pydom_tree(doctree))
        outfile = self.get_outfilename(docname)
        with open(outfile, "w") as file:
            file.write(rendered)

    def finish(self) -> None:
        return super().finish()

    def get_target_uri(self, docname: str, typ: str | None = None) -> str:
        return ""

    def get_relative_uri(self, from_: str, to: str, typ: str | None = None) -> str:
        return ""

    def as_pydom_tree(self, node: Node):
        children = [self.as_pydom_tree(child) for child in node.children]
        if not children:
            return node.astext()

        component = self.components.get(node.tagname, Fragment) # type: ignore
        return component(*children)

    def get_outfilename(self, pagename: str):
        return self.outdir / f"{pagename}.html"

    def _import_template(self, name: str) -> Component:
        module = None
        try:
            for path in self.config.templates_path:
                module_path = self.confdir / path / f"{name}.py"
                if not module_path.exists():
                    continue
                spec = importlib.util.spec_from_file_location(name, module_path)
                if spec is None:
                    raise ImportError
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module) # type: ignore
        except ImportError:
            pass

        module = module or importlib.import_module(f"pydom_theme.templates.{name}")

        return getattr(module, TEMPLATE_COMPONENTS[name])
