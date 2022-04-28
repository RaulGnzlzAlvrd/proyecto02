import sys
from ..logica.ocultar import ocultar
from ..logica.develar import develar


def main():
    """
    Verifica que los argumentos con los que se ejecuta el programa, sean correctos y si sí lo son, manda a llamar la lógica principal 
    """
    argumentos = sys.argv
    base_dir = "./tests/assets/"
    msg_path = base_dir + "msg.txt"
    img_path = base_dir + "img.jpg"
    modified_img_path = base_dir + "modified_img.png"
    lsb_img_path = base_dir + "lsb_img.png"
    msg_revealed_path = base_dir + "msg_revealed.txt"  
    mensaje = f"""Parámetros inválidos {argumentos[1:]}

Uso:    python -B src/main.py [option]

Opciones:
    -h msg img dest     Oculta el texto del archivo msg usando la imagen img, el resultado lo guarda en dest
    -u img dest         Extrae el mensaje oculto en img y lo guarda el el archivo dest

Ejemplos:
    Cualquiera de los siguientes ejemplos se pueden ejecutar como demo del programa

    Para ocultar:
    python -B src/main.py -h {msg_path} {img_path} {modified_img_path}

    Para develar
    python -B src/main.py -u {lsb_img_path} {msg_revealed_path}"""
    if len(argumentos) <= 1:
        print(mensaje) 
    elif '-h' == argumentos[1] and len(argumentos[2:]) == 3:
        path_texto = argumentos[2]
        path_img = argumentos[3]
        path_destino = argumentos[-1]
        ocultar(path_texto, path_img, path_destino)
    elif '-u' == argumentos[1] and len(argumentos[2:]) == 2:
        path_img = argumentos[2]
        path_destino_texto = argumentos[-1]
        develar(path_img, path_destino_texto)
    else:
       print(mensaje)
