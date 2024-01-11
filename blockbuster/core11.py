import json
import os

BASEDATA = 'data/peliculas.json'

def NewFile (data):
    with open (BASEDATA,'w') as archivo:
        json.dump(data,archivo,indent = 2)

def AddData (id):
    data = readFile()
    if id in data:
        print(f"Ya existe {id}")
    else:
        data = {'id':'P93'}
        # data[nombre] = "xxxxxx"
        # data[duracion] = "xxxxxx"
        # data[sinopsis] = "xxxxxx"
        # data[generos] = "xxxxxx"
        NewFile(data)
        print("Pelicula registrada exitosamente!")
        os.system ("pause")
        os.system("cls")

def readFile ():
    if os.path.isfile (BASEDATA):
        with open (BASEDATA, 'r') as rf:
            return json.load (rf)
    else:
        return{}