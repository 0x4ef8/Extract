import requests
from bs4 import BeautifulSoup as bs

class TimelineNoLogin:
    def __init__(self):
        self.result = []

    def LandingTimeline(self, id_type, id, limit):
        url = f'https://www.facebook.com/{id_type}/{id}'
        self.ScrapData(url, limit)

    def ScrapData(self, url, limit):
        response = requests.get(url)
        soup = bs(response.content, 'html.parser')

        # For simplicity, let's assume we're just collecting some dummy data
        self.result = [{'id': '123', 'name': 'Dummy Name'} for _ in range(limit)]
