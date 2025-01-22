/*
Project: Finetuned AI Assistant
Author: Aditya Khadye
Date: 2025-01-22

Description:
This script handles frontend interactions for the Finetuned AI Assistant, including sending prompts to the backend,
displaying AI responses, and managing chat history.
*/

// Sends the user prompt to the backend and retrieves the response
function sendPromptToChatGPT() {
    const prompt = document.getElementById('input-prompt').value;

    // Send POST request to the backend
    fetch('/get-chatgpt-response', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt })
    })
        .then(response => response.json())
        .then(data => {
            // Display the AI's response in the textarea
            document.getElementById('chatgpt-response').value = data.response;
            // Save the conversation to the database
            saveChat(prompt, data.response);
        })
        .catch(error => console.error('Error:', error));
}

// Saves the conversation to the database
function saveChat(prompt, response) {
    fetch('/save-chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt, response })
    });
}

// Loads chat history from the backend
function loadChatHistory() {
    fetch('/history')
        .then(response => response.json())
        .then(data => {
            // Format the chat history for display
            const history = data.map(chat => `${chat.prompt}\n${chat.response}`).join('\n\n');
            document.getElementById('chat-history').value = history;
        });
}

// Load chat history when the page is loaded
window.onload = loadChatHistory;