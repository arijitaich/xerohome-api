from flask import Blueprint

auth = Blueprint("auth", __name__, url_prefix="/api/v2/auth")

@auth.post('/register')
def register():
    return "User created"

@auth.get("/me")
def me():
    return {"user":"me"}