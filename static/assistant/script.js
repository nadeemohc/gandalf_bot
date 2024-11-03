async function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    if (!userInput) return;

    // Append user message to chat box
    const chatBox = document.getElementById("chat-box");
    const userMessage = document.createElement("div");
    userMessage.className = "chat-message user";
    userMessage.innerHTML = `<p>${userInput}</p>`;
    chatBox.appendChild(userMessage);

    // Fetch Gandalf's response from the server
    const response = await fetch('/chat/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userInput, context: chatBox.innerText })
    });
    
    // Check if the response is okay
    if (response.ok) {
        const data = await response.json();

        // Append Gandalf's message to chat box
        const gandalfMessage = document.createElement("div");
        gandalfMessage.className = "chat-message gandalf";
        gandalfMessage.innerHTML = `<p>${data.message}</p>`;
        chatBox.appendChild(gandalfMessage);
    } else {
        // Handle error
        console.error('Error fetching response:', response.statusText);
    }

    // Clear input after processing the response
    document.getElementById("user-input").value = "";
    // Scroll to the bottom of the chat box
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Add an event listener for the 'Enter' key
document.getElementById("user-input").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        event.preventDefault(); // Prevent default form submission (if inside a form)
        sendMessage(); // Call the sendMessage function
    }
});
