from flask import Flask, jsonify
 

def create_app(testing: bool = True):
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "<h1>XEROHOME API 2.0</h1><br><b>Status: </b>Connected.<br><b>Production:</b> {testing}"

    @app.route("/status")
    def status():
        return jsonify({"status": "Connected"})


    return app
