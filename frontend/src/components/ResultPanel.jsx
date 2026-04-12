export default function ResultPanel({ result }) {
  if (!result) {
    return (
      <p className="result-empty">Submit a task to see the result here.</p>
    );
  }

  return (
    <div>
      {result.tool && <span className="result-tool-badge">{result.tool}</span>}
      <div className="result-value">{result.result}</div>
      <p className="result-task-label">Task: "{result.task}"</p>
    </div>
  );
}
