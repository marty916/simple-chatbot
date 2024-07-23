from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key = os.getenv('OPENAI_API_KEY')
)

app = FastAPI()

@app.get("/")
async def get():
    return HTMLResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Chatbot</title>
    </head>
    <body>
        <h1>Chat with AI</h1>
        <div id="messages"></div>
        <input type="text" id="input" placeholder="Type a message...">
        <button onclick="sendMessage()">Send</button>
        <script>
            const ws = new WebSocket("ws://localhost:8000/ws");

            ws.onmessage = function(event) {
                const messageDiv = document.createElement('div');
                messageDiv.textContent = 'Bot: ' + event.data;
                document.getElementById('messages').appendChild(messageDiv);
            };

            function sendMessage() {
                const input = document.getElementById('input');
                const message = input.value;
                input.value = '';
                
                const messageDiv = document.createElement('div');
                messageDiv.textContent = 'You: ' + message;
                document.getElementById('messages').appendChild(messageDiv);

                ws.send(message);
            }
        </script>
    </body>
    </html>
    """)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        message = await websocket.receive_text()
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message}
            ],
            model="gpt-4o-mini"
        )
        await websocket.send_text(response.choices[0].message.content)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
