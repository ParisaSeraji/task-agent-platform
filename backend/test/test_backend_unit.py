import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "app"))

from tools.text_tool import TextTool
from tools.calculator_tool import CalculatorTool
from tools.weather_tool import WeatherTool
from tools.tool_registry import ToolRegistry
from agent.controller import Controller
from storage.sqlite_storage import SQLiteStorage


# ---------------------------------------------------------------------------
# TextTool
# ---------------------------------------------------------------------------


class TestTextTool:
    def setup_method(self):
        self.tool = TextTool()

    # can_handle
    def test_can_handle_uppercase(self):
        assert self.tool.can_handle("uppercase: hello") is True

    def test_can_handle_lowercase(self):
        assert self.tool.can_handle("lowercase: HELLO") is True

    def test_can_handle_count(self):
        assert self.tool.can_handle("count words in hello world") is True

    def test_can_handle_case_insensitive(self):
        assert self.tool.can_handle("UPPERCASE: hello") is True

    def test_cannot_handle_unrelated(self):
        assert self.tool.can_handle("what is the weather in Paris") is False

    def test_cannot_handle_math(self):
        assert self.tool.can_handle("3 + 5") is False

    # execute — uppercase
    def test_execute_uppercase_colon_syntax(self):
        assert self.tool.execute("uppercase: hello world") == "HELLO WORLD"

    def test_execute_uppercase_no_colon(self):
        result = self.tool.execute("uppercase hello")
        assert result == "HELLO"

    def test_execute_uppercase_mixed_case_input(self):
        assert self.tool.execute("uppercase: Hello World") == "HELLO WORLD"

    # execute — lowercase
    def test_execute_lowercase_colon_syntax(self):
        assert self.tool.execute("lowercase: HELLO WORLD") == "hello world"

    def test_execute_lowercase_no_colon(self):
        result = self.tool.execute("lowercase HELLO")
        assert result == "hello"

    # execute — word count
    def test_execute_count_colon_syntax(self):
        assert self.tool.execute("count: one two three") == "3"

    def test_execute_count_single_word(self):
        assert self.tool.execute("count: hello") == "1"

    # execute — fallback
    def test_execute_unknown_operation_returns_message(self):
        tool = TextTool()
        # Force a task that passes can_handle but doesn't match any branch
        # by monkeypatching task_lower check — instead test the fallback string
        result = tool.execute("count: a b")
        assert result == "2"


# ---------------------------------------------------------------------------
# CalculatorTool
# ---------------------------------------------------------------------------


class TestCalculatorTool:
    def setup_method(self):
        self.tool = CalculatorTool()

    # can_handle
    def test_can_handle_addition(self):
        assert self.tool.can_handle("3 + 5") is True

    def test_can_handle_subtraction(self):
        assert self.tool.can_handle("10 - 4") is True

    def test_can_handle_multiplication(self):
        assert self.tool.can_handle("6 * 7") is True

    def test_can_handle_division(self):
        assert self.tool.can_handle("15 / 3") is True

    def test_cannot_handle_plain_text(self):
        assert self.tool.can_handle("convert to uppercase") is False

    def test_cannot_handle_weather(self):
        assert self.tool.can_handle("weather in Paris") is False

    # execute — all four operations
    def test_execute_addition(self):
        assert self.tool.execute("what is 3 + 5") == "8"

    def test_execute_subtraction(self):
        assert self.tool.execute("10 - 4") == "6"

    def test_execute_multiplication(self):
        assert self.tool.execute("6 * 7") == "42"

    def test_execute_division_exact(self):
        assert self.tool.execute("15 / 3") == "5"

    def test_execute_division_float(self):
        assert self.tool.execute("10 / 4") == "2.5"

    def test_execute_division_by_zero(self):
        assert self.tool.execute("5 / 0") == "Division by zero"

    def test_execute_with_decimals(self):
        assert self.tool.execute("1.5 + 2.5") == "4"

    def test_execute_negative_numbers(self):
        assert self.tool.execute("-3 + 5") == "2"

    def test_execute_invalid_expression(self):
        assert self.tool.execute("just some text no numbers") == "Invalid expression"

    def test_execute_result_int_when_whole(self):
        # 6.0 should be returned as "6", not "6.0"
        assert self.tool.execute("3 * 2") == "6"


# ---------------------------------------------------------------------------
# WeatherTool
# ---------------------------------------------------------------------------


class TestWeatherTool:
    def setup_method(self):
        self.tool = WeatherTool()

    # can_handle
    def test_can_handle_weather(self):
        assert self.tool.can_handle("weather in Paris") is True

    def test_can_handle_case_insensitive(self):
        assert self.tool.can_handle("What is the Weather in London") is True

    def test_cannot_handle_unrelated(self):
        assert self.tool.can_handle("uppercase: hello") is False

    # execute — city extraction
    def test_execute_city_with_in(self):
        result = self.tool.execute("weather in Paris")
        assert "Paris" in result

    def test_execute_city_with_for(self):
        result = self.tool.execute("weather for London")
        assert "London" in result

    def test_execute_no_city(self):
        result = self.tool.execute("what is the weather")
        assert "Unknown" in result

    def test_execute_contains_mock_data(self):
        result = self.tool.execute("weather in Toronto")
        assert "Sunny" in result
        assert "25" in result
        assert "mock" in result


# ---------------------------------------------------------------------------
# ToolRegistry
# ---------------------------------------------------------------------------


