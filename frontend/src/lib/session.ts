let lastActivityTime = Date.now();

export function setupSessionTracking(updateStatus: (status: string) => void) {
  ["mousemove", "keydown", "touchstart"].forEach(evt =>
    document.addEventListener(evt, () => {
      lastActivityTime = Date.now();
    })
  );

  // Periodically ping backend
  setInterval(() => {
    const now = Date.now();
    if (now - lastActivityTime < 1000) {
      fetch("http://localhost:8000/session/ping", { method: "POST" });
    }
  }, 1000);

  // Check session expiration
  setInterval(() => {
    fetch("http://localhost:8000/session/check")
      .then(res => res.json())
      .then(data => updateStatus(data.status));
  }, 1000);
}
