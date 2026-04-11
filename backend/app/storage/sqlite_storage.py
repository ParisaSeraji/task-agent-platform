import sqlite3
import json
from datetime import datetime
from .storage import Storage


class SQLiteStorage(Storage):
    """
    SQLite-backed storage. Steps are JSON-serialised for storage
    and deserialised on retrieval so callers always receive a Python list.
    """

    def __init__(self, db_name="tasks.db"):
        """Open (or create) the database and ensure the tasks table exists."""

        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self._create_table()

    def _create_table(self):
        """Create the tasks table if it does not already exist."""

        query = """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT,
            result TEXT,
            steps TEXT,
            tool TEXT,
            timestamp TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def save(self, task, result, steps, tool):
        """Insert a new task record. Steps list is JSON-serialised."""

        query = """
        INSERT INTO tasks (task, result, steps, tool, timestamp)
        VALUES (?, ?, ?, ?, ?)
        """
        self.conn.execute(
            query, (task, result, json.dumps(steps), tool, datetime.now().isoformat())
        )
        self.conn.commit()

    def get_all(self):
        """Return all records with steps deserialised back to a Python list."""

        cursor = self.conn.execute("SELECT * FROM tasks")
        rows = []
        for row in cursor.fetchall():
            r = dict(row)
            r["steps"] = json.loads(r["steps"])
            rows.append(r)
        return rows
