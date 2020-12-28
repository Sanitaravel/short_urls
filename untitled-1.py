from flask import Flask

app = Flask(__name__)

d = {}
@app.route('/stats/<short_url>/')
def f(short_url):
    global d
    if short_url not in d.keys():
        d[short_url] = 1
    else:
        d[short_url] += 1
    if d[short_url] in [2, 3, 4]:
        s = 'ѕользователи проходили по этой ссылке ' + str(d[short_url]) + ' раза'
    else:
        s = 'ѕользователи проходили по этой ссылке ' + str(d[short_url]) + ' раз'
    return s

if __name__ == "__main__":
    app.run()