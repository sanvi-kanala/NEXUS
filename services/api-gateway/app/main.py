from fastapi import FastAPI

app = FastAPI(
    title="NEXUS API Gateway",
    description="Entry point for the NEXUS distributed system",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "service": "api-gateway",
        "project": "NEXUS",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "service": "api-gateway",
        "status": "healthy",
    }