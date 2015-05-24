"""
Data collection classes.
"""
from __future__ import (absolute_import, division, print_function, unicode_literals)

import threading


class DataCollector(threading.Thread):
    """
    A class from which other data collection classes will inherit.
    """

    def __init__(self):
        """
        methods to initialize oneself
        """
        super(DataCollector, self).__init__()

    def run(self):
        """
        Method that simply calls our own overwritten method.
        """
        self.pull_data()

    def pull_data(self):
        """
        method to pull data
        """
        pass
