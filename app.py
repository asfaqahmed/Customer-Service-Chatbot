from flask import Flask, request, jsonify
from chatbot_model import Chatbot

app = Flask(__name__)
bot = Chatbot("faq.json")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "Message is required"}), 400
    response = bot.get_response(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
