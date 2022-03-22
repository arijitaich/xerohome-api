from flask import Flask

def create_app(testing: bool = True):
    app = Flask(__name__)

    @app.route("/")
    def index():
        return f"Connected: {testing}"

    # @app.get("/")
    # def index():
    #     return "CONNECTED"

    return app
