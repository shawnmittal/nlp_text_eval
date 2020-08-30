import unittest
import requests
import json


class TestUrlPost(unittest.TestCase):
    def setUp(self):
        self.url = "http://localhost:5000/url_eval"
        self.valid_request_url = json.dumps("https://www.cnn.com/2020/08/17/us/coronavirus-college-university/index.html")
        self.invalid_request_url = json.dumps("http://www.notrealurl.com/this-is-a-fake-url")
        self.headers = {"content-type": "application/json", "Accept-Charset": "UTF-8"}

    def post_request(self, url, data, headers):
        r = requests.post(
            url, data=data, headers=headers
        )
        response_json = json.loads(r.text)

        self.assertEqual(
            r.status_code,
            200,
            f"Docker HTTP response not 200:\n{r.status_code}",
        )
        self.assertTrue(
            len(response_json["keywords"]) > 0,
            f"summary does not contain enough data:\n{response_json['keywords']}",
        )
    
    def test_valid_request(self):
        self.post_request(self.url, self.valid_request_url, self.headers)

    def test_invalid_reqeust(self):
        self.post_request(self.url, self.invalid_request_url, self.headers)

if __name__ == "__main__":
    unittest.main()
