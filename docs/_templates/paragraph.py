from pydom import Component, P

class Paragraph(Component):
    def render(self):
        return P(class_name="card p-2")(*self.children)