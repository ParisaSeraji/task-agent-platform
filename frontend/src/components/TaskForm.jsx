import { useState } from "react";

export default function TaskForm({ onSubmit, loading, error }) {
  const [value, setValue] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (value.trim()) onSubmit(value.trim());
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className="task-form">
        <input
          className="task-input"
          type="text"
          placeholder='e.g. "uppercase: hello"  or  "3 + 5"  or  "weather in Paris"'
          value={value}
          onChange={(e) => setValue(e.target.value)}
          disabled={loading}
        />
        <button
          className="btn-submit"
          type="submit"
          disabled={loading || !value.trim()}
        >
          {loading ? "Running…" : "Run"}
        </button>
      </div>
      {error && <p className="error-msg">{error}</p>}
      <p className="task-hint">
        Try: "lowercase: HELLO WORLD" · "15 / 3" · "weather in Toronto"
      </p>
    </form>
  );
}
