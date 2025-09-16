document.getElementById("chat-form").addEventListener("submit", async function (e) {
  e.preventDefault();

  const input = document.getElementById("command");
  const command = input.value;
  input.value = "";

  const response = await fetch("/command", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ command })
  });

  const result = await response.json();

  // Show assistant's reply
  const chatBox = document.getElementById("chat-box");
  const msg = document.createElement("p");
  msg.innerHTML = `<b>Assistant:</b> ${result.message || ""}`;
  chatBox.appendChild(msg);

  // ✅ Auto-open website
  if (result.action === "open_url" && result.url) {
      window.open(result.url, "_blank");
  }
});
