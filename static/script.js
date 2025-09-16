document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("chat-form");
  const input = document.getElementById("command");
  const chatBox = document.getElementById("chat-box");
  const micBtn = document.getElementById("mic-btn");

  // 🛡️ Ask for microphone access when page loads
  async function requestMicPermission() {
      try {
          await navigator.mediaDevices.getUserMedia({ audio: true });
          console.log("✅ Microphone permission granted");
      } catch (err) {
          console.warn("❌ Microphone access denied:", err);
          alert("Please allow microphone access to use voice commands.");
          micBtn.disabled = true;
      }
  }
  requestMicPermission();

  // 🎤 Voice Recognition setup
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  let recognition;

  if (SpeechRecognition) {
      recognition = new SpeechRecognition();
      recognition.continuous = false;
      recognition.interimResults = false;
      recognition.lang = "en-US";

      recognition.onresult = (event) => {
          const transcript = event.results[0][0].transcript;
          input.value = transcript;
          form.requestSubmit(); // auto-submit after speaking
      };

      recognition.onerror = (event) => {
          console.error("Speech recognition error:", event.error);
      };
  } else {
      micBtn.style.display = "none"; // hide if not supported
  }

  // 🎤 Mic button click
  micBtn.addEventListener("click", () => {
      if (recognition) {
          recognition.start();
      } else {
          alert("Speech Recognition not supported in this browser.");
      }
  });

  // 📝 Chat form submit
  form.addEventListener("submit", async (e) => {
      e.preventDefault();
      const command = input.value.trim();
      if (!command) return;

      // Display user message
      const userMsg = document.createElement("p");
      userMsg.textContent = "🧑 You: " + command;
      chatBox.appendChild(userMsg);

      // Send to Flask backend
      const response = await fetch("/", {
          method: "POST",
          headers: { "Content-Type": "application/x-www-form-urlencoded" },
          body: new URLSearchParams({ command }),
      });

      const text = await response.text();
      const parser = new DOMParser();
      const doc = parser.parseFromString(text, "text/html");
      const chat = doc.getElementById("chat-box").innerHTML;

      chatBox.innerHTML = chat;
      input.value = "";

      // 📢 Text-to-Speech for Assistant’s last reply
      const lastMsg = chatBox.querySelector("p:last-child")?.textContent;
      if (lastMsg) {
          try {
              const utterance = new SpeechSynthesisUtterance(lastMsg.replace("Assistant: ", ""));
              utterance.lang = "en-US";
              speechSynthesis.speak(utterance);
          } catch (err) {
              console.error("TTS error:", err);
          }
      }
  });
});


  // Show assistant's reply
  const chatBox = document.getElementById("chat-box");
  const msg = document.createElement("p");
  msg.innerHTML = `<b>Assistant:</b> ${result.message || ""}`;
  chatBox.appendChild(msg);

  // ✅ Auto-open website
  if (result.action === "open_url" && result.url) {
      window.open(result.url, "_blank");
  }

