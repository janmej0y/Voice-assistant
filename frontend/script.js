// Function to append messages in chat box
function appendMessage(sender, text) {
    let chatBox = document.getElementById("chatBox");
    let msgDiv = document.createElement("div");
    msgDiv.className = "message " + (sender === "You" ? "user" : "assistant");
    msgDiv.textContent = text;
    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight; // auto-scroll to bottom
  }
  
  // Ask assistant (API call)
  async function askAssistant(msg = null) {
    let text = msg || document.getElementById("message").value;
    if (!text) return;
  
    appendMessage("You", text);
    document.getElementById("message").value = "";
  
    let res = await fetch("http://127.0.0.1:5000/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text })
    });
  
    let data = await res.json();
    appendMessage("Assistant", data.response);
  
    // Speak response aloud
    let speech = new SpeechSynthesisUtterance(data.response);
    window.speechSynthesis.speak(speech);
  }
  
  // Voice recognition setup
  let recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
  recognition.lang = "en-US";
  recognition.continuous = false;
  
  function startListening() {
    recognition.start();
  }
  
  recognition.onresult = function(event) {
    let userText = event.results[0][0].transcript;
    document.getElementById("message").value = userText;
    askAssistant(userText);
  };
  