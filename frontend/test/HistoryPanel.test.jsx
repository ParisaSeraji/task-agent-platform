import { describe, it, expect, vi } from "vitest";
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import HistoryPanel from "../src/components/HistoryPanel";

const mockHistory = [
  {
    id: 1,
    task: "what is 2+2",
    result: "4",
    steps: ["Analyzed task", "Used calculator"],
    tool: "calculator",
    timestamp: "2026-04-12T10:00:00",
  },
  {
    id: 2,
    task: "hello world",
    result: "Hello, World!",
    steps: ["Analyzed task"],
    tool: "text",
    timestamp: "2026-04-12T11:30:00",
  },
];

describe("HistoryPanel", () => {
  it("shows empty state when history is empty", () => {
    render(
      <HistoryPanel
        history={[]}
        active={null}
        onSelect={vi.fn()}
        onRefresh={vi.fn()}
      />,
    );
    expect(screen.getByText(/no tasks yet/i)).toBeInTheDocument();
  });

  it("renders all history items", () => {
    render(
      <HistoryPanel
        history={mockHistory}
        active={null}
        onSelect={vi.fn()}
        onRefresh={vi.fn()}
      />,
    );
    expect(screen.getByText("what is 2+2")).toBeInTheDocument();
    expect(screen.getByText("hello world")).toBeInTheDocument();
  });

  it("calls onSelect with the clicked item", async () => {
    const onSelect = vi.fn();
    render(
      <HistoryPanel
        history={mockHistory}
        active={null}
        onSelect={onSelect}
        onRefresh={vi.fn()}
      />,
    );
    await userEvent.click(screen.getByText("what is 2+2"));
    expect(onSelect).toHaveBeenCalledWith(mockHistory[0]);
  });

  it("marks the active item with the active class", () => {
    const active = { task: "hello world" };
    const { container } = render(
      <HistoryPanel
        history={mockHistory}
        active={active}
        onSelect={vi.fn()}
        onRefresh={vi.fn()}
      />,
    );
    const items = container.querySelectorAll(".history-item");
    expect(items[0]).not.toHaveClass("active");
    expect(items[1]).toHaveClass("active");
  });

  it("calls onRefresh when the refresh button is clicked", async () => {
    const onRefresh = vi.fn();
    render(
      <HistoryPanel
        history={mockHistory}
        active={null}
        onSelect={vi.fn()}
        onRefresh={onRefresh}
      />,
    );
    await userEvent.click(screen.getByText(/refresh/i));
    expect(onRefresh).toHaveBeenCalled();
  });
});
