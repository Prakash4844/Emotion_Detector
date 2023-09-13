'''
    Executing this function initiates the application of Emotion Detector 
    to be executed over the Flask channel and deployed on localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection import emotion_detection


app = Flask("Emotion Detection")


@app.route("/emotionDetector")
def sent_analyzer():
    '''
        This code receives the text from the HTML interface and runs sentiment analysis over it 
        using emotion_detection.emotion_detector() function. The output returned shows the 
        label and its confidence anger, disgust, fear, joy, sadness, dominant_emotion.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detection.emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    system_response = (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return system_response


@app.route("/")
def render_index_page():
    ''' 
        This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    