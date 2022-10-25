
#"""Asignar parametros por defecto 
# y consegeguir varios returns"""


# Sin parametros por defecto
def vol(length, width, depth):
    a = length * width * depth
    print (a)

vol(1, 4, 6)

#Asignando parametros por defecto
def volumen(length=1, width=4, depth=6):
    a = length * width * depth
    print (a)

volumen()


# Devolver varios Returns, se separa por comas luego de la palabra return
# El resultado de se retorna a manera de tupla 

def area(length, width):
    return length * width, "Hola"
    

result = area(5, 2)
print(result)

