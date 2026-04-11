from .text_tool import TextTool
from .calculator_tool import CalculatorTool
from .weather_tool import WeatherTool


class ToolRegistry:
    """
    Registry of all available tools.
    Tools are checked in order — specific tools first, general ones last.
    """

    def __init__(self):
        self._tools = [WeatherTool(), CalculatorTool(), TextTool()]

    def get_tool(self, task: str):
        """Return the first tool that can handle the task, or None."""

        for tool in self._tools:
            if tool.can_handle(task):
                return tool
        return None
