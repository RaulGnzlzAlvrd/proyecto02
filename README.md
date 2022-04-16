# Modelado y Programación 2022-2, Proyecto 2 - Esteganografía por el método LSB 

## Integrantes del equipo:
- Camargo Fortiz Miriam: 313056459
- González Alvarado Raúl: 313245312
- Novella Jiménez Maria Rebeca: 313143926

## Instrucciones de uso
- Instalar dependencias `pip install -r requirements.txt`
- Para ejecutar depende de la acción a realizar:
	- Ocultar: `python -B src/main.py -h txt_path img_path dest_path` donde `img_path` es el path de la imagen donde se va a ocultar el texto del archivo `txt_path`, y la imágen final estará en `dest_path`.
	- Develar: `python -B src/main.py -u img_path txt_path`, donde la imagen de donde se saca el mensaje es `img_path` y el texto resultante estará en `txt_path`

> **Nota 1:** Si se ocupan path relativos, deben ser relativos al directorio base del proyecto.

> **Nota 2:** La opción `-B` es para que no se generen archivos cache.

## Instrucciones de testeo
Para ejecutar los tests, desde el directorio raíz (este mismo directorio) ejecutar:
```
python -Bm unittest -v
```
