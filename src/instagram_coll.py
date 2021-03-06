"""
collector for instagram photos
"""
from __future__ import (absolute_import, division, print_function, unicode_literals)

from requests import get

from data_collector import DataCollector


class InstagramColl(DataCollector):
    """
    class to collect instagram stuff
    """
    def __init__(self, latitude, longitude, distance):
        """
        initialize some stuff here
        """
        super(InstagramColl, self).__init__()
        self.latitude = latitude
        self.longitude = longitude
        self.distance = distance
        self.access_token = self.getkey()

    def getkey(self):
        """
        Open the keys directory, extract a token
        :return:
        """
        # TODO: Set access token here.
        return -1 + self.distance

    def pull_data(self):
        """
        overrides the parent method: specifics of getting data here.
        :return:
        """
        payload = {"lat": self.latitude,
                   "lng": self.longitude,
                   "access_token": self.access_token,
                   "distance": self.distance}
        request = get("https://api.instagram.com/v1/locations/search",
                      params=payload)



