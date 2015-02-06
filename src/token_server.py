"""
A server that serves tokens.
"""

from flask import Flask
import json
from os.path import isfile
import sqlite3

app = Flask(__name__)

SCHEMAFILE = '../sql/tokenserver.sql'
TOKENDB = './tokens.db'
CONN = None

@app.route('/flickr/')
def get_flickr_token():
    """
    Get a token for flickr and send it back.
    :return:
    """
    res = -1
    return json.dumps(res)
    return 'no tokens'


@app.route('/instagram/')
def get_instagram_token():
    """
    Get a token for instagram and send it back.
    :return:
    """
    pass


def dbconnect():
    """
    connect to the db
    :return:
    """
    global CONN
    CONN = sqlite3.connect(TOKENDB)
    return CONN.curs()


def load_keys():
    """
    Load a set of keys from various databases
    :return:
    """

if __name__ == '__main__':
    if not isfile(TOKENDB):
        with open(SCHEMAFILE) as f:
            sql_build_db = f.read()
        conn = sqlite3.connect(TOKENDB)
        curs = conn.cursor()
        curs.executescript(sql_build_db)
        conn.close()

    app.run()
