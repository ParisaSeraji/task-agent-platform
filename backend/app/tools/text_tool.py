from .base_tool import Tool

_COMMAND_WORDS = {
    "uppercase",
    "lowercase",
    "count",
    "word",
    "convert",
    "to",
    "make",
    "the",
    "text",
    "me",
    "give",
}


class TextTool(Tool):
    """
    Tool for basic text processing: uppercase, lowercase, word count.
    Supports colon syntax ("uppercase: hello") and natural language ("uppercase hello").
    """

    name = "TextTool"

    def can_handle(self, task):
        """Return True if task contains a recognised text operation keyword."""

        task_lower = task.lower()
        return (
            "uppercase" in task_lower
            or "lowercase" in task_lower
            or "count" in task_lower
        )

    def execute(self, task, context=None):
        """Apply the requested text operation and return the result."""

        task_lower = task.lower()
        text = self._extract_text(task)
        if "uppercase" in task_lower:
            return text.upper()
        if "lowercase" in task_lower:
            return text.lower()
        if "count" in task_lower:
            return str(len(text.split()))
        return "Unknown text operation"

    def _extract_text(self, task):
        """Extract the subject text — after colon if present, otherwise strip command words."""
        if ":" in task:
            return task.split(":", 1)[1].strip()
        words = task.split()
        remaining = [w for w in words if w.lower() not in _COMMAND_WORDS]
        return " ".join(remaining) if remaining else task
