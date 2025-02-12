import os
from flask import Flask
from requests import get

app = Flask(__name__)
base_url = "https://124.49.55.153/"
base_hea = {
        'Host': 'torrentqq354.com',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        }

@app.route("/")
def main():
    resp = get(base_url, headers=base_hea, verify=False)
    return resp.raw.read(), resp.status_code, resp.headers.items()

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
