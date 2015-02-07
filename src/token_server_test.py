__author__ = 'jimmy1'

import unittest
from token_server import get_free_token, init_db


class MyTestCase(unittest.TestCase):
    def __init__(self):
        """
        initialize the database
        :return:
        """
        init_db("./test_db.db")

    def test_token_acq(self):
        """
        Check to see if we get accurate tokens from the db server.
        :return:
        """
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
