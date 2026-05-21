from pydantic import BaseModel, HttpUrl
from typing import Optional


class Project(BaseModel):
    title: str
    description: str
    tech: list[str]
    github: str
    live: Optional[str] = None
    featured: bool = False  # show on home page carousel


PROJECTS: list[Project] = [
    Project(
        title="FastAPI Auth Service",
        description="A production-ready JWT authentication microservice with refresh tokens, role-based access control, and Redis session management.",
        tech=["Python", "FastAPI", "Redis", "PostgreSQL"],
        github="https://github.com/you/auth-service",
        live="https://auth-service.example.com",
        featured=True,
    ),
    Project(
        title="Real-time Chat App",
        description="WebSocket-powered chat with rooms, presence indicators, and message persistence. Handles 1000+ concurrent users.",
        tech=["Python", "FastAPI", "WebSockets", "SQLite"],
        github="https://github.com/you/chat-app",
        featured=True,
    ),
    Project(
        title="CLI Data Pipeline",
        description="A composable ETL pipeline for transforming and loading CSV/JSON data into multiple targets with configurable transforms.",
        tech=["Python", "Typer", "Pandas", "Pydantic"],
        github="https://github.com/you/data-pipeline",
        live="https://pypi.org/project/data-pipeline",
        featured=True,
    ),
    Project(
        title="Portfolio Site",
        description="This very site. Built with FastAPI + Jinja2, static data, no database, deployed on Railway.",
        tech=["Python", "FastAPI", "Jinja2", "Railway"],
        github="https://github.com/you/portfolio",
        live="https://yourname.dev",
        featured=True,
    ),
    Project(
        title="Markdown Blog Engine",
        description="A flat-file blog engine that parses Markdown files with frontmatter, generates slugs, and serves syntax-highlighted posts.",
        tech=["Python", "FastAPI", "Markdown", "Pygments"],
        github="https://github.com/you/blog-engine",
        featured=True,
    ),
    Project(
        title="Expense Tracker API",
        description="RESTful API for personal finance tracking with category tagging, monthly summaries, and CSV export.",
        tech=["Python", "FastAPI", "SQLAlchemy", "SQLite"],
        github="https://github.com/you/expense-tracker",
        featured=True,
    ),
    Project(
        title="DNS Lookup Tool",
        description="A fast async DNS resolver CLI and REST API that queries multiple record types and visualises propagation.",
        tech=["Python", "asyncio", "dnspython", "Rich"],
        github="https://github.com/you/dns-tool",
    ),
    Project(
        title="Image Resizer Lambda",
        description="Serverless image resizing on AWS Lambda triggered by S3 uploads. Supports WebP conversion and thumbnail generation.",
        tech=["Python", "AWS Lambda", "Pillow", "S3"],
        github="https://github.com/you/image-resizer",
    ),
]
