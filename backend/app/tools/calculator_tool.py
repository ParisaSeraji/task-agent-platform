import re
from .base_tool import Tool

_OP_MAP = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}


class CalculatorTool(Tool):
    """
    Tool for single-operation arithmetic (+, -, *, /).
    Extracts two operands and one operator via regex.
    """

    name = "CalculatorTool"

    def can_handle(self, task):
        """Return True if task contains a recognised arithmetic operator."""

        return any(op in task for op in _OP_MAP)

    def execute(self, task, context=None):
        """Parse and evaluate the arithmetic expression. Returns error string on failure."""

        match = re.search(r"(-?[\d.]+)\s*([+\-*/])\s*(-?[\d.]+)", task)
        if not match:
            return "Invalid expression"
        a, op, b = float(match.group(1)), match.group(2), float(match.group(3))
        if op == "/" and b == 0:
            return "Division by zero"
        result = _OP_MAP[op](a, b)
        return str(int(result) if result == int(result) else result)
