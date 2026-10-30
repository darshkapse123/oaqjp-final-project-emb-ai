import unittest
from unittest.mock import patch, Mock
import requests

from emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):

    def test_emotion_detector_success(self):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "emotionPredictions": [{
                "emotion": {
                    "anger": 0.01,
                    "disgust": 0.02,
                    "fear": 0.03,
                    "joy": 0.90,
                    "sadness": 0.04
                }
            }]
        }

        with patch("emotion_detection.requests.post",
                   return_value=mock_response):
            result = emotion_detector("I am very happy")

        self.assertEqual(result["dominant_emotion"], "joy")
        self.assertEqual(result["joy"], 0.90)

    def test_empty_text(self):
        result = emotion_detector("")
        self.assertIsNone(result["dominant_emotion"])

    def test_api_connection_error(self):
        with patch(
            "emotion_detection.requests.post",
            side_effect=requests.exceptions.ConnectionError
        ):
            result = emotion_detector("I am happy")

        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
