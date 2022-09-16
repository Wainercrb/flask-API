import os
from api import create_app

HOST = os.environ.get('MONGO_URI')
DB = os.environ.get('DATABASE')
app = create_app(host=HOST, db=DB)

if __name__ == '__main__':
    app.debug = True
    app.run(debug=True)
