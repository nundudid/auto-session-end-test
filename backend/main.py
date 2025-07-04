from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta
from typing import Dict
from fastapi.responses import JSONResponse

app = FastAPI()

# Allow Svelte frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Change to your frontend port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Session activity in memory
session_activity: Dict[str, datetime] = {}

@app.post("/session/ping")
async def ping_session():
    session_activity["child1"] = datetime.utcnow()
    return {"status": "ping received"}

@app.get("/session/check")
async def check_session():
    last_active = session_activity.get("child1")
    now = datetime.utcnow()
    if not last_active or now - last_active > timedelta(seconds=10):
        return JSONResponse({"status": "expired"})
    return {"status": "active"}
