from fastapi import FastAPI

app = FastAPI(title="Docker Learning API")

@app.get("/")
def home():
    return {
        "message": "My first Dockerized application",
        "status": "running"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/tasks")
def tasks():
    return {
        "tasks": [
            "Learn Docker images",
            "Understand containers",
            "Practice Docker Compose"
        ]
    }
