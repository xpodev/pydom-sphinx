from pydom import Component, Div
from pydom.element import Element


class DocsLayout(Component):
    def __init__(self, toctree: Component | Element, section_tree: Component | Element):
        self.toctree = toctree
        self.section_tree = section_tree

    def render(self):
        return Div(class_name="container")(
            Div(class_name="row")(
                Div(class_name="col-3")(
                    self.toctree,
                ),
                Div(
                    class_name="col-6",
                )(
                    *self.children,
                ),
                Div(class_name="col-3")(
                    self.section_tree,
                ),
            ),
        )
