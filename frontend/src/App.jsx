import { useState, useEffect } from "react";
import TaskForm from "./components/TaskForm";
import ResultPanel from "./components/ResultPanel";
import TracePanel from "./components/TracePanel";
import HistoryPanel from "./components/HistoryPanel";
import { submitTask, fetchHistory } from "./api";

export default function App() {
  const [active, setActive] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [history, setHistory] = useState([]);

  const loadHistory = async () => {
    try {
      const data = await fetchHistory();
      setHistory(data.reverse()); // newest first
    } catch {
      // history load failures are non-critical
    }
  };

  useEffect(() => {
    loadHistory();
  }, []);

  const handleSubmit = async (task) => {
    setLoading(true);
    setError(null);
    try {
      const response = await submitTask(task);
      setActive({ ...response, task });
      loadHistory();
    } catch (err) {
      setError("Failed to reach the agent. Is the backend running?");
    } finally {
      setLoading(false);
    }
  };

  const handleSelectHistory = (item) => {
    setActive({
      result: item.result,
      steps: item.steps,
      tool: item.tool,
      task: item.task,
    });
  };

  return (
    <>
      <header className="app-header">
        <div className="logo-dot">B</div>
        <h1>Task Agent</h1>
      </header>

      <main className="app-layout">
        <div className="left-col">
          <div className="card">
            <div className="card-header">Submit a Task</div>
            <div className="card-body">
              <TaskForm
                onSubmit={handleSubmit}
                loading={loading}
                error={error}
              />
            </div>
          </div>

          <div className="card">
            <div className="card-header">Result</div>
            <div className="card-body">
              <ResultPanel result={active} />
            </div>
          </div>

          <div className="card card-full-width">
            <div className="card-header">Execution Trace</div>
            <div className="card-body">
              <TracePanel result={active} />
            </div>
          </div>
        </div>

        <div className="right-col">
          <div className="card">
            <div className="card-header">Task History</div>
            <HistoryPanel
              history={history}
              active={active}
              onSelect={handleSelectHistory}
              onRefresh={loadHistory}
            />
          </div>
        </div>
      </main>
    </>
  );
}
