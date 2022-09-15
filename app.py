import os
from flask import Flask
from flask_cors import CORS
from mongoengine import connect

# import routes
from api.user import user_route

app = Flask(__name__)
app.register_blueprint(user_route)

CORS(app)

connect(host=os.environ.get('MONGO_URI'), db='arteria')

if __name__ == "__main__":
    app.debug = True
    app.run(debug=True)
