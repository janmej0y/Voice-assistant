async function sendMessage() {
    let input = document.getElementById("command");
    let userMsg = input.value.trim();
    if (!userMsg) return;
  
    let chatBox = document.getElementById("chat");
    chatBox.innerHTML += `<p><b>You:</b> ${userMsg}</p>`;
  
    let res = await fetch("/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ command: userMsg })
    });
    let data = await res.json();
  
    let botReply = data.response;
    chatBox.innerHTML += `<p><b>Assistant:</b> ${botReply}</p>`;
    chatBox.scrollTop = chatBox.scrollHeight;
    input.value = "";
  
    // 🔊 Speak the response using browser TTS
    let utterance = new SpeechSynthesisUtterance(botReply);
    utterance.lang = "en-US";
    speechSynthesis.speak(utterance);
  }
  
  document.getElementById("sendBtn").addEventListener("click", sendMessage);
  document.getElementById("command").addEventListener("keypress", function(e) {
    if (e.key === "Enter") sendMessage();
  });
  
  // 🎤 Voice recognition
  document.getElementById("voiceBtn").addEventListener("click", () => {
    let recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = "en-US";
    recognition.start();
  
    recognition.onresult = function(event) {
      let voiceInput = event.results[0][0].transcript;
      document.getElementById("command").value = voiceInput;
      sendMessage();
    };
  });
  