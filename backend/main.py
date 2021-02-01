import flask
import idgen as idgen
import tyanitolkay as tyanitolkay

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
            return flask.render_template('index.html',
                                         link=f"{flask.request.base_url}/{unic_ids[original_links.index(link)]}")
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


@app.route('/stats/<short_url>/')
def f(short_url):
    global d
    if short_url not in d.keys():
        d[short_url] = 1
    else:
        d[short_url] += 1
    if d[short_url] in [2, 3, 4]:
        s = '������������ ��������� �� ���� ������ ' + str(d[short_url]) + ' ����'
    else:
        s = '������������ ��������� �� ���� ������ ' + str(d[short_url]) + ' ���'
    return s


@app.route('/404')
def page_404():
    return flask.render_template('page404.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
