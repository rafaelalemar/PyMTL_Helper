
import requests
import json


class GAS(object):
    def __init__(self):
        self.url = None
        self.status_code = None
        self.content = {}
        self.response = None

    def setUrl(self, url):
        self.url = url
        return self

    def run(self, body={}):
        response = requests.post(self.url, data=body)
        self.status_code = response.status_code
        self.response = response
        if response.status_code == 200:
            self.content = json.loads(response.text)
        return self

    def contents(self):
        return self.content
