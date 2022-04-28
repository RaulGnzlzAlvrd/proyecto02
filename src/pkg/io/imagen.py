from PIL import Image 
import numpy as np
def get_pixeles_imagen(path_imagen):
    """
    path_imagen: string

    return matriz
    """
    img = Image.open(path_imagen) 
    numpydata = np.array(img) 
  
    return numpydata
    

def crea_imagen(matriz_pixels, path_destino):
    """
    matriz_pixels: matriz de numpy de 3 dimensiones
    path_destino: string

    return None
    a = np.array(matriz_pixels)
    np.savetxt(path_destino, a, delimiter =', ')
    """
    pil_image=Image.fromarray(matriz_pixels).save(path_destino)
    
    return None
    
