export default function TracePanel({ result }) {
  if (!result?.steps?.length) {
    return (
      <p className="trace-empty">
        Execution steps will appear here after a task runs.
      </p>
    );
  }

  return (
    <div className="trace-steps">
      {result.steps.map((step, i) => (
        <div key={i} className="trace-step">
          <div className="step-dot" />
          <span>{step}</span>
        </div>
      ))}
    </div>
  );
}
