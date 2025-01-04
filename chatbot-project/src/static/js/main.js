// src/static/js/main.js

document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("chat-form");
    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");

    form.addEventListener("submit", function(event) {
        event.preventDefault();
        const userMessage = input.value;
        appendMessage("You: " + userMessage);
        input.value = "";

        fetch("/api/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": "Bearer " + localStorage.getItem("authToken")
            },
            body: JSON.stringify({ message: userMessage })
        })
        .then(response => response.json())
        .then(data => {
            appendMessage("Bot: " + data.response);
        })
        .catch(error => {
            console.error("Error:", error);
            appendMessage("Bot: Sorry, there was an error processing your request.");
        });
    });

    function appendMessage(message) {
        const messageElement = document.createElement("div");
        messageElement.textContent = message;
        chatBox.appendChild(messageElement);
    }
});