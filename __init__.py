from flask import Flask
from flask_mongoengine import MongoEngine
from config import *
def create_app():
    app = Flask(__name__)
    app.config[ 'UPLOAD_FONDER'] = './static/images/'
    app.config['MONGODB_SETTINGS'] =[Config.crearConfig()]
    return app