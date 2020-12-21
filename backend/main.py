import flask
import json
from random import randint
import idgen
import tyanitolkay

app = flask.Flask(__name__, template_folder='../frontend', static_folder='../frontend/static')


@app.route('/', methods=['GET', 'POST'])
def main_page():
    if flask.request.method == 'POST':
        link = flask.request.form['text']
        print(link)
        urls = tyanitolkay.pull()['idlist']
        unic_ids = list(urls.keys())
        original_links = list(urls.values())
        if link in original_links:
            return flask.render_template('index.html', link=f"{flask.request.base_url}/{unic_ids[original_links.index(link)]}")
        else:
            print(unic_ids)
            new_id = idgen.idgen(unic_ids)
            tyanitolkay.add({new_id: link})
            return flask.render_template('index.html', link=f"{flask.request.base_url}/{new_id}")
    else:
        return flask.render_template('index.html')

@app.route('/<id>')
def redirect(id):
    links = tyanitolkay.pull()['idlist']
    if id in links:
        return flask.redirect(links[id])
    else:
        return flask.redirect('/404')

@app.route('/404')
def page_404():
    return flask.render_template('page404.html')
