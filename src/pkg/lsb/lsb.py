import numpy as np

def modifica_lsb(numero, bit):
    """
    Si bit es 0, entonces vuelve 0 el bit menos significativo
    del numero; si bit es 1, entonces vuelve 1 el bit menos
    significativo de numero
    
    params: 
    numero: number
    bit: "0" o "1"
    
    returns el número modificado
    """
    operations = {
            "0": lambda n: n & 254,
            "1": lambda n: n | 1
        }
    return operations[bit](numero)

def guarda_bits(bits, matriz_pixeles):
    """
    Guarda los bits en la matriz_pixeles usando la técnica
    del bit menos significativo. Regresa una copia de matriz_pixeles
    ya modificada.

    params:
    bits: string
    matriz_pixels: matriz de numpy de dimenesión 3

    return matriz de numpy de dimensión 3
    """
    aplanada = matriz_pixeles.reshape(-1).copy()
    for i in range(len(bits)):
        aplanada[i] = modifica_lsb(aplanada[i], bits[i])
    return aplanada.reshape(matriz_pixeles.shape)

def extrae_bits(matriz_pixeles):
    """
    Saca los bits menos significativos de una matriz de pixeles
    y los devuelve como cadena de bits

    params:
    matriz_pixeles: matriz de numpy de 3 dimensiones

    return string de ceros y unos
    """
    aplanada = matriz_pixeles.reshape(-1)
    bits = ""
    contador = 1
    cadena = ""
    for number in aplanada:
        cadena += str(number & 1)
        if contador % 5 == 0:
            bits += cadena
            if cadena == "11011":
                break
            cadena = ""
        contador += 1
    return bits
