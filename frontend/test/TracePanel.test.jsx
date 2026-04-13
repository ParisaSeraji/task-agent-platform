import { render, screen } from "@testing-library/react";
import { describe, it, expect } from "vitest";
import TracePanel from "../src/components/TracePanel";

describe("TracePanel", () => {
  it("shows empty state when result is null", () => {
    render(<TracePanel result={null} />);
    expect(screen.getByText(/execution steps/i)).toBeInTheDocument();
  });

  it("shows empty state when steps array is empty", () => {
    render(<TracePanel result={{ steps: [] }} />);
    expect(screen.getByText(/execution steps/i)).toBeInTheDocument();
  });

  it("renders all steps when result has steps", () => {
    const steps = [
      'Step 1: Received task: "uppercase: hello"',
      "Step 2: Selected tool: TextTool",
      "Step 3: Tool result: HELLO",
      "Step 4: Returning result to user",
    ];
    render(<TracePanel result={{ steps }} />);
    steps.forEach((step) => {
      expect(screen.getByText(step)).toBeInTheDocument();
    });
  });

  it("renders the correct number of step elements", () => {
    const steps = ["Step 1", "Step 2", "Step 3"];
    render(<TracePanel result={{ steps }} />);
    expect(document.querySelectorAll(".trace-step")).toHaveLength(3);
  });

  it("shows run timestamp when result has timestamp", () => {
    const steps = ["Step 1"];
    render(<TracePanel result={{ steps, timestamp: "2026-04-12T10:00:00" }} />);
    expect(screen.getByText(/run at/i)).toBeInTheDocument();
  });

  it("does not show run timestamp when timestamp is absent", () => {
    const steps = ["Step 1"];
    render(<TracePanel result={{ steps }} />);
    expect(screen.queryByText(/run at/i)).not.toBeInTheDocument();
  });
});
