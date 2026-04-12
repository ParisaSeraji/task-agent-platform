import { useState } from "react";
import TaskForm from "./components/TaskForm";
import ResultPanel from "./components/ResultPanel";
import { submitTask } from "./api";

export default function App() {
  const [active, setActive] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (task) => {
    setLoading(true);
    setError(null);
    try {
      const response = await submitTask(task);
      setActive({ ...response, task });
    } catch (err) {
      setError("Failed to reach the agent. Is the backend running?");
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <header className="app-header">
        <div className="logo-dot">B</div>
        <h1>Task Agent</h1>
      </header>

      <main className="app-layout">
        <div className="card">
          <div className="card-header">Submit a Task</div>
          <div className="card-body">
            <TaskForm onSubmit={handleSubmit} loading={loading} error={error} />
          </div>
        </div>

        <div className="card">
          <div className="card-header">Result</div>
          <div className="card-body">
            <ResultPanel result={active} />
          </div>
        </div>
      </main>
    </>
  );
}
