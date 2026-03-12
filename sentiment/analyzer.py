from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from collections import Counter
import re

analyzer = SentimentIntensityAnalyzer()

stopwords = {
"the","is","and","a","to","of","in","it","that","this",
"for","on","with","as","are","was","but","be","have",
"you","i","they","he","she"
}


def clean_words(text):

    text = text.lower()

    words = re.findall(r'\b[a-z]{3,}\b', text)

    return [w for w in words if w not in stopwords]


def analyze_comments(comments):

    positive = 0
    negative = 0
    neutral = 0

    pos_words = []
    neg_words = []
    all_words = []

    for c in comments:

        score = analyzer.polarity_scores(c)["compound"]

        words = clean_words(c)

        all_words.extend(words)

        if score >= 0.05:
            positive += 1
            pos_words.extend(words)

        elif score <= -0.05:
            negative += 1
            neg_words.extend(words)

        else:
            neutral += 1

    top_positive = Counter(pos_words).most_common(10)
    top_negative = Counter(neg_words).most_common(10)
    word_cloud = Counter(all_words).most_common(40)

    mood = "Neutral"

    if positive > negative:
        mood = "Positive 😊"

    if negative > positive:
        mood = "Negative 😡"

    return {
        "positive": positive,
        "neutral": neutral,
        "negative": negative,
        "mood": mood,
        "top_positive": top_positive,
        "top_negative": top_negative,
        "word_cloud": word_cloud
    }
