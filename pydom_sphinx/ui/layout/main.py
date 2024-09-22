from pydom import Component, Div


class MainLayout(Component):
    def render(self):
        return Div(
            id="app",
            class_name="d-flex flex-column vh-100 bg-dark text-light",
        )(
            Div(class_name="py-4 bg-primary")(
                Div(class_name="container mx-auto")(
                    Div(class_name="d-flex justify-content-between")(
                        Div()("{% Logo %}"),
                        Div()("Menu"),
                    )
                )
            ),
            Div(class_name="flex-grow-1 d-flex flex-column overflow-auto")(
                Div(class_name="flex-grow-1")(
                    *self.children,
                ),
                Div(class_name="bg-dark-subtle")(
                    Div(class_name="container py-4 text-white")("Footer"),
                ),
            ),
        )
