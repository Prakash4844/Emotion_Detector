from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        res_1 = emotion_detector("I am glad this happened")
        self.assertEqual(res_1['dominant_emotion'], 'joy')

        res_2 = emotion_detector("I am really mad about this")
        self.assertEqual(res_2['dominant_emotion'], 'anger')

        res_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(res_3['dominant_emotion'], 'disgust')

        res_4 = emotion_detector("I am so sad about this")
        self.assertEqual(res_4['dominant_emotion'], 'sadness')

        res_4 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(res_4['dominant_emotion'], 'fear')

unittest.main()