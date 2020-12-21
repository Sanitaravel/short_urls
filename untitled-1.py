from flask import Flask

app = Flask(__name__)

d = {}
@app.route('/stats/<short_url>')
def f(short_url):
    global d
    if short_url not in d.keys():
        d[short_url] = 1
    else:
        d[short_url] += 1
    return str(d[short_url])

if __name__ == "__main__":
    app.run()