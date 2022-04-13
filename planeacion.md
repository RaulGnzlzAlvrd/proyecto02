## Subtareas a realizar
- Leer los parámetros al momento de ejecutar el programa
- Validar cantidad de parámetros (-h img_path
txt_path dest_path, -u img_path txt_path)

En caso de **Ocultar**:
- Revisar si existe la imágen del parámetro img_path
- Cargar la imágen en memoria
- Convertir la imágen a su representación matricial
- Revisar si existe el archivo txt del parámetro txt_path
- Cargar el contenido del archivo txt a memoria
- Obtener codificación binaria del mensaje (con
símbolo de fin de mensaje)
- Construir el alfabeto a usar y su
codificación/decodificación
- Modificar el bit menos significativo dependiendo
del mensaje codificado
- Crear imágen en dest_path con los nuevos
datos de imágen modificados 

En caso de **Develar**
- Revisar si existe la imágen del parámetro img_path
- Cargar la imágen a memoria
- Convertir la imágen a su representación matricial
- Extrar el bit menos significativo de los datos de la imágen
- Decodificar los datos binarios a string
- Escribir archivo en txt_path con el mensaje decodificado

## ¿Qué podría malir sal?
- Que los archivos de texto o imágen no existan
- Que los archivos estén dañados
- Que no se tenga permiso para leer o escribir
alguno de los archivos
- Que el tamaño del mensaje codificado supere
la cantidad de bytes en la imágen
- Que el texto contenga caracteres no válidos
- Que la imagen a develar no tenga ningún mensaje
válido.
- Que la imagen sea demasiado grande para procesarla
en memoria

-----

## Agrupando funcionalidades

#### Interfaz de usuario:
- Tomar los parámetros y validar que sean correctos.
- Mandar llamar las funcionalidades base del programa
(ocultar, develar) con los parámetros. 
- Imprimir mensajes o excepciones al usuario

#### Lógica primaria
Usar cualquier funcionalidad para componer el algoritmo
base de:
- Ocultar
- Develar

#### Lectura/Escritura
- De un path devolver matriz de pixeles
- De matriz de pixeles se crea una imágen
- De un path devolver el texto plano (string)
- De texto plano se crea un archivo de texto
- Validar existencia, integridad y permisos de archivos
- (Opcional) Validar tamaño al cargar en memoria

#### Codificador/Decodificador
- Definir un código (alfabeto y número de bits)
- Definir un símbolo de fin de mensaje
- Obtener binario a partir de mensaje
- Obtener mensaje a partir de binario
- Validar que el tamaño al codificar el mensaje sea
de cierto tamaño
- Detectar códigos no válidos al codificar/decodificar

#### Método LSB
Usando el bit menos significativo (LSB):
- Guardar un binario en una matríz de pixeles
- Extraer el binario de una matríz de pixeles
