"""
collector for instagram photos
"""

from data_collector import DataCollector


class InstagramColl(DataCollector):
    """
    class to collect instagram stuff
    """
    def __init__(self):
        """
        initialize some stuff here
        """
        super(InstagramColl, self).__init__()

    def pull_data(self):
        """
        overrides the parent method: specifics of getting data here.
        :return:
        """
        print "Collecting."


