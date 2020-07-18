import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods = ['GET'])

def home():
    return "<h1> This is a test api for small children and huge adults </h1> <p>I could serve up some html here</p>"

app.run()

