from fastapi import APIRouter

router = APIRouter()


@router.get("/google")
async def google_login():
    """Redirect to Google OAuth (placeholder)."""
    return {"url": "https://accounts.google.com/o/oauth2/v2/auth"}


@router.get("/google/callback")
async def google_callback(code: str):
    """Handle Google OAuth callback (placeholder)."""
    return {"code": code}
