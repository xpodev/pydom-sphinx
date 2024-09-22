from pathlib import Path
import shutil

from pydom import Component, render
from pydom.element import Element
from pydom.page import Page as PydomPage

from app import app
import routing
from ui.pages.base import Page

ROOT = Path.cwd()


def create_file(path: str):
    if path.endswith("/"):
        path += "index"

    file = Path(path + ".html")
    if file.parent == ROOT:
        return file
    
    file.parent.mkdir(parents=True, exist_ok=True)

    if file.parent.with_suffix(".html").exists():
        shutil.move(file.parent.with_suffix(".html"), file.parent / "index.html")

    return file


def build_static_page(route):
    endpoint = route.endpoint
    try:
        page = endpoint()
    except Exception:
        return

    if not isinstance(page, (Component, Element)):
        return
    
    if not isinstance(page, (Page, PydomPage)):
        page = Page()(page)

    path = f"build/{route.path}"
    file = create_file(path)
    with file.open("w") as f:
        f.write(render(page))


if __name__ == "__main__":
    for route in app.routes:
        build_static_page(route)
