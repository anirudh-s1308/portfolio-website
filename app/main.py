from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import home, projects, contacts

app = FastAPI(docs_url=None, redoc_url=None)  # hide API docs for portfolio

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(home.router)
app.include_router(projects.router)
app.include_router(contacts.router)