import unittest
import requests
import json


class TestCNNVader(unittest.TestCase):
    def test_request_response(self):
        self.url = "http://localhost:5000/url_eval"
        self.request_url = "https://www.cnn.com/2020/08/17/us/coronavirus-college-university/index.html"

        # package request into json payload
        j_url = json.dumps(self.request_url)
        headers = {"content-type": "application/json", "Accept-Charset": "UTF-8"}

        # get request
        r = requests.post(self.url, data=j_url, headers=headers)

        # tests
        self.assertEqual(r.status_code, 200, "Docker HTTP response not 200.")
        self.assertTrue(len(r.text) > 10, "Response does not contain enough data.")


if __name__ == "__main__":
    unittest.main()
