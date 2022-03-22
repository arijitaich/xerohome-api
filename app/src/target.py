from flask import Blueprint

target = Blueprint("target", __name__, url_prefix="/api/v2/target")

@target.get('/')
def get_all():
    return {"targets": []}

