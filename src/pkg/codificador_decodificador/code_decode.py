import numpy as np 


def llena_codigo():
    codigo = {}
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ /"
    numero = 0
    for letra in alfabeto:
        codigo[letra] = np.binary_repr(numero,5)
        numero += 1
    return codigo    



def get_bits(mensaje):
    """
    mensaje: string

    return string
    """
    bits = ""
    codigo = llena_codigo()
    for letra in mensaje:
        bits += codigo[letra]
    
    return bits + "11011"


def get_mensaje(bits):
    """
    Devuelve el mensaje asociado a la cadena de bits,
    en caso de que no sea una codificación válida
    lanza una excepción

    bits: string

    return string
    """
    contador = 1
    cadena = ""
    mensaje = ""
    volteado = voltea_codigo(llena_codigo())
    bits2 = bits[:-5]
    for bit in bits2: 
        cadena += bit
        if contador % 5 == 0:
            mensaje += volteado[cadena]
            cadena = ""
        contador += 1
    return mensaje 

def voltea_codigo(codigo):
    volteado = dict(zip(codigo.values(), codigo.keys()))
    return volteado

def valida_tamanio(mensaje, limite):
    """
    Verifica que el mensaje codificado sea menor o
    igual que cierto límite

    mensaje: string
    limite: number

    return boolean
    """
    pass
