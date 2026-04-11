# Task Agent Orchestrator

## Overview

This project implements a lightweight agent-based system that processes user tasks, selects appropriate tools, and executes them while providing a transparent execution trace.

The system demonstrates core agentic patterns including:

- Tool selection
- Execution tracing
- Modular architecture

---

## Features

- Task submission via UI
- Agent-based decision making
- Multiple tools (text, calculator, weather mock)
- Execution trace visualization
- Task history persistence

---

## Tech Stack

- Backend: Python (FastAPI)
- Frontend: React
- Storage: SQLite

---

## Project Structure and Architecture

### HLD

The system follows a layered architecture:
![High-Level Diagram](docs/HLD.drawio.png)

### Sequence Diagram

---

## Repository Structure

```bash
agent-task-system/
│
├── backend/
│   ├── app/
│   │   ├── main.py                    # API entry point
│   │   │
│   │   ├── agent/
│   │   │   ├── controller.py          # orchestrator
│   │   │   ├── classifier.py          # desision logic
│   │   │
│   │   ├── tools/
│   │   │   ├── base_tool.py           # interface
│   │   │   ├── text_tool.py
│   │   │   ├── calculator_tool.py
│   │   │   ├── weather_tool.py
│   │   │   └── tool_registry.py
│   │   │
│   │   └── storage/
│   │       ├── storage.py             # interface
│   │       ├── sqlite_storage.py
│   │
│   ├── test/
│   │
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │
│   ├── test/
│   │
│   └── package.json
│
├── docs/
│   ├──HLD.png
│   ├── sequence_diagram.png
│   └── class_diagram.png
│
├── .gitignore
└── README.md

```

---

## Prerquisites

- Python 3.11+
- ***

## How to Run

### Backend

```bash
cd backend

# Virtual environment creation
# Windows users
python -m venv .venv
.venv\Scripts\Activate

# Mac users
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the server
# Windows
$env:PYTHONPATH = "app" ; .venv\Scripts\python.exe -m uvicorn app.main:app --reload

# Mac / Linux
PYTHONPATH=app .venv/bin/uvicorn app.main:app --reload

```

- Server runs at: http://localhost:8000
- Interactive API docs or Swagger: http://localhost:8000/docs

```json
// Post /task
// In Swagger, click "Try it out" then replace the body with one of these and click "Execute"

{ "task": "uppercase: hello world" }
{ "task": "3 + 5" }
{ "task": "weather in Paris" }
{ "task": "count: one two three four" }

// GET /tasks
// In Swagger, click "Try it out" then click "Execute"
// This will return the full history of all tasks saved to the DB

```

### Backend Test

```bash
cd backend/test

# Run unit tests and save the results in a log file
.venv\Scripts\python.exe -m pytest test/test_backend_unit.py -v > test/unit_test_results.log 2>&1

```

### Frontend

```bash
cd frontend

```

### Frontend Test

```bash
cd frontend/test

```

---

## Design Decisions

- Rule-based task classification for simplicity and determinism
- Tool abstraction for extensibility
- Separation of concerns across layers

---

## Future Improvements

- LLM-based task understanding

---
