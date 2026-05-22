from fastapi import FastAPI

from app.api.auth import router as auth_router

app = FastAPI(
    title="ERTOP API",
    description="Enterprise Red Team Operations Platform API",
    version="1.0.0"
)

app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": "ERTOP Backend Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }