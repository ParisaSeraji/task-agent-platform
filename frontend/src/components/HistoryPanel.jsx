export default function HistoryPanel({ history, active, onSelect, onRefresh }) {
  if (!history.length) {
    return (
      <div className="card-body">
        <p className="history-empty">
          No tasks yet. Submit one to get started.
        </p>
      </div>
    );
  }

  const formatTime = (ts) => {
    if (!ts) return "";
    const d = new Date(ts);
    return d.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
  };

  return (
    <>
      <div className="history-list">
        {history.map((item) => (
          <div
            key={item.id}
            className={`history-item ${active?.task === item.task ? "active" : ""}`}
            onClick={() => onSelect(item)}
          >
            <span className="history-task" title={item.task}>
              {item.task}
            </span>
            <div className="history-meta">
              {item.tool && <span className="history-tool">{item.tool}</span>}
              <span className="history-time">{formatTime(item.timestamp)}</span>
            </div>
          </div>
        ))}
      </div>
      <div className="history-refresh">
        <button className="btn-refresh" onClick={onRefresh}>
          ↻ Refresh
        </button>
      </div>
    </>
  );
}
