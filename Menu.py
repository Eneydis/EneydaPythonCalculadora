

def calculadora():
    programa = True
    while programa:
        print("Hello")
        print("Agrega el Primer Numero")
        numeroUno = input()

        print("Agrega el Segundo Numero")
        numeroDos = input()
        opcion = input()
        if opcion == "11":
            print("Misma Opcion")
        if opcion == "12":
            print("Salido")
            programa = False


calculadora()