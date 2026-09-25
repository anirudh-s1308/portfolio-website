import sys
from datetime import datetime
from fastapi import APIRouter, Header, HTTPException, status
from pydantic import BaseModel

router = APIRouter(tags=["Tracking"])

PING_SECRET = "YOUR_CUSTOM_SECRET_KEY"


class PingPayload(BaseModel):
    docs_modified: int = 1


@router.post("/api/ping")
async def log_paper_app_usage(
    payload: PingPayload,
    x_ping_secret: str = Header(None),
):
    if x_ping_secret != PING_SECRET:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized",
        )

    timestamp = datetime.utcnow().isoformat()
    log_entry = (
        f"[PAPER_APP_TELEMETRY] App executed at {timestamp} "
        f"| Modified {payload.docs_modified} document(s)"
    )
    print(log_entry, flush=True)
    sys.stdout.flush()

    return {"status": "logged", "received_count": payload.docs_modified}