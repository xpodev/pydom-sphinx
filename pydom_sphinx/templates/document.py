from pydom import Link
from ui.pages.base import Page


class Document(Page):
  def head(self):
    yield from super().head()
    yield Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css")
