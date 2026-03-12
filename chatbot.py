import random


def mood_chatbot(message):

    msg = message.lower()

    sad_words = ["sad","tired","depressed","upset","cry","lonely","stress","stressed"]
    happy_words = ["happy","good","great","excited","awesome"]
    angry_words = ["angry","mad","annoyed","frustrated"]


    sad_responses = [
        "I'm really sorry you're feeling this way. Sometimes talking about what's bothering you can help. What happened today?",
        "That sounds really tough. You're not alone though, I'm here to listen. Want to tell me more?",
        "Everyone has difficult days. It's okay to feel overwhelmed sometimes. What made your day tiring?",
        "That must have been exhausting. Take a deep breath for a moment. What part of your day felt the hardest?",
        "I understand how draining that can feel. But remember, one difficult day doesn't define you."
    ]


    happy_responses = [
        "That's wonderful to hear! What's making you feel good today?",
        "I'm glad you're feeling positive today 😊",
        "That sounds great! Moments like that are worth celebrating.",
        "That's awesome! Keep that energy going!"
    ]


    angry_responses = [
        "It sounds like something really frustrated you. Want to talk about it?",
        "That must have been irritating. What happened?",
        "Sometimes venting helps. I'm listening."
    ]


    neutral_responses = [
        "Tell me a bit more about what's on your mind.",
        "I'm listening. What would you like to talk about?",
        "That's interesting. Can you explain a little more?",
        "Hmm, I see. How did that make you feel?"
    ]


    if any(word in msg for word in sad_words):
        return random.choice(sad_responses)

    if any(word in msg for word in happy_words):
        return random.choice(happy_responses)

    if any(word in msg for word in angry_words):
        return random.choice(angry_responses)

    return random.choice(neutral_responses)