# 🤖 AI Chatbot

A simple **web-based AI chatbot** built with **Flask**, **HTML/CSS/JS**, and **Ollama AI**.  
The bot can answer **predefined questions** instantly and also uses **Ollama AI** to answer anything else dynamically.
---

## 🎯 Features

- Modern ChatGPT-style UI  
- Predefined sample questions for quick responses  
- Clickable suggested questions  
- Fallback to Ollama AI for unknown queries  
- Runs locally on your computer  

---

## 🛠️ Step 1: Install Ollama

1. Go to the official website and download Ollama:  
   👉 [https://ollama.com](https://ollama.com)

2. Install it like a normal app (Windows/Mac supported).  

3. Verify the installation:

   Open **Command Prompt (Windows)** or **Terminal (Mac/Linux)** and run:
   ```bash
   ollama --version

You should see something like:

Warning: could not connect to a running Ollama instance
Warning: client version is 0.12.x


✅ This means Ollama is installed, but the service isn’t running yet — no worries, it auto-starts when needed.

🧠 Step 2: Pull an AI Model

Ollama requires a model to generate AI responses.
We recommend Llama 3 for this project:

ollama pull llama3


This downloads the model (~4–5 GB).
It may take a few minutes depending on your internet.

👉 For faster testing, you can use a smaller model like Phi-3:

ollama pull phi3

⚙️ Step 3: Test the Model

Once the model is downloaded, test it:

ollama run llama3


Type a message like:

>>> Hello


You should get a response like:

Hi there! How can I help you today?


✅ This confirms Ollama is working properly.

💻 Step 4: Install Python & Flask

Make sure you have Python 3.8+ installed:
🔗 https://www.python.org/downloads/

Install Flask:

pip install flask


Make sure Ollama is running in the background (it auto-starts when needed).

🚀 Step 5: Run the Chatbot

Open a terminal/command prompt in the project folder, then run:

python app.py


Open your browser and visit:

http://127.0.0.1:5000


Now you can chat with your bot 🎉

✅ Try these:

Click sample questions

Type your own questions

Predefined answers respond instantly

Anything else is sent to Ollama AI

⚠️ Notes & Tips

First model download may take 5–10 minutes

Keep Ollama running while using the chatbot

To stop Ollama:

Close the app, or

End ollama.exe in Task Manager (Windows)

You can edit predefined questions in app.py under the predefined_answers dictionary

✨ Enjoy building your personal AI assistant!
