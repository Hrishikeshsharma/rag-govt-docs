from fastapi import FastAPI
from app.api.ingest import router
app = FastAPI()

app.include_router(router, prefix="/api")

@app.get("/api-health")
def health():
    return {"status":"ok"}
