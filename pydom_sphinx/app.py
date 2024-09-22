from fastapi import FastAPI
from fastapi.encoders import encoders_by_class_tuples
from fastapi.responses import HTMLResponse
from pydom import Component, render as pydom_render
from pydom.element import Element
from pydom.page import Page as PydomPage

from ui.pages.base import Page

def render(renderable):
    if not isinstance(renderable, (PydomPage, Page)):
        renderable = Page()(renderable)

    return pydom_render(renderable)

# This is a workaround to make FastAPI use pydom's render function to render pydom elements.
encoders_by_class_tuples[render] = (Component, Element)

app = FastAPI(default_response_class=HTMLResponse, openapi_url=None)
