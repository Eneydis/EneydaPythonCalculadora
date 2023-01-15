import numpy
import math


# Sumar
def sumar(valorUno, valorDos):
    return int(valorUno) + int(valorDos)


# Restar
def restar(valorUno, valorDos):
    return int(valorUno) - int(valorDos)


# Multiplicación

def multiplicar(valorUno, valorDos):
    return int(valorUno) * int(valorDos)


# Division

def dividir(valorUno, valorDos):
    return int(valorUno) / int(valorDos)


# Raiz

def raiz(valor1):
    return math.sqrt(int(valor1))


# Exponente

def exponente(base1, exponente):
    return math.pow(int(base1), int(exponente))


# Seno

def seno(valor1):
    return numpy.sin(int(valor1))