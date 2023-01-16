from CaluladoraEnyda import sumar, restar, multiplicar, raiz, exponente, seno


def operaciones():
    print("Caculadora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Raiz")
    print("6. Exponente")
    print("7. Seno")
    print("Seleccione una Operación")


def obtenerResultado(opcion):
    if opcion == "1":
        print("1: Sumar ")
        print("Ingrese el Primer Valor ")
        valorUno = input()
        print("Ingrese el Segundo Valor ")
        valorDos = input()
        print("El Resultado es: ")
        print(sumar(valorUno,valorDos))
    elif opcion == "2":
        print("2: Restar")
        print("Ingrese el Primer Valor ")
        valorUno = input()
        print("Ingrese el Segundo Valor ")
        valorDos = input()
        print("El Resultado es: ")
        print(restar(valorUno, valorDos))
    elif opcion == "3":
        print("3: Multiplicar")
        print("Ingrese el Primer Valor ")
        valorUno = input()
        print("Ingrese el Segundo Valor ")
        valorDos = input()
        print("El Resultado es: ")
        print(multiplicar(valorUno, valorDos))
    elif opcion == "4":
        print("4: Dividir")
        print("Ingrese el Primer Valor ")
        valorUno = input()
        print("Ingrese el Segundo Valor ")
        valorDos = input()
        print("El Resultado es: ")

    elif opcion == "5":
        print("5: Raiz N")
        print("Ingrese un valor")
        valorUno = input()
        print("El Resultado es: ")
        print(raiz(valorUno))
    elif opcion == "6":
        print("6: Exponente")
        print("Ingrese la Base")
        valorUno = input()
        print("Ingrese el Exponente ")
        valorDos = input()
        print("El Resultado es: ")
        print(exponente(valorUno,valorDos))
    elif opcion == "7":
        print("7: Seno")
        print("Ingrese un valor")
        valorUno = input()
        print("El Resultado es: ")
        print(seno(valorUno))
