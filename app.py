from flask import Flask
from os import getenv

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "%s %s" % ('Hello DevopsMeetup')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
