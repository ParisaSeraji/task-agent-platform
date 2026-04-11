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

- Python
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

pip install -r requirements.txt

```

### Backend Test

```bash
cd backend/test

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
