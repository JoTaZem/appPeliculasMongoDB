from flask import request
from models.genero import Genero
from app import app, db

@app.route("/genero/", methods=["GET"])
def listarGeneros():
    try:
        mensaje = None
        generos=Genero.objects()
        if not generos:
            mensaje = "No hay generos..."
        else:
            mensaje = "consulta Exitosa"
    except Exception as error:
        mensaje=str(error)
    return {"mensaje":mensaje, "generos": generos}

@app.route("/genero/<id>", methods=["GET"])
def obtenerGenero(id):
    try:
        mensaje = None
        genero = Genero.objects.get(id=id)
        if not genero:
            mensaje = "Genero no encontrado"
        else:
            mensaje = "Consulta exitosa"
    except Exception as error:
        mensaje=str(error)
    return {"mensaje":mensaje, "genero": genero}

@app.route("/genero/", methods=["POST"])
def agregarGenero():
    try:
        mensaje = None
        estado =  False
        if request.method =='POST':
            datos=request.get_json(force=True)
            genero = Genero(**datos)
            genero.save()
            estado = True
            mensaje = "Genero agregado correctamente"
        else:
            mensaje = "Metodo no permitido"
    except Exception as error:
        mensaje=str(error)
    return {"estado":estado,"mensaje": mensaje}

@app.route("/genero/<id>", methods=["PUT"])
def actualizarGenero(id):
    try:
        mensaje = None
        estado = False
        if request.method == 'PUT':
            datos = request.get_json(force=True)
            genero = Genero.objects.get(id=id)
            genero.update(**datos)
            estado = True
            mensaje = "Genero actualizado correctamente"
        else:
            mensaje = "Metodo no permitido"
    except Exception as error:
        mensaje = str(error)
    return {"estado": estado, "mensaje": mensaje}

@app.route("/genero/<id>", methods=["DELETE"])
def eliminarGenero(id):
    try:
        mensaje = None
        estado = False
        if request.method == 'DELETE':
            genero = Genero.objects.get(id=id)
            genero.delete()
            estado = True
            mensaje = "Genero eliminado correctamente"
        else:
            mensaje = "Metodo no permitido"
    except Exception as error:
        mensaje = str(error)
    return {"estado": estado, "mensaje": mensaje}


