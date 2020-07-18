from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)
Bootstrap(app)
# API Credentials. Set your API Key and Secret here
API_KEY = 'acc_4a6c2f06b5c84c3'
API_SECRET = '2fe0687c4aec182b27a4516ff91c0007'
ENDPOINT = 'https://api.imagga.com/v2/categories/nsfw_beta'
auth = HTTPBasicAuth(API_KEY, API_SECRET)
@app.route('/', methods=['GET', 'POST'])
def index():
    image_url = None
    res = None
    if request.method == 'POST' and 'image_url' in request.form:
        image_url = request.form['image_url']
        response = requests.get(
           '%s?image_url=%s' % (ENDPOINT, image_url),
           auth=auth)
        try:
            res = response.json()
        except Exception as e:
            print('Exception in JSON decode:')
            print(e)
            print(response.content, response.status_code)
    return render_template('index.html', image_url=image_url, res=res)
if __name__ == '__main__':
    app.run(debug=True)