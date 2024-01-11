menuActores = ['Crear Actor','Listar Actor','Ir Menu principal']

def menuActoresP ():
    isMenuActor = True
    header = """""
    ++++++++++++++++++++++++++++++++++++++
    +        GESTOR DE ACTORES           +
    ++++++++++++++++++++++++++++++++++++++
    """""
    
    print(header)
    while (isMenuActor):
        for i,item in enumerate(menuActores):
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
                isMenuActor = False


menuActoresP ()