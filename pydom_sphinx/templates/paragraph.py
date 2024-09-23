from pydom import P
from pydom_sphinx import Component

class Paragraph(Component):
    def render(self):
        return P(*self.children)