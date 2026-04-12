from .base_tool import Tool


class WeatherTool(Tool):
    """
    Tool for fetching weather information.
    Extracts city name from task using simple heuristics.
    """

    name = "WeatherTool"

    def can_handle(self, task):
        """Return True if task is related to weather."""

        return "weather" in task.lower()

    def execute(self, task, context=None):
        """Return mock weather response, extracting city from 'in'/'for' preposition."""

        words = task.lower().split()
        city = "Unknown"
        for i, word in enumerate(words):
            if word in ("in", "for") and i + 1 < len(words):
                city = words[i + 1].capitalize()
                break
        return f"{city}: Sunny, 25\u00b0C"
