const chatBody = document.querySelector(".chat-body");
const messageInput = document.querySelector(".message-input");
const chatForm = document.querySelector(".chat-form");

const createMessageElement = (content, className) => {
    const div = document.createElement("div");
    div.classList.add("message", className);
    div.innerHTML = content;
    return div;
};

chatForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const userMessage = messageInput.value.trim();
    if (!userMessage) return;

    const userContent = `
        <div class="message-text">${userMessage}</div>
    `;
    const userDiv = createMessageElement(userContent, "user-message");
    chatBody.appendChild(userDiv);

    const thinkingContent = `
        <img class="chatbot-avatar" src="/static/assets/chatbot-logo.png" alt="logo"/>
        <div class="message-text">
            <div class="thinking-indicator">
                <div class="dot"></div>
                <div class="dot"></div>
                <div class="dot"></div>
            </div>
        </div>
    `;
    const thinkingDiv = createMessageElement(thinkingContent, "bot-message");
    chatBody.appendChild(thinkingDiv);

    chatBody.scrollTop = chatBody.scrollHeight;
    messageInput.value = "";

    try {
        const formData = new FormData();
        formData.append("msg", userMessage);

        const response = await fetch("/get", {
            method: "POST",
            body: formData
        });

        const botReply = await response.text();
        thinkingDiv.remove();

        const botContent = `
            <img class="chatbot-avatar" src="/static/assets/chatbot-logo.png" alt="logo"/>
            <div class="message-text">${botReply}</div>
        `;
        const botDiv = createMessageElement(botContent, "bot-message");
        chatBody.appendChild(botDiv);
        chatBody.scrollTop = chatBody.scrollHeight;
    } catch (error) {
        thinkingDiv.remove();

        const errorContent = `
            <img class="chatbot-avatar" src="/static/assets/chatbot-logo.png" alt="logo"/>
            <div class="message-text">Sorry, something went wrong.</div>
        `;
        const errorDiv = createMessageElement(errorContent, "bot-message");
        chatBody.appendChild(errorDiv);
    }
});