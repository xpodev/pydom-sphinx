from pathlib import Path

from fastapi.staticfiles import StaticFiles

from app import app
from ui.pages.home import Home
from ui.pages.quick_start import QuickStart

CWD = Path.cwd()

@app.get("/")
def home():
    return Home()

@app.get("/quick-start")
def foo():
    return QuickStart()

@app.get("/foo/bar")
def bar():
    return Home()

app.mount("/static", StaticFiles(directory="_static"), name="static")