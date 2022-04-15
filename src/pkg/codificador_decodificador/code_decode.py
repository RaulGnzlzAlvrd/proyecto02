import numpy as np 


def llena_codigo():
    """
    Devuelve el código de símbolo a bist
    
    return: diccionario 
    """
    codigo = {}
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ /"
    numero = 0
    for letra in alfabeto:
        codigo[letra] = np.binary_repr(numero,5)
        numero += 1
    return codigo    



def get_bits(mensaje):
    """
    Devuelve una codificación asociada al mensaje 
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
    try:
        for bit in bits: 
            cadena += bit
            if cadena == "11011":
                return mensaje
            if contador % 5 == 0:
                mensaje += volteado[cadena]
                cadena = ""
            contador += 1
    except: 
        print("Codificación no válida")        

def voltea_codigo(codigo):
    """
    devuelve el código de bits a símobolo

    return: Diccionario 
    """
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
    return len(mensaje*5)+5 <= limite
