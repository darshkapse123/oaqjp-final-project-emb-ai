# Emotion Detection Application

## Project Overview
A Flask web application that detects five emotions from text using IBM Watson NLP:
- Anger
- Disgust
- Fear
- Joy
- Sadness

It also identifies the dominant emotion.

## Technologies Used
- Python
- Flask
- Requests
- HTML
- JavaScript
- Bootstrap
- IBM Watson NLP

## Project Files
- emotion_detection.py
- server.py
- test_emotion_detection.py
- static/mywebscript.js
- templates/index.html

## Installation

Install dependencies:

```bash
python3 -m pip install flask requests
```

## Run Application

```bash
python3 server.py
```

Open http://127.0.0.1:5001 in your browser.

## Run Tests

```bash
python3 -m unittest -v test_emotion_detection
```

## Code Quality
- emotion_detection.py: Pylint 10/10
- server.py: Pylint 10/10
- Unit tests: 3 passed

## Note
The application requires access to the IBM Watson NLP Emotion Detection service. If the service is unavailable, the application displays an appropriate error message.Final Project
