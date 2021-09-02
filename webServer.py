from flask import Flask
from threading import Thread

"""
This program creates a web server with flask witch
is pinged every 5' so Replit keeps out bot alive
"""

app = Flask('')


@app.route('/')
def home():
    return "Hello. I am alive!"


def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()
