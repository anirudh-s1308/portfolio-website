from pydantic import BaseModel
from fastapi import APIRouter, Header, HTTPException, status
from pathlib import Path

router = APIRouter(tags=["Tracking"])

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)
COUNTER_FILE = DATA_DIR / "usage_count.txt"

APP_SECRET = "YOUR_CUSTOM_SECRET_KEY"

if not COUNTER_FILE.exists():
    COUNTER_FILE.write_text("0")

class TrackPayload(BaseModel):
    events_count: int = 1

def increment_count(amount: int = 1) -> int:
    try:
        current = int(COUNTER_FILE.read_text().strip())
    except (ValueError, FileNotFoundError):
        current = 0
        
    new_total = current + max(1, amount)
    COUNTER_FILE.write_text(str(new_total))
    return new_total

@router.post("/api/track")
async def track_usage(
    payload: TrackPayload,
    x_app_secret: str = Header(None)
):
    if x_app_secret != APP_SECRET:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized"
        )
    
    new_total = increment_count(payload.events_count)
    return {"status": "success", "count": new_total}