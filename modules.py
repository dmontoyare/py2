#Algunos modulos 

import sys
print(sys.path)

import re
text = 'Mi numero de telefono es 311 123 121, el codigo del pais es 57, mi numero de la suerte 3'
result = re.findall('[0-9]+', text)
print(result)

import time
timestamp = time.time()
print(timestamp)

local = time.localtime()
result = time.asctime(local)
print(result)

import collections
numbers = [1,1,2,1,2,1,4,5,3,3,21]
counter = collections.Counter(numbers)
print(counter)

# """Se pueden crear los propios modulos, un modulo es cualquier archivo .py
# se utiliza para para guardar funciones, clases o variables en otro archivo para segmentar 
# la informacion y hacer mas mantenible el codigo 
# 
# los modulos se importan con la palabra import [nombre del archivo sin extencion]
# 
# para llamar variables de un modulo que se haya importado usar :
# modulo.variable 
# 
# 
# un aquete es una carpeta con varios modulos de python
# para importar un solo modulo de un paqute así:
# from paquete import modulo"""