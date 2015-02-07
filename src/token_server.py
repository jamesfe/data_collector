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


@app.route('/<application>/gettoken/')
def get_instagram_token(application):
    """
    Get a token for instagram and send it back.
    :return:
    """
    # return a token.
    return -1

@app.route("/<application>/use/")
def increment_app(application):
    """
    increment a generic app up once
    :param application:
    :return:
    """
    increment_app(application)

def dbconnect():
    """
    connect to the db
    :return:
    """
    if CONN is None:
        global CONN
        CONN = sqlite3.connect(TOKENDB)
        CONN.row_factory = sqlite3.Row
    return CONN.cursor()


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


def init_db(tgt_db=TOKENDB):
    """
    If a DB doens't already exist, just create one.
    :return:
    """
    if not isfile(tgt_db):
        with open(SCHEMAFILE) as f:
            sql_build_db = f.read()
        conn = sqlite3.connect(tgt_db)
        curs = conn.cursor()
        curs.executescript(sql_build_db)
        conn.close()


if __name__ == '__main__':
    init_db()
    load_keys()

    # app.run()
