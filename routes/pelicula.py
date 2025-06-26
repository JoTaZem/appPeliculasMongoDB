from bson import ObjectId
from flask import request
from models.pelicula import Pelicula
from models.genero import Genero
from app import app, db

@app.route("/pelicula/",methods=["POST"])
def agregarPelicula():
    try:
        mensaje = None
        estado = False
        if request.method == 'POST':
            datos = request.get_json(force=True)
            genero = Genero.objects(id=ObjectId(datos['genero'])).first() 
            if genero is not None:
                pelicula = Pelicula(**datos)
                pelicula.save()
                estado = True
                mensaje = "Pelicula agregada correctamente"
            else:
                mensaje = "Genero no encontrado"
        else:
            mensaje = "Metodo no permitido"
    except Exception as error:
        mensaje = str(error)
        if "duplicate key error" in mensaje:
            mensaje = "Error Ya existe una pelicula con ese codigo"
    return {"estado": estado, "mensaje": mensaje}

@app.route("/pelicula/",methods=["GET"])
def listarPeliculas():
    try:    
        mensaje = None
        peliculas = Pelicula.objects()
    except Exception as error:
        mensaje = str(error)
    return {"mensaje": mensaje, "peliculas": peliculas}

@app.route("/pelicula/", methods=["PUT"])
def actualizarPelicula():
    try:
        mensaje= None
        estado = False
        if request.method == 'PUT':
            datos = request.get_json(force=True)
            pelicula = Pelicula.objects(id=ObjectId(datos['id'])).first()
            if pelicula is not None:
                pelicula.codigo = datos['codigo']
                pelicula.titulo = datos['titulo']
                pelicula.protagonista = datos['protagonista']
                pelicula.duracion = datos['duracion']
                pelicula.resumen = datos['resumen']
                pelicula.foto = datos['foto']
                pelicula.genero = ObjectId(datos['genero'])
                pelicula.save()
                estado = True
                mensaje = "Pelicula actualizada correctamente"
    except Exception as error:
        mensaje = str(error)
    return {"estado":estado,"mensaje": mensaje}

@app.route("/pelicula/<string:idPeli>",methods=["DELETE"])
def eliminarPelicula(idPeli):
    try:
        mensaje = None
        estado = False
        if request.method == 'DELETE':    
            pelicula = Pelicula.objects(id=idPeli).first()
            if pelicula is not None:
                pelicula.delete()
                estado = True
                mensaje = "Pelicula eliminada correctamente"
            else:
                mensaje = "Pelicula no encontrada"
        else:
            mensaje = "Metodo no permitido"
    except Exception as error:
        mensaje = str(error)
    return {"estado": estado, "mensaje": mensaje}