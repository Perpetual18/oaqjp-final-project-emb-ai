import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):
    # URL of the emotion analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # Custom header specifying the model ID for the sentiment analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=myobj, headers=header)
    
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    
    # If response status code is 400, return same dictionary with all keys being None
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
            }

    # Extracting required emotions and scores from the response
    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

    #Determine dominant emotion
    dominant_emotion_score = max([anger_score, disgust_score, fear_score, joy_score, sadness_score])
    emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
    for emotion in emotions:
        if formatted_response['emotionPredictions'][0]['emotion'][emotion] == dominant_emotion_score:
            dominant_emotion = emotion
  
    # Returning the required dictionary
    return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
           }