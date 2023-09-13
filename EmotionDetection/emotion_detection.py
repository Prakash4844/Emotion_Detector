import requests
import json

def emotion_detector(text_to_analyze):
    # Define the URL, headers, and input JSON format
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    try:
        # Send a POST request to the Emotion Predict function
        response = requests.post(URL, headers=headers, json=input_json)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            formatted_response = json.loads(response.text)
    
            emotions = { 
                        'anger': 0,
                        'disgust': 0,
                        'fear': 0,
                        'joy': 0,
                        'sadness': 0,
                        'dominant_emotion': -1
            }
            emotions['anger'] = formatted_response['emotionPredictions'][0]['emotion']['anger']
            emotions['disgust'] = formatted_response['emotionPredictions'][0]['emotion']['disgust']
            emotions['fear'] = formatted_response['emotionPredictions'][0]['emotion']['fear']
            emotions['joy'] = formatted_response['emotionPredictions'][0]['emotion']['joy']
            emotions['sadness'] = formatted_response['emotionPredictions'][0]['emotion']['sadness']
            emotions['dominant_emotion'] = max(emotions, key=emotions.get)

            return emotions
        
        elif response.status_code == 400:
            emotions = {   'anger': None,
                            'disgust': None,
                            'fear': None,
                            'joy': None,
                            'sadness': None,
                            'dominant_emotion': None }
            return emotions
        
        else:
            print(f"Error: Request failed with status code {response.status_code}")
            return None

    except Exception as e:
        print(f"Error: {str(e)}")
        return None


if __name__ == "__main__":
    # Example usage:
    text = "I am happy!"
    detected_emotion = emotion_detector(text)
    
    if detected_emotion:
        print(f"Detected Emotion: {detected_emotion}")
    else:
        print("Emotion detection failed.")
