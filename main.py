from fastapi import FastAPI
import time

app = FastAPI()
start_time = time.time()

@app.get("/ping")
async def ping():
    return {"message": "pong"}

@app.get("/health")
async def health():
    uptime = int(time.time() - start_time)
    return {
        "status": "ok",
        "uptime_seconds": uptime
    }

