from flask import Flask
from flask_mongoengine import MongoEngine
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)

app.config[ 'UPLOAD_FONDER'] = './static/images/'
app.config['MONGODB_SETTINGS'] =[
    {
        'db': 'peliculasMongoDB',
        'host': os.environ.get('URI')  # Use the URI from the .env file
        #'port': 27017
    }
]
db = MongoEngine(app)

if __name__ == '__main__':
    from routes.genero import *
    from routes.pelicula import * 
    app.run(debug=True,port=5000,host='0.0.0.0')