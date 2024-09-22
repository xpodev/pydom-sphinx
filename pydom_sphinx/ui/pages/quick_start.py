from pydom import Component, Div

from ui.components.code_block import CodeBlock
from ui.layout.docs import DocsLayout


class QuickStart(Component):
    def render(self):
      return DocsLayout(section_tree=Div("section tree"), toctree=Div("toctree"))(
          CodeBlock()(
            """from pydom import Component, Div

from ui.components.code_block import CodeBlock
from ui.layout.docs import DocsLayout


class QuickStart(Component):
    def render(self):
      return DocsLayout(section_tree=Div("section tree"), toctree=Div("toctree"))(
          CodeBlock()(
            ""
          )
      )

"""
          )
      )

