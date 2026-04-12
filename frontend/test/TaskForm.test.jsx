import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, it, expect, vi } from "vitest";
import TaskForm from "../src/components/TaskForm";

describe("TaskForm", () => {
  it("renders the input and submit button", () => {
    render(<TaskForm onSubmit={() => {}} loading={false} />);
    expect(screen.getByRole("textbox")).toBeInTheDocument();
    expect(screen.getByRole("button", { name: /run/i })).toBeInTheDocument();
  });

  it("submit button is disabled when input is empty", () => {
    render(<TaskForm onSubmit={() => {}} loading={false} />);
    expect(screen.getByRole("button", { name: /run/i })).toBeDisabled();
  });

  it("submit button is enabled when input has text", async () => {
    render(<TaskForm onSubmit={() => {}} loading={false} />);
    await userEvent.type(screen.getByRole("textbox"), "uppercase: hello");
    expect(screen.getByRole("button", { name: /run/i })).toBeEnabled();
  });

  it("calls onSubmit with the trimmed input value", async () => {
    const onSubmit = vi.fn();
    render(<TaskForm onSubmit={onSubmit} loading={false} />);
    await userEvent.type(screen.getByRole("textbox"), "  3 + 5  ");
    await userEvent.click(screen.getByRole("button", { name: /run/i }));
    expect(onSubmit).toHaveBeenCalledOnce();
    expect(onSubmit).toHaveBeenCalledWith("3 + 5");
  });

  it("disables input and button while loading", () => {
    render(<TaskForm onSubmit={() => {}} loading={true} />);
    expect(screen.getByRole("textbox")).toBeDisabled();
    expect(screen.getByRole("button")).toBeDisabled();
  });

  it("shows error message when error prop is provided", () => {
    render(
      <TaskForm
        onSubmit={() => {}}
        loading={false}
        error="Failed to reach the agent."
      />,
    );
    expect(screen.getByText(/failed to reach the agent/i)).toBeInTheDocument();
  });

  it("does not call onSubmit when input is only whitespace", async () => {
    const onSubmit = vi.fn();
    render(<TaskForm onSubmit={onSubmit} loading={false} />);
    await userEvent.type(screen.getByRole("textbox"), "   ");
    await userEvent.click(screen.getByRole("button", { name: /run/i }));
    expect(onSubmit).not.toHaveBeenCalled();
  });
});
