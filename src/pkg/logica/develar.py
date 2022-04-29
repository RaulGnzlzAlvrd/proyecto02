from ..codificador_decodificador.code_decode import get_mensaje
from ..io.imagen import get_pixeles_imagen
from ..lsb.lsb import extrae_bits
from ..io.texto import escribe

def develar(path_imagen, path_destino):
    """
    Devela el mensaje (si hay) que esté en path_imagen. 
    El texto resultante se guarda en el archivo path_destino

    params:
    path_imagen: string
    path_destino: string

    return None
    """
    pixeles = get_pixeles_imagen(path_imagen)
    bits_menos_significativos = extrae_bits(pixeles)
    mensaje = get_mensaje(bits_menos_significativos)
    escribe(mensaje, path_destino)
