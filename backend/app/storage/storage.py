from abc import ABC, abstractmethod


class Storage(ABC):
    """Abstract base class for storage backends. Swap implementations without changing the rest of the system."""

    @abstractmethod
    def save(self, task, result, steps, tool, timestamp):
        """Persist a completed task and its execution details."""
        pass

    @abstractmethod
    def get_all(self):
        """Return all stored task records as a list of dicts."""
        pass
