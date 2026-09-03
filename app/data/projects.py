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
        title="Insurance Policy RAG Analyzer",
        description=(
            "A document ingestion pipeline that parses insurance policy PDFs "
            "(fine-print exclusions, tables) and answers queries with page-level "
            "source citation, using hybrid retrieval (BM25 + dense embeddings). "
            "Currently in progress — retrieval accuracy and latency benchmarks "
            "are being finalized."
        ),
        tech=["Python", "FastAPI", "pgvector", "Qdrant", "BM25", "RAG", "Ragas"],
        github="https://github.com/anirudh-s1308/policy-rag-engine",
        featured=True,
    ),
    Project(
        title="API & UI Test Automation Framework",
        description=(
            "A test automation framework covering both API and UI test flows, "
            "built with Pytest and Playwright, integrated into a GitHub Actions "
            "CI/CD pipeline for automated regression checks on every push."
        ),
        tech=["Python", "Pytest", "Playwright", "Requests", "GitHub Actions"],
        github="https://github.com/anirudh-s1308/py-test-automation-framework",
        featured=True,
    ),
    Project(
        title="QR Code Generator & Security API",
        description=(
            "Backend routing and IP-based rate limiting for a collaborative QR "
            "code generation service, restructured to prevent request flooding "
            "and support scalable, concurrent request handling."
        ),
        tech=["Python", "FastAPI", "Rate Limiting"],
        github="https://github.com/anirudh-s1308/QRcode-Generator",
        featured=True,
    ),
    Project(
        title="Character Recognition System",
        description=(
            "A PyTorch computer vision pipeline combining CNN feature extractors "
            "with an RNN to recognize handwritten text line by line, with data "
            "augmentation (rotation, scaling, contrast adjustment) via OpenCV."
        ),
        tech=["Python", "PyTorch", "OpenCV", "CNN", "RNN"],
        github="https://github.com/anirudh-s1308/",
        featured=False,
    ),
    Project(
        title="Hybrid log classification",
        description=(
            "A three-tier cascading pipeline that classifies raw application/system "
            "log lines by combining zero-cost regex matching, a fine-tuned "
            "Sentence-BERT + Logistic Regression classifier, and a local LLM "
            "fallback (Ollama) — exposed through a FastAPI service and monitored "
        ),
        tech=["Python", "PyTorch", "NumPy", "Pandas", "Scikit-learn", "Machine Learning", "FastAPI", "Regex"],
        github="https://github.com/anirudh-s1308/log-classification",
        featured=True,
        ),
    Project(
        title="Booking Engine",
        description=(
            "High-throughput ticket reservation engine built with FastAPI, "
            "PostgreSQL, Redis, and RabbitMQ. "
            " Uses pessimistic locking to guarantee zero percent overbooking and Redis"
            " token buckets for distributed rate limiting"
        ),
        tech=["Python", "FastAPI", "PostgreSQL", "Redis", "RabbitMQ"],
        github="https://github.com/anirudh-s1308/booking-engine",
        featured=True,
        ),
    Project(
        title="Suport Agent",
        description=(
            "AI Support Agent: Built an automated customer support agent "
            " using Python and LLMs to process user queries, route tickets,"
            " and generate context-aware responses via REST APIs."
        ),
        tech=["Python", "LLM", "Gemini", "FastAPI"],
        github="https://github.com/anirudh-s1308/support-agent",
        featured=True,
        ),
    Project(
            title="Resume Agent",
            description=(
                "AI Resume Agent: Built an automated resume screening agent "
                " An agent which ranks a set of resumes against a given job "
                " description and outputs an ordered shortlist."
            ),
            tech=["Python", "Gemini", "FastAPI"],
            github="https://github.com/anirudh-s1308/support-agent",
            featured=True,
            ),
]