def leer(archivo):
    """
    archivo: string
    return string con el texto del archivo
    """
    documento= open(archivo)
    texto= documento.read()
    cadena_nueva=texto.replace("\n", "")
    return cadena_nueva



def escribe(texto, path_destino):
    """
    Crea un archivo de nombre path_destino con
    contenido texto

    texto: string
    path_destino: string

    return None
    """
    document=open(path_destino, 'w')
    document.write(texto)
    document.close()
    return None
