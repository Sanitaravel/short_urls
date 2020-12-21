import flask
import json
from random import randint
app = flask.Flask(__name__, template_folder='../frontend', static_folder='../frontend/static')


@app.route('/', methods=['GET', 'POST'])
def main_page():
    if flask.request.method == 'POST':
        link = flask.request.form['link']

    return flask.render_template('index.html')
