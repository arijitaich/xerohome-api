from flask import Flask, jsonify
 

def create_app(testing: bool = True):
    app = Flask(__name__)

    @app.route("/")
    def index():
        return f"Connected: {testing}"

    @app.get("/status")
    def status():
        return jsonify({"status": "Connected"})

    return app
