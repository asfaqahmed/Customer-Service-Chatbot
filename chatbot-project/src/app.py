from flask import Flask, request, jsonify, render_template
from utils.auth import token_required
from utils.logging import setup_logging
from chatbot_model import Chatbot
from transformers.bert_model import BERTModel

app = Flask(__name__)
setup_logging()

# Load the chatbot and BERT model
chatbot = Chatbot('faqs.json')
bert_model = BERTModel()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
@token_required
def chat():
    user_input = request.json.get('message')
    response = chatbot.get_response(user_input)  # Assuming a method to get response
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)