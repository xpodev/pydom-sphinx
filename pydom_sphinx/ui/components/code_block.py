from typing import Optional
from pydom import Code, Component, Div, Pre, Script
from pydom.utils.functions import random_string


class CodeBlock(Component):
    def __init__(self, language: Optional[str] = None):
        self.language = language
        self.id = random_string(8)

    def render(self):
        return Div(class_name="code-block")(
            Div(class_name="code-block-header")(
                Div(class_name="code-block-language")(
                    self.language,
                ),
            ),
            Div(class_name="code-block-body")(
                Pre(
                    Code(
                        id=self.id,
                        class_name=(
                            f"language-{self.language}" if self.language else None
                        ),
                    )(
                        *self.children,
                    ),
                )
            ),
            Script(
                f"hljs.highlightElement(document.getElementById('{self.id}'))",
            ),
        )
