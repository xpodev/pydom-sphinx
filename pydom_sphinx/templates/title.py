from pydom import H1
from pydom_sphinx import Component


class Title(Component):
    def render(self):
        return H1(*self.children)
