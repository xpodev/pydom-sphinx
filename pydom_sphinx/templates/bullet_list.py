from pydom import Ul
from pydom_sphinx import Component


class BulletList(Component):
    def render(self):
        return Ul()(*self.children)
