from flask import Flask
from flask_cors import CORS
from mongoengine import connect

# import routes
from api.routes.user import user_route
from api.routes.home import home_route


def create_app(db, host, uuidRepresentation='standard'):
    app = Flask(__name__)
    app.register_blueprint(user_route)
    app.register_blueprint(home_route)

    CORS(app)

    connect(host=host, db=db, uuidRepresentation=uuidRepresentation)

    return app
