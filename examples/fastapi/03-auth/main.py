from fastapi import Depends
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status

from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security import HTTPBearer

app = FastAPI(
    title="FastAPI Example 03 - Authentication",
    version="1.0.0",
)

security = HTTPBearer()


# ------------------------------------------------------------------
# Mock Authentication Service
# ------------------------------------------------------------------

def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    """
    Simulates token validation.

    In real applications this would:
    - Decode JWT
    - Verify signature
    - Check expiration
    - Load user permissions
    """

    valid_token = "my-secret-token"

    if credentials.credentials != valid_token:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={
                "WWW-Authenticate": "Bearer",
            },
        )

    return {
        "user_id": 1,
        "username": "admin",
        "role": "administrator",
    }


# ------------------------------------------------------------------
# Public Route
# ------------------------------------------------------------------

@app.get("/api/v1/public")
async def public_endpoint():

    return {
        "message": "This endpoint is public.",
    }


# ------------------------------------------------------------------
# Protected Route
# ------------------------------------------------------------------

@app.get("/api/v1/protected")
async def protected_endpoint(
    current_user: dict = Depends(verify_token),
):

    return {
        "message": "Protected resource accessed successfully.",
        "user": current_user,
    }
