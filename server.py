"""
This module contains a Flask application. It receives the inputs text
from the HTML interface and passes it to the emotion detection function
before returning the response to the HTML interface via host: 0.0.0.0  
on port number 5000
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detect():
    """
    This function retrieves text from the HTML interface, passes it to the
    emotion_detector function and extracts the response to return the required
    response.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the scores and dominant emotion from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Error handling when dominant emotion is None
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Return required response
    return (f"For the given statement, the system response is 'anger': {anger}, "
          f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, and 'sadness': {sadness}. "
          f"The dominant emotion is <strong>{dominant_emotion}</strong>.")

@app.route("/")
def render_index_page():
    """
    This function renders the HTML page
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    