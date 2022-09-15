import os
from api import create_app

app = create_app(host=os.environ.get('MONGO_URI'),
                db=os.environ.get('DATABASE'))

if __name__ == '__main__':
    app.debug = True
    app.run(debug=True)
