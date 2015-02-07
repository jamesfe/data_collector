"""
A server that serves tokens for the gathering of social media.
Twitter: @jimmysthoughts
GitHub: github.com/jamesfe
"""

from flask import Flask
from os import listdir
from os.path import isfile, join
import sqlite3
import time

FLASK_APP = Flask(__name__)

SCHEMAFILE = '../sql/tokenserver.sql'
TOKENDB = './tokens.db'
KEYDIR = '../keys/'
CONN = None


@FLASK_APP.route('/<application>/gettoken/')
def get_token(application):
    """
    Get a token for instagram and send it back.
    :return:
    """
    curs = dbconnect()
    sql = "select * from tokens WHERE application=%s"
    curs.execute(sql, (application, ))
    res = curs.fetchall()
    # return a token.
    return -1

@FLASK_APP.route("/<application>/use/<tokenid>")
def increment_app(application, tokenid):
    """
    increment a generic app up once
    :param application:
    :return:
    """
    curs = dbconnect()
    currepoch = time.time()
    sql = "INSERT INTO tokenuse (application, tokenid, usage_time) VALUE (%, %s, %s)"
    data = (application, tokenid, currepoch)
    curs.execute(sql, data)
    return curs.fetchone()


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
        with open(SCHEMAFILE) as infile:
            sql_build_db = infile.read()
        conn = sqlite3.connect(tgt_db)
        curs = conn.cursor()
        curs.executescript(sql_build_db)
        conn.close()


if __name__ == '__main__':
    init_db()
    load_keys()

    # app.run()
