import unittest
import requests
import json


class TestCNNVader(unittest.TestCase):
    def test_request_response(self):
        # api url
        url = 'http://127.0.0.1:5000/url_eval'

        # url for requested article to test on
        # no need to request actual url since it may change. maybe worth downloading and storing in asset folder for tests
        # TODO
        request_url = 'https://www.cnn.com/2020/08/17/us/coronavirus-college-university/index.html'

        # package request into json payload
        j_url = json.dumps(request_url)
        headers = {'content-type': 'application/json',
                   'Accept-Charset': 'UTF-8'}

        # should probably move test dict to pickle
        # TODO
        test_dict = {"keywords": ["covid19", "inperson", "reverses", "classes", "tested", "cases", "test", "students", "campus", "uncchapel", "plans", "university", "oklahoma", "hill", "positive", "quarantine"], "score": {"compound": 0.9861, "neg": 0.043, "neu": 0.884, "pos": 0.073},
                     "summary": "(CNN) The University of North Carolina at Chapel Hill abruptly decided it will no longer hold in-person classes on campus after about 130 students tested positive for Covid-19 in the first week since classes began.\nIn the past week, the Covid-19 positivity rate among students rose to 13.6% of the 954 students tested, and five employees also tested positive, according to the university's Covid-19 dashboard.\nOn Sunday, UNC announced a fourth cluster of Covid-19 cases on campus, defined as five or more cases in proximity.\nAn Oklahoma State University sorority house is under quarantine after 23 members tested positive for Covid-19, according to the university.\nThe student who tested positive is receiving care after arriving on campus on August 14 and exposing residents of Loomis Hall, according to the report.", "title": "UNC-Chapel Hill reverses plans for in-person classes after 130 students test positive for Covid-19"}

        # get request
        r = requests.post(url, data=j_url, headers=headers)
        request_json = json.loads(r.text)

        # tests
        self.assertEqual(r.status_code, 200, "Docker HTTP response not 200")
        self.assertDictEqual(
            request_json, test_dict, "Response json does not contain the expected values.\nResponse values:\n" + r.text)


if __name__ == '__main__':
    unittest.main()
