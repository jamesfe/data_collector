"""
A server that serves tokens for the gathering of social media.
Twitter: @jimmysthoughts
GitHub: github.com/jamesfe
"""
from __future__ import (absolute_import, division, print_function, unicode_literals)

from flask import Flask
from os import listdir
from os.path import join
import psycopg2
import psycopg2.extras
import time

FLASK_APP = Flask(__name__)

KEYDIR = '../keys/'
SCHEMAFILE = "../sql/tokenserver.sql"


@FLASK_APP.route('/<application>/gettoken/')
def get_token(application):
    """
    Get a token for instagram and send it back.
    :return:
    """
    conn, curs = dbconnect()

    sql = "select token_id, use_period_secs, max_uses, client, application, secret," \
          "username, token from tokens WHERE application=%s"
    curs.execute(sql, (application, ))
    token_results = curs.fetchall()
    # Given some number of uses of the token, we
    for res in token_results:
        print(res)
        tokenid = res[0]
        usage_cutoff = int(time.time()) - res[1]
        usage_sql = "SELECT COUNT(*) as num_uses FROM token_use WHERE token_id=%s AND usage_time > %s"

        curs.execute(usage_sql, (tokenid, usage_cutoff))
        num_uses = curs.fetchone()[0]
        if num_uses < res[2]:
            return res
    return -1


@FLASK_APP.route("/<application>/use/<tokenid>")
def increment_app(application, tokenid):
    """
    increment a generic app up once
    :param application:
    :return:
    """
    conn, curs = dbconnect()

    currepoch = time.time()
    sql = "INSERT INTO token_use (application, tokenid, usage_time) VALUE (%, %s, %s)"
    data = (application, tokenid, currepoch)
    curs.execute(sql, data)
    return curs.fetchone()


def dbconnect():
    """
    connect to the db
    :return:
    """

    conn_str = "dbname='jimmy1' user='jimmy1' " \
               "host='localhost' " \
               "port='5432' "
    conn = psycopg2.connect(conn_str)
    curs = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    return conn, curs


def load_keys():
    """
    Load a set of keys from various databases
    :return:
    """
    conn, curs = dbconnect()

    keys = [_ for _ in listdir(KEYDIR) if _[-6:].lower() == 'sqlkey']
    for key in keys:
        sql_stmt = open(join(KEYDIR, key)).read()
        print(sql_stmt)
        curs.execute(sql_stmt)
    conn.commit()


def init_db():
    """
    If a DB doens't already exist, just create one.
    :return:
    """
    conn, curs = dbconnect()

    curs.execute(open(SCHEMAFILE, "r").read())
    conn.commit()



if __name__ == '__main__':
    init_db()
    load_keys()

    # app.run()
