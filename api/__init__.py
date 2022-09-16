from flask import Flask
from flask_cors import CORS
from mongoengine import connect, disconnect
from mongoengine.connection import _get_db
from model import get_model_list

# import routes
from api.routes.user import user_route
from api.routes.home import home_route
# end - import routes


def create_app(db, host, uuidRepresentation='standard'):
    app = Flask(__name__)
    app.register_blueprint(user_route)
    app.register_blueprint(home_route)

    CORS(app)

    connect(host=host, db=db, uuidRepresentation=uuidRepresentation)

    return app


def hanbleDisconnectDatabase():
    disconnect()


def hanbleDropCollection():
    try:
        db = _get_db()
        for model in get_model_list():
            db.drop_collection(model)

    except Exception as e:
        print(str(e))
        return str(e)
