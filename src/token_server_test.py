"""
A set of tests for our token server.
Twitter: @jimmysthoughts
GitHub: github.com/jamesfe
"""


import unittest
from token_server import init_db, get_token, dbconnect, load_keys


class MyTestCase(unittest.TestCase):
    """
    Get some tokens, set some tokens, load tokens, test everything.
    """
    def setUp(self):
        """
        initialize the database
        :return:
        """
        print "Setup Function"
        init_db()
        conn, curs = dbconnect()

        print "Key Load Tests"
        load_keys()

        curs.execute("SELECT * FROM tokens")
        # More than 0 results
        count = 0
        for i in curs.fetchall():
            print i
            count += 1
        self.assertGreater(count, 0)

    def test_token_acq(self):
        """
        Check to see if we get accurate tokens from the db server.
        :return:
        """
        print "Token Aquisition Tests"
        token = get_token('instagram')
        print token
        self.assertNotEqual(token, -1)

    def test_increment_token(self):
        """
        Increment a bunch of times and see what happens.
        :return:
        """
        print "Token increment: "
        for i in range(0, 100):
            token = get_token('instagram')
        conn, curs = dbconnect()

        # sql = "SELECT token_id, max_uses, use_period_secs FROM tokens WHERE token_id=%s"
        # data = (token[0])
        # curs.execute("SELECT COUNT(*) FROM token_use WHERE token_id=%s AND


if __name__ == '__main__':
    unittest.main()
