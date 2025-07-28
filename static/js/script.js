async function sendMessage() {
  const userInput = document.getElementById("user-input");
  const chatLog = document.getElementById("chat-log");
  const question = userInput.value.trim();
  if (!question) return;

  const userMessage = document.createElement("p");
  userMessage.innerHTML = `<span class="chat-user">You:</span> ${question}`;
  chatLog.appendChild(userMessage);
  userInput.value = "";

  try {
    const res = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: question }),
    });

    const data = await res.json();
    const assistantMessage = document.createElement("p");
    assistantMessage.innerHTML = `<span class="chat-assistant">Assistant:</span> ${data.reply}`;
    chatLog.appendChild(assistantMessage);
    chatLog.scrollTop = chatLog.scrollHeight;
  } catch (err) {
    const errorMsg = document.createElement("p");
    errorMsg.innerHTML = `<span class="chat-assistant">Assistant:</span>Error: ${err.message}`;
    chatLog.appendChild(errorMsg);
  }
}