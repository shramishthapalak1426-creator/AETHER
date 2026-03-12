from flask import Flask, render_template, request, jsonify
import sqlite3
import random

from sentiment.youtube_scraper import get_youtube_comments
from sentiment.analyzer import analyze_comments

app = Flask(__name__)


# HOME PAGE
@app.route("/")
def home():
    return render_template("index.html")


# YOUTUBE ANALYSIS PAGE
@app.route("/youtube")
def youtube_page():
    return render_template("youtube.html")


# CHATBOT PAGE
@app.route("/chatbot_page")
def chatbot_page():
    return render_template("chatbot.html")


# FEEDBACK PAGE
@app.route("/feedback_page")
def feedback_page():
    return render_template("feedback.html")


# ABOUT PAGE
@app.route("/about")
def about():
    return render_template("about.html")


# YOUTUBE ANALYSIS API
@app.route("/analyze", methods=["POST"])
def analyze():

    url = request.form["url"]

    comments = get_youtube_comments(url)

    result = analyze_comments(comments)

    return jsonify(result)


# CHATBOT API
@app.route("/chatbot", methods=["POST"])
def chatbot():

    import random

    message = request.form["message"].lower()

    greetings = ["hi","hello","hey"]
    wellbeing = ["how are you","how r you"]
    sad_words = ["sad","tired","depressed","upset","cry","lonely"]
    stress_words = ["stress","work","pressure","scolding","teacher"]
    happy_words = ["happy","good","great","awesome","excited"]

    greeting_responses = [
        "Hi there! 😊 How has your day been going?",
        "Hello! I'm glad you're here. How are you feeling today?",
        "Hey! Tell me what's on your mind."
    ]

    wellbeing_responses = [
        "I'm doing well, thanks for asking! I'm here to listen to you. How has your day been?",
        "I'm here and ready to chat. How are *you* feeling today?",
        "I'm doing great! Tell me about your day."
    ]

    sad_responses = [
        "I'm really sorry you're feeling this way. Do you want to talk about what happened today?",
        "That sounds really exhausting. I'm here to listen if you'd like to share more.",
        "Some days can feel really heavy. What part of your day was the hardest?",
        "It sounds like today wasn't easy. But you're not alone — I'm here with you."
    ]

    stress_responses = [
        "That sounds stressful. Sometimes taking a small break can help reset your mind.",
        "Stress can really build up during the day. What part of your work felt overwhelming?",
        "That must have been frustrating. Want to tell me more about what happened?"
    ]

    happy_responses = [
        "That's wonderful to hear! 😊 What made your day good?",
        "I'm glad you're feeling positive today!",
        "That's great! Positive moments are always worth celebrating."
    ]

    neutral_responses = [
        "That's interesting. Tell me more about it.",
        "I see. What happened next?",
        "How did that make you feel?",
        "I'm listening. Go on."
    ]

    if any(word in message for word in greetings):
        response = random.choice(greeting_responses)

    elif any(word in message for word in wellbeing):
        response = random.choice(wellbeing_responses)

    elif any(word in message for word in sad_words):
        response = random.choice(sad_responses)

    elif any(word in message for word in stress_words):
        response = random.choice(stress_responses)

    elif any(word in message for word in happy_words):
        response = random.choice(happy_responses)

    else:
        response = random.choice(neutral_responses)

    return jsonify({"response": response})


# FEEDBACK API
@app.route("/feedback", methods=["POST"])
def feedback():

    text = request.form["feedback"]

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS feedback(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT
    )
    """)

    cur.execute("INSERT INTO feedback(text) VALUES (?)", (text,))

    conn.commit()
    conn.close()

    return jsonify({"status": "saved"})


# RUN APP
if __name__ == "__main__":
    app.run(debug=True)
    