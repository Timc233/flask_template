from flask import Blueprint

home = Blueprint('home', __name__)

@home.route('/')
def index():
    return '<h1>This is the home page<h1>'