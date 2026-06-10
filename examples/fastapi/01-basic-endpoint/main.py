from datetime import datetime

from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Example 01 - Basic Endpoint",
    version="1.0.0",
)


@app.get("/api/v1/health", tags=["Health"])
async def health_check():
    """
    Basic health check endpoint.

    Demonstrates:
    - Route definition
    - JSON response
    - API versioning
    """

    return {
        "status": "success",
        "message": "API is operational",
        "timestamp": datetime.utcnow().isoformat(),
    }