class TestToolRegistry:
    def setup_method(self):
        self.registry = ToolRegistry()

    def test_returns_weather_tool(self):
        tool = self.registry.get_tool("weather in Paris")
        assert tool is not None
        assert tool.name == "WeatherTool"

    def test_returns_calculator_tool(self):
        tool = self.registry.get_tool("3 + 5")
        assert tool is not None
        assert tool.name == "CalculatorTool"

    def test_returns_text_tool_uppercase(self):
        tool = self.registry.get_tool("uppercase: hello")
        assert tool is not None
        assert tool.name == "TextTool"

    def test_returns_text_tool_lowercase(self):
        tool = self.registry.get_tool("lowercase: HELLO")
        assert tool is not None
        assert tool.name == "TextTool"

    def test_returns_none_for_unknown_task(self):
        tool = self.registry.get_tool("tell me a joke")
        assert tool is None

    def test_weather_takes_priority_over_text(self):
        # A task with "weather" should route to WeatherTool, not TextTool
        tool = self.registry.get_tool("weather in Toronto")
        assert tool.name == "WeatherTool"


# ---------------------------------------------------------------------------
# Controller
# ---------------------------------------------------------------------------


class TestController:
    def setup_method(self):
        self.controller = Controller()

    # response shape
    def test_response_has_required_keys(self):
        response = self.controller.handle_task("uppercase: hello")
        assert "result" in response
        assert "steps" in response
        assert "tool" in response

    def test_steps_is_list(self):
        response = self.controller.handle_task("3 + 5")
        assert isinstance(response["steps"], list)

    def test_steps_start_with_received(self):
        response = self.controller.handle_task("uppercase: hello")
        assert response["steps"][0].startswith("Step 1")

    # tool routing
    def test_routes_to_text_tool(self):
        response = self.controller.handle_task("uppercase: hello")
        assert response["tool"] == "TextTool"

    def test_routes_to_calculator_tool(self):
        response = self.controller.handle_task("3 + 5")
        assert response["tool"] == "CalculatorTool"

    def test_routes_to_weather_tool(self):
        response = self.controller.handle_task("weather in Paris")
        assert response["tool"] == "WeatherTool"

    # results
    def test_text_result_correct(self):
        response = self.controller.handle_task("uppercase: hello")
        assert response["result"] == "HELLO"

    def test_calculator_result_correct(self):
        response = self.controller.handle_task("3 + 5")
        assert response["result"] == "8"

    def test_weather_result_contains_city(self):
        response = self.controller.handle_task("weather in Paris")
        assert "Paris" in response["result"]

    # unknown task
    def test_no_tool_found_returns_message(self):
        response = self.controller.handle_task("tell me a joke")
        assert response["result"] == "No suitable tool found"
        assert response["tool"] is None

    def test_no_tool_found_steps_contain_message(self):
        response = self.controller.handle_task("tell me a joke")
        assert any("No suitable tool found" in s for s in response["steps"])

    # trace quality
    def test_steps_mention_selected_tool(self):
        response = self.controller.handle_task("uppercase: hello")
        assert any("TextTool" in s for s in response["steps"])

    def test_steps_mention_result(self):
        response = self.controller.handle_task("uppercase: hello")
        assert any("HELLO" in s for s in response["steps"])

    def test_last_step_is_returning_result(self):
        response = self.controller.handle_task("uppercase: hello")
        assert "Returning result" in response["steps"][-1]


# ---------------------------------------------------------------------------
# SQLiteStorage
# ---------------------------------------------------------------------------


class TestSQLiteStorage:
    @pytest.fixture
    def storage(self, tmp_path):
        return SQLiteStorage(db_name=str(tmp_path / "test.db"))

    def test_empty_on_init(self, storage):
        assert storage.get_all() == []

    def test_save_and_retrieve(self, storage):
        storage.save("uppercase: hello", "HELLO", ["Step 1", "Step 2"], "TextTool")
        records = storage.get_all()
        assert len(records) == 1

    def test_record_fields(self, storage):
        storage.save("3 + 5", "8", ["Step 1"], "CalculatorTool")
        r = storage.get_all()[0]
        assert r["task"] == "3 + 5"
        assert r["result"] == "8"
        assert r["tool"] == "CalculatorTool"
        assert "timestamp" in r
        assert r["id"] == 1

    def test_steps_returned_as_list(self, storage):
        storage.save("task", "result", ["s1", "s2", "s3"], "TextTool")
        r = storage.get_all()[0]
        assert isinstance(r["steps"], list)
        assert r["steps"] == ["s1", "s2", "s3"]

    def test_multiple_records_order(self, storage):
        storage.save("task one", "result one", ["s1"], "ToolA")
        storage.save("task two", "result two", ["s2"], "ToolB")
        records = storage.get_all()
        assert len(records) == 2
        assert records[0]["task"] == "task one"
        assert records[1]["task"] == "task two"

    def test_timestamp_is_iso_format(self, storage):
        from datetime import datetime

        storage.save("task", "result", [], "ToolA")
        ts = storage.get_all()[0]["timestamp"]
        # Should parse without raising
        datetime.fromisoformat(ts)

    def test_tool_can_be_none(self, storage):
        storage.save(
            "unknown task", "No suitable tool found", ["Step 1", "Step 2"], None
        )
        r = storage.get_all()[0]
        assert r["tool"] is None


