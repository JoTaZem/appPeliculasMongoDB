from dotenv import load_dotenv
import os

load_dotenv()

class Config():

    def crearConfig():
        config= {
            'db': os.environ.get('DB'),  # Use the DB from the .env file
            'host': os.environ.get('URI'),  # Use the URI from the .env file
            #'port': os.environ.getenv('PORT')  # Use the PORT from the .env file or default to 5000
        }
        return config