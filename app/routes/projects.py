from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.data.projects import PROJECTS

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/projects")
def projects(request: Request):
    return templates.TemplateResponse(
        request,
        "projects.html",
        {"projects": PROJECTS},
    )
