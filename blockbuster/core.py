import json

BASEDATA = 'data/peliculas.json'

def NewFile (data):
    with open (BASEDATA,'w') as archivo:
        json.dump(data,archivo,indent = 2)

def cargarDatos ():
    try:
        with open('data/peliculas.json','r') as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        datos = {}
    return datos


def guardarDatos (datos):
    with open ('data/peliculas.json','w') as archivo:
        json.dump(datos,archivo,indent = 4)


def registrarPelicula (id,nombre,duracion,sinopsis,generos):
    peliculas = cargarDatos ()
    pelicula = {'id':id,'nombre':nombre,'sinopsis':sinopsis, 'duracion':duracion,'generos':generos}
    peliculas.append(pelicula)
    guardarDatos(peliculas)   


def buscarPelicula (peliculas):
    peliculas = cargarDatos()
    for pelicula in peliculas:
        if pelicula ['id'] == id:
            return pelicula
    return None


def editarPelicula (id,nuevoNombre,nuevoPrecio,etc):
    peliculas = cargarDatos()
    for pelicula in peliculas:
        if peliculas['id'] == 'id':
            peliculas['id'] == 'nueva id'
            peliculas['nombre'] == nuevoNombre
            peliculas['precio'] == nuevoPrecio
            guardarDatos (peliculas)
            return True
        return False
    

    
def eliminarPelicula (id):
    peliculas = cargarDatos ()
    peliculas = [pelicula for pelicula in peliculas if pelicula ['id'] != 'id']
    guardarDatos(peliculas)




    

    
    
