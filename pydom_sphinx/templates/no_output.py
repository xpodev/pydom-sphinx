from pydom_sphinx import Component


class NoOutput(Component):
    def render(self):
        return None
