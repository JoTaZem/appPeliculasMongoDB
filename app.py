from __init__ import *


app = create_app()
db = MongoEngine(app)

@app.route("/", methods=["GET"])
def index():
    return "bienvenido a la API de peliculas"


if __name__ == '__main__':
    from routes.genero import *
    from routes.pelicula import * 
    app.run(debug=True,host='0.0.0.0')