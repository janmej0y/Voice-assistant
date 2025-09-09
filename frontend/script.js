const chatBox = document.getElementById("chat-box");
const input = document.getElementById("command");
const button = document.getElementById("send");
const voiceButton = document.getElementById("voice");

function appendMessage(sender, message) {
    const msg = document.createElement("p");
    msg.innerHTML = `<b>${sender}:</b> ${message}`;
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
}

button.addEventListener("click", async () => {
    const text = input.value;
    if (!text) return;

    appendMessage("You", text);
    input.value = "";

    const res = await fetch("/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: text })
    });
    const data = await res.json();
    appendMessage("Assistant", data.response);

    // Assistant voice reply
    const utter = new SpeechSynthesisUtterance(data.response);
    speechSynthesis.speak(utter);
});

// 🎤 Voice input
voiceButton.addEventListener("click", () => {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = "en-US";
    recognition.start();

    recognition.onresult = (event) => {
        const spokenText = event.results[0][0].transcript;
        input.value = spokenText;
        button.click();
    };
});
