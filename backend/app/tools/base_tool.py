from abc import ABC, abstractmethod


class Tool(ABC):
    """
    Abstract base class for all agent tools.
    Each tool must implement can_handle() and execute().
    """

    name = "base"

    @abstractmethod
    def can_handle(self, task: str) -> bool:
        """Return True if this tool can handle the given task string."""
        pass

    @abstractmethod
    def execute(self, task: str, context=None) -> str:
        """Execute the tool logic and return the result as a string."""
        pass
