import os
import core11 as c


menuBlockbuster = ['Administrador de Generos','Administrador de Actores','Administrador de Formatos','Gestor de Informes','Salir']


def menuPrincipalBlock ():
    isMenuBlockb = True
    header = """""
            ++++++++++++++++++++++++++++++++++++++++++++++++++
            +    SISTEMA GESTOR DE PELICULAS BLOCKBUSTER     +
            ++++++++++++++++++++++++++++++++++++++++++++++++++
    """""
    
    print(header)
    while (isMenuBlockb):
        for i,item in enumerate(menuBlockbuster):
            print(f'{i+1} - {item}')
        try:
            op = int(input("Seleccione la opcion que desee: "))
        except ValueError:
            print("Opcion no valida")
        else:   
            if (op == 1):
                pass
            elif(op == 2):
                pass
            elif(op == 3):
                pass
            elif(op == 4):
                pass
            elif(op == 5):
                pass
            elif(op == 6):
                isMenuBlockb = False

menuPrincipalBlock ()

