"""
A set of tests for our token server.
Twitter: @jimmysthoughts
GitHub: github.com/jamesfe
"""


import unittest
from token_server import init_db, get_token


class MyTestCase(unittest.TestCase):
    """
    Get some tokens, set some tokens, load tokens, test everything.
    """
    def setUp(self):
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
        token = get_token('instagram')
        self.assertNotEqual(token, None)


if __name__ == '__main__':
    unittest.main()
