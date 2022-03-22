from flask import flask

app = Flask(__name__)

@app.get("/")
def index():
    return "CONNECTED"
    