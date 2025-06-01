from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def index():
    return render_template("cerebro.html")

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['mensaje']

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Eres un asistente llamado LuisGPT que responde de manera amable y clara."
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    return response['choices'][0]['message']['content']

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
