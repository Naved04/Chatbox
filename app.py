from flask import Flask, render_template, request, jsonify
import subprocess
import string

app = Flask(__name__)

# ✅ Predefined questions and answers
predefined_answers = {
    "hi": "Hey there! 👋 How can I help you today?",
    "hello": "Hello! 😊 What’s up?",
    "who are you": "I'm your AI chatbot connected with Ollama 💡",
    "what can you do": "I can answer your questions, tell jokes, or explain things. If I don’t know, I’ll ask Ollama!",
    "tell me a joke": "Why did the computer catch a cold? Because it left its Windows open! 😂",
    "what is python": "Python is a popular programming language known for simplicity and power 🐍.",
    "who created you": "I was created by a developer using Flask and Ollama! ⚙️",
    "give me motivation": "Don’t stop when you’re tired. Stop when you’re done. 💪",
    "bye": "Goodbye! 👋 Have a great day!"
}

# 🧠 Function to call Ollama
def call_ollama(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", "llama3", prompt],
            capture_output=True,
            text=True
        )
        return result.stdout.strip() if result.stdout else "Hmm… Ollama didn’t respond 😅"
    except Exception as e:
        return f"⚠️ Error calling Ollama: {e}"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").lower().strip()
    # Remove punctuation for better matching
    user_message = user_message.translate(str.maketrans('', '', string.punctuation))

    # ✅ Check exact predefined questions
    if user_message in predefined_answers:
        return jsonify({"reply": predefined_answers[user_message]})

    # 🔥 Else call Ollama
    ai_reply = call_ollama(user_message)
    return jsonify({"reply": ai_reply})

if __name__ == "__main__":
    app.run(debug=True)
