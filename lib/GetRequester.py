import requests

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url, timeout=5)  # Add timeout
        return response.content

    def load_json(self):
        response = requests.get(self.url, timeout=5)  # Add timeout
        return response.json()
