from pydom import B
from pydom_sphinx import Component


class Strong(Component):
    def render(self):
        return B()(*self.children)
