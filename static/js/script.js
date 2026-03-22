const chatBody = document.querySelector(".chat-body");
const messageInput = document.querySelector(".message-input");
const chatForm = document.querySelector(".chat-form");

const BOT_AVATAR = "/static/assets/chatbot-logo.png";

const createMessageElement = (content, className) => {
    const div = document.createElement("div");
    div.classList.add("message", className);
    div.innerHTML = content;
    return div;
};

const appendWelcomeMessage = () => {
    const alreadyExists = chatBody.querySelector(".bot-message");
    if (alreadyExists) return;

    const welcomeContent = `
        <img class="chatbot-avatar" src="${BOT_AVATAR}" alt="logo"/>
        <div class="message-text">
            Hi there 👋 <br /> How can I help you today?
        </div>
    `;
    const welcomeDiv = createMessageElement(welcomeContent, "bot-message");
    chatBody.appendChild(welcomeDiv);
};

const sendMessage = async (userMessage) => {
    const thinkingContent = `
        <img class="chatbot-avatar" src="${BOT_AVATAR}" alt="logo"/>
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

    try {
        const formData = new FormData();
        formData.append("msg", userMessage);

        const response = await fetch("/get", {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            throw new Error(`HTTP error: ${response.status}`);
        }

        const botReply = await response.text();
        thinkingDiv.remove();

        const botContent = `
            <img class="chatbot-avatar" src="${BOT_AVATAR}" alt="logo"/>
            <div class="message-text">${botReply}</div>
        `;
        const botDiv = createMessageElement(botContent, "bot-message");
        chatBody.appendChild(botDiv);
        chatBody.scrollTop = chatBody.scrollHeight;
    } catch (error) {
        thinkingDiv.remove();

        const errorContent = `
            <img class="chatbot-avatar" src="${BOT_AVATAR}" alt="logo"/>
            <div class="message-text">Sorry, something went wrong.</div>
        `;
        const errorDiv = createMessageElement(errorContent, "bot-message");
        chatBody.appendChild(errorDiv);
        chatBody.scrollTop = chatBody.scrollHeight;
        console.error(error);
    }
};

const handleOutgoingMessage = async (e) => {
    e.preventDefault();

    const userMessage = messageInput.value.trim();
    if (!userMessage) return;

    const userContent = `
        <div class="message-text">${userMessage}</div>
    `;
    const userDiv = createMessageElement(userContent, "user-message");
    chatBody.appendChild(userDiv);

    chatBody.scrollTop = chatBody.scrollHeight;
    messageInput.value = "";

    await sendMessage(userMessage);
};

window.addEventListener("DOMContentLoaded", () => {
    appendWelcomeMessage();
});

chatForm.addEventListener("submit", handleOutgoingMessage);

messageInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        chatForm.requestSubmit();
    }
});