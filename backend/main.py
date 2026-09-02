from fastapi import FastAPI

app = FastAPI(
    title="SafeCross AI Backend",
    description="AI-powered road accident prediction and safety backend",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "SafeCross AI Backend is running",
        "status": "success"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }