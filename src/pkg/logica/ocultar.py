from ..codificador_decodificador.code_decode import get_bits, valida_tamanio
from ..io.imagen import get_pixeles_imagen, crea_imagen
from ..lsb.lsb import guarda_bits
from ..io.texto import leer

def ocultar(path_mensaje, path_imagen, path_destino):
    """
    Oculta el mensaje dentro del archivo en path_mensaje en la 
    imágen en path_imagen. La imágen resultante se guarda en
    path_destino

    params:
    path_mensaje: string
    path_imagen: string
    path_destino: string

    return None
    """
    mensaje = leer(path_mensaje)
    pixeles = get_pixeles_imagen(path_imagen)
    if not valida_tamanio(mensaje, pixeles.size):
        raise Exception("Mensaje demasiado grande")
    mensaje_codificado = get_bits(mensaje)
    pixeles_modificados = guarda_bits(mensaje_codificado, pixeles)
    crea_imagen(pixeles_modificados)
