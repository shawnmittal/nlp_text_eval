import unittest
import requests
import json


class TestValidUrl(unittest.TestCase):
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

class TestInvalidUrl(unittest.TestCase):
    def test_request_response(self):
        self.url = "http://localhost:5000/url_eval"
        self.request_url = "http://www.notrealurl.com/this-is-a-fake-url"

        j_url = json.dumps(self.request_url)
        headers = {"content-type": "application/json", "Accept-Charset": "UTF-8"}

        r = requests.post(self.url, data=j_url, headers=headers)

        self.assertNotEqual(r.status_code, 200, "Docker HTTP response was 200")
        self.assertEqual(len(r.text), 0, "Response text not empty")


if __name__ == "__main__":
    unittest.main()
