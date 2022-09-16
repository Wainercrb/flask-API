import os
import pytest
from api import create_app
from api import hanbleDisconnectDatabase
from api import hanbleDropCollection


HOST = os.environ.get('MONGO_URI')
DB = os.environ.get('DATABASE')


@pytest.fixture(scope="session")
def flask_app():
    app = create_app(host=HOST, db=DB)

    client = app.test_client()

    ctx = app.test_request_context()
    ctx.push()

    yield client

    ctx.pop()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


@pytest.fixture(scope="session")
def app_with_db(flask_app):

    hanbleDropCollection()

    yield flask_app

    hanbleDisconnectDatabase()
