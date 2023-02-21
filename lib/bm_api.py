from urllib.request import urlopen
import json

class BmAPI:

    def __init__(self):
        self.url = "https://opendata.bordeaux-metropole.fr/api/records/1.0/search/?dataset=ci_courb_a&rows=193"

    def get_daily_stat(self):
        """
        :return str: raw json with daily bm stats
        """
        response = urlopen(self.url)
        return response.read()
