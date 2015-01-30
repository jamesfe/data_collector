"""
A server that serves tokens.
"""

from flask import Flask
import json
import sqlite3

app = Flask(__name__)


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

if __name__ == '__main__':
    app.run()