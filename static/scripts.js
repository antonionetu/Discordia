if (!localStorage.getItem('nick')) {
    localStorage.setItem('next', location.href)
    location.href = "/set-name"
}

document.querySelector("#input").addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
        event.preventDefault();
        sendMessage();
    }
})

socket.onmessage = function (event) {
    const data = JSON.parse(event.data)
    const messages = document.querySelector('#messages')

    addMessage(data, messages)
}

function sendMessage() {
    const input = document.querySelector('#input')

    socket.send(JSON.stringify({
        'author': localStorage.getItem('nick'),
        'message': input.value,
        'chat_name': roomName,
    }));

    input.value = ''
}

function addMessage(data, messages) {
    const lastAuthor = messages.children[messages.children.length - 1]
    const currentAuthor = data.author

    const newMessage = document.createElement("p")
    newMessage.innerHTML = data.message

    if (lastAuthor.getAttribute('data-author') === currentAuthor) {
        lastAuthor.appendChild(newMessage)
        return;
    }

    const greetings = document.createElement("p")
    greetings.innerHTML = `${currentAuthor} disse:`
    greetings.classList.add('greetings')
    messages.appendChild(greetings)

    const newSender = document.createElement("div")
    newSender.setAttribute('data-author', data.author)
    newSender.appendChild(newMessage)
    newSender.classList.add('message')

    messages.appendChild(newSender)

    messages.scrollTop = messages.scrollHeight;
}