export async function submitTask(task) {
  const response = await fetch("/task", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ task }),
  });
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  return response.json();
}

export async function fetchHistory() {
  const response = await fetch("/tasks");
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  return response.json();
}
