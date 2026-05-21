from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.data.projects import PROJECTS

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/")
def home(request: Request):
    featured = [p for p in PROJECTS if p.featured]
    return templates.TemplateResponse(
        request,
        "home.html",
        {"featured_projects": featured},
    )
