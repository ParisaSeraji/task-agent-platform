import { render, screen } from "@testing-library/react";
import { describe, it, expect } from "vitest";
import ResultPanel from "../src/components/ResultPanel";

describe("ResultPanel", () => {
  it("shows empty state when result is null", () => {
    render(<ResultPanel result={null} />);
    expect(screen.getByText(/submit a task/i)).toBeInTheDocument();
  });

  it("displays the result value", () => {
    render(
      <ResultPanel
        result={{ result: "HELLO", tool: "TextTool", task: "uppercase: hello" }}
      />,
    );
    expect(screen.getByText("HELLO")).toBeInTheDocument();
  });

  it("displays the tool badge", () => {
    render(
      <ResultPanel
        result={{ result: "HELLO", tool: "TextTool", task: "uppercase: hello" }}
      />,
    );
    expect(screen.getByText("TextTool")).toBeInTheDocument();
  });

  it("displays the task label", () => {
    render(
      <ResultPanel
        result={{ result: "HELLO", tool: "TextTool", task: "uppercase: hello" }}
      />,
    );
    expect(screen.getByText(/uppercase: hello/i)).toBeInTheDocument();
  });
});
