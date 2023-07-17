from flask import Flask, render_template
from markdown import markdown
import json

app = Flask(__name__)

@app.route('/')
def home():
    with open('chat_data.json') as f:
        chat_data = json.load(f)

    # Sort the chat data by timestamp
    chat_data = sorted(chat_data.values(), key=lambda msg: msg['timestamp'])

    # Convert content from markdown to HTML
    for message in chat_data:
        message['content'] = markdown(message['content'])

    return render_template('chat.html', chat_data=chat_data)

if __name__ == "__main__":
    app.run(debug=True)
