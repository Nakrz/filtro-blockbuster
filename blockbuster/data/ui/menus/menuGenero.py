menuGenero = ['Crear Genero','Listar Generos','Ir Menu principal']

def menuGeneroP ():
    isMenuGenero = True
    header = """""
    ++++++++++++++++++++++++++++++++++++++
    +        GESTOR DE GENERO            +
    ++++++++++++++++++++++++++++++++++++++
    """""
    
    print(header)
    while (isMenuGenero):
        for i,item in enumerate(menuGenero):
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
                isMenuGenero = False


menuGeneroP ()