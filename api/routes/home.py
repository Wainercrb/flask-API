from flask import Blueprint

home_route = Blueprint('home_route', __name__)


@home_route.route('/', methods=['GET'])
def home():
    return 'Welcome to flask-API'
