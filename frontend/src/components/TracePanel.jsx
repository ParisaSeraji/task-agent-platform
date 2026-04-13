export default function TracePanel({ result }) {
  if (!result?.steps?.length) {
    return (
      <p className="trace-empty">
        Execution steps will appear here after a task runs.
      </p>
    );
  }

  const formatTimestamp = (ts) => {
    if (!ts) return "";
    const d = new Date(ts);
    return d.toLocaleString([], {
      month: "short",
      day: "numeric",
      hour: "2-digit",
      minute: "2-digit",
      second: "2-digit",
    });
  };

  return (
    <div className="trace-steps">
      {result.timestamp && (
        <p className="trace-timestamp">
          Run at: {formatTimestamp(result.timestamp)}
        </p>
      )}
      {result.steps.map((step, i) => (
        <div key={i} className="trace-step">
          <div className="step-dot" />
          <span>{step}</span>
        </div>
      ))}
    </div>
  );
}
