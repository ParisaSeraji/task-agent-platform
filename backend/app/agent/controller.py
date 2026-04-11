from tools import ToolRegistry


class Controller:
    """
    Agent controller — orchestrates task processing.
    Delegates tool selection to ToolRegistry, executes the tool,
    and builds a transparent execution trace.
    """

    def __init__(self):
        self.registry = ToolRegistry()

    def handle_task(self, task: str):
        """
        Process a task and return result, steps, and tool name.
        Steps list makes the agent's reasoning inspectable by the frontend.
        """

        steps = []

        steps.append(f'Step 1: Received task: "{task}"')

        tool = self.registry.get_tool(task)
        if not tool:
            steps.append("Step 2: No suitable tool found")
            return {"result": "No suitable tool found", "steps": steps, "tool": None}

        steps.append(f"Step 2: Selected tool: {tool.name}")

        result = tool.execute(task)
        steps.append(f"Step 3: Tool result: {result}")

        steps.append("Step 4: Returning result to user")

        return {"result": result, "steps": steps, "tool": tool.name}
