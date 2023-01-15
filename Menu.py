from procesamiento import operaciones, obtenerResultado


def calculadora():
    programa = True
    while programa:
        operaciones()
        opcion = input()
        obtenerResultado(opcion)
        print("Para Continuar con la Caludadora cualquier otro numero")
        print("9. Repetir Operación")
        print("0. Salir")
        segundaOpcion = input()
        if segundaOpcion == "9":
            print("Usted Quiere Repetir la Misma Opcion")
            obtenerResultado(opcion)
            print("Para Continuar con la Caludadora cualquier otro numero")
            print("9. Repetir Operación")
            print("0. Salir")
            segundaOpcion = input()
        if segundaOpcion == "0":
            print("Gracias por usuar la Calculadora")
            programa = False


calculadora()
