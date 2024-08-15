function stylizeText(text) {
    // Bold text between **
    text = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    
    // Convert - to bullet points
    text = text.replace(/^-\s(.+)$/gm, '<li>$1</li>');
    text = text.replace(/<li>/g, '<ul><li>').replace(/<\/li>(?![\n\r]*<li>)/g, '</li></ul>');
    
    return text;
}
// Refreshes all text fields
window.onload = function() {
    document.getElementById('document-content').value = '';
    document.getElementById('system-prompt').value = '';
    document.getElementById('intent').value = '';
    document.getElementById('expected-length').value = '';
    document.getElementById('focus').value = '';
    document.getElementById('tone').value = '';
    document.getElementById('target-audience').value = '';
    document.getElementById('emphasis').value = '';
    document.getElementById('customize').value = '';
};

// Show dropdown options on input focus
document.querySelectorAll('.form-group input').forEach(input => {
    input.addEventListener('focus', function() {
        this.nextElementSibling.style.display = 'block';
    });
});

// Hide dropdown options when selecting an option
document.querySelectorAll('.dropdown-options div').forEach(option => {
    option.addEventListener('click', function() {
        const input = this.parentElement.previousElementSibling;
        input.value = this.innerText;
        this.parentElement.style.display = 'none';
    });
});

// Hide dropdown when clicking outside
document.addEventListener('click', function(event) {
    document.querySelectorAll('.dropdown-options').forEach(dropdown => {
        if (!event.target.closest('.form-group input')) {
            dropdown.style.display = 'none';
        }
    });
});

// Hide dropdown when pressing Escape
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        document.querySelectorAll('.dropdown-options').forEach(dropdown => {
            dropdown.style.display = 'none';
        });
    }
});
document.getElementById('send-button').addEventListener('click', async function() {
    
    const data = {
        'sys_prompt': document.getElementById('system-prompt').value,
        'document': document.getElementById('document-content').value,
        'intent': document.getElementById('intent').value,
        'tone': document.getElementById('tone').value,
        'length': document.getElementById('expected-length').value,
        'focus': document.getElementById('focus').value,
        'target_audience': document.getElementById('target-audience').value,
        'emphasis': document.getElementById('emphasis').value,
        'customization': document.getElementById('customize').value
    };

    // Calling the API endpoint to generate response and the user prompt
    const response = await fetch('/gen-sum', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });
    

    const responseData = await response.json();
    const chatContainer = document.getElementById('chat-container');

    const promptContainer = document.createElement('div');
    promptContainer.className = 'prompt-container';

    const promptLabel = document.createElement('div');
    promptLabel.className = 'chat-label';
    promptLabel.innerText = 'PROMPT';

    const promptBubble = document.createElement('div');
    promptBubble.className = 'chat-bubble prompt';
    //promptBubble.innerText = responseData.user_prompt;
    promptBubble.innerHTML = responseData.user_prompt;

    promptContainer.appendChild(promptLabel);
    promptContainer.appendChild(promptBubble);

    chatContainer.appendChild(promptContainer);

    // Wait for 1 second
    setTimeout(() => {
        const responseContainer = document.createElement('div');
        responseContainer.className = 'response-container';

        const responseLabel = document.createElement('div');
        responseLabel.className = 'chat-label';
        responseLabel.innerText = 'AI Summary';

        const responseBubble = document.createElement('div');
        responseBubble.className = 'chat-bubble response';
        // responseBubble.innerText = responseData.prompt_response;
        responseBubble.innerHTML = stylizeText(responseData.prompt_response);

        responseContainer.appendChild(responseLabel);
        responseContainer.appendChild(responseBubble);

        chatContainer.appendChild(responseContainer);
    }, 1000);

    chatContainer.scrollTo(0, chatContainer.scrollHeight);
});

// File selecting and fetching the input
document.getElementById('file-input').addEventListener('change', async function(event) {
    const form = document.getElementById('document-content');
    const formData = new FormData(form);
    
    await fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.content) {
            document.getElementById('document-content').value = data.content;
        } else if (data.error) {
            document.getElementById('document-content').value = `Error: ${data.error}`;
        }
    })
    .catch(error => {
        document.getElementById('document-content').value = `Error: ${error}`;
    });
});