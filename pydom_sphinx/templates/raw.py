from pydom import Fragment
from pydom_sphinx import Component


class Raw(Component):
    def render(self):
        return Fragment(dangerously_set_inner_html={"__html": self.children[0]})
