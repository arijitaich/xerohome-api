

# from curses import flash
from flask import Flask, jsonify

def create_app(test_config=None):
    
    
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY = "dev"
        )

    else:
        app.config.from_mapping(test_config)


    @app.route("/")
    def index():
        return "Connected: {test_config}"

    @app.route("/status")
    def status():
        return jsonify({"status": "Connected"})

    return app