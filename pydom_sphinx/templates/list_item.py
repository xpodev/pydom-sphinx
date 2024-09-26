from pydom import Li
from pydom_sphinx import Component


class ListItem(Component):
    def render(self):
        return Li()(*self.children)
