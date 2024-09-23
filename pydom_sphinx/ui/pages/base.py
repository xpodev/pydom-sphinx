from pydom import Link, Script
from pydom.page import Page as Base

from ui.layout.main import MainLayout


class Page(Base, title="PyDOM Documentation"):
    def __init__(self, *children, title=None, **kwargs):
        super().__init__(*children)
        self.kwargs = kwargs
        self.title = title
        self._html_props["data-bs-theme"] = "dark" # type: ignore - data-bs-theme is a valid attribute

    def head(self):
        yield from super().head()
        yield Link(
            rel="stylesheet",
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css",
        )
        yield Link(
            rel="stylesheet",
            href="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/styles/hybrid.min.css",
        )
        yield Script(
            src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/highlight.min.js"
        )
        yield Script(
            src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/languages/python.min.js"
        )
        yield Script(
            src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/languages/xml.min.js"
        )
        yield Script(
            src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/languages/javascript.min.js"
        )
        yield Link(
            rel="stylesheet",
            href="/static/css/main.css",
        )

    def body(self):
        return (MainLayout()(*self.children), Script("hljs.highlightAll();"))
