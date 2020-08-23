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
        r_json = json.loads(r.text)

        # tests
        self.assertEqual(r.status_code, 200, f"Docker HTTP response not 200:\n{r.status_code}")
        self.assertTrue(len(r_json['keywords']) > 0, f"summary does not contain enough data:\n{r_json['keywords']}")

class TestInvalidUrl(unittest.TestCase):
    def test_request_response(self):
        self.url = "http://localhost:5000/url_eval"
        self.request_url = "http://www.notrealurl.com/this-is-a-fake-url"

        j_url = json.dumps(self.request_url)
        headers = {"content-type": "application/json", "Accept-Charset": "UTF-8"}

        r = requests.post(self.url, data=j_url, headers=headers)
        r_json = json.loads(r.text)

        self.assertEqual(r.status_code, 200, f"Docker HTTP response not 200:\n{r.status_code}")
        self.assertTrue(len(r_json['keywords']) < 1, f"Response text not empty:\n{r.text}")


if __name__ == "__main__":
    unittest.main()
