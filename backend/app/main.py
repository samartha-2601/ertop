from fastapi import FastAPI

app = FastAPI(
    title="ERTOP API",
    description="Enterprise Red Team Operations Platform API",
    version="1.0.0"
)

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