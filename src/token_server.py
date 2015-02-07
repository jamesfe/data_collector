"""
A server that serves tokens.
"""

from flask import Flask
import json
from os import listdir
from os.path import isfile, join
import sqlite3

app = Flask(__name__)

SCHEMAFILE = '../sql/tokenserver.sql'
TOKENDB = './tokens.db'
KEYDIR = '../keys/'
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
    if CONN is None:
        global CONN
        CONN = sqlite3.connect(TOKENDB)


def load_keys():
    """
    Load a set of keys from various databases
    :return:
    """
    dbconnect()
    keys = [_ for _ in listdir(KEYDIR) if _[-6:].lower() == 'sqlkey']
    cursor = CONN.cursor()
    for key in keys:
        with open(join(KEYDIR, key), 'r') as sql_file:
            sql_stmt = sql_file.read()
        cursor.executescript(sql_stmt)


if __name__ == '__main__':
    if not isfile(TOKENDB):
        with open(SCHEMAFILE) as f:
            sql_build_db = f.read()
        conn = sqlite3.connect(TOKENDB)
        curs = conn.cursor()
        curs.executescript(sql_build_db)
        conn.close()
    load_keys()

    # app.run()
