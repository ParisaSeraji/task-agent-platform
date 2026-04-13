"""
API entry point.

Exposes two endpoints:
  POST /task   - Submit a task for the agent to process.
  GET  /tasks  - Retrieve the full history of processed tasks.
"""

from datetime import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import Controller
from storage.sqlite_storage import SQLiteStorage

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

agent = Controller()
storage = SQLiteStorage()


class TaskRequest(BaseModel):
    """Request body schema for POST /task."""

    task: str


@app.post("/task")
def run_task(payload: TaskRequest):
    """Process a task through the agent and persist the result."""
    response = agent.handle_task(payload.task)
    timestamp = datetime.now().isoformat()
    storage.save(payload.task, response["result"], response["steps"], response.get("tool"), timestamp)
    return {**response, "timestamp": timestamp}


@app.get("/tasks")
def get_tasks():
    """Return all previously processed tasks from storage."""
    return storage.get_all()
