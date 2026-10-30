"""Flask web application for emotion detection."""

from flask import Flask, request, render_template
from emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    """Display the home page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def detect_emotion():
    """Receive text and return its detected emotions."""
    text_to_analyze = request.args.get("textToAnalyze", "")

    if not text_to_analyze.strip():
        return "Invalid text! Please try again."

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return (
            "Emotion detection service is currently unavailable. "
            "Please try again later."
        )

    response = (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
