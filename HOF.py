


#Se define una funcion completamente normal
def increment(x):
    return x + 1


# Se define una funcion que recibe como parametro otra funcion 
# Dicha funcion parametro no corresponde a una funcion definida, solamene corresponde con el parametro con el que se está operando dentro de la funcion 
# Notese que las x si corresponden entre la hof y la funcion normal, pero la funcion no tiene que hacerlo
def hof(x, func):
    return x +func(x)

# Al utilizar la hof, se debe asignar a una variable, y ademas NO SE LE DA PARAMETRO A LA FUNCION PARAMETRO
result = hof(2, increment)

print(result)

# Definiendo la misma funcion superior anterior con funcion Lamda

# Funcion normal 
increment2 = lambda x: x +1

# Hof
hof2 = lambda x, func: x + func(x)
result2 = hof2(2, increment2)
print(result2)


#----------------------------------------------------------

# Map: hof que permite transformar cada elemento de una lsita
# # la funcion lambda dentro de map revibe 3 grupos de instrucicones: los parametros, la operacion y la/las listas a operar 

numbers = [1, 2, 3, 4]
numbers2 = list(map(lambda i: i * 2, numbers))
print(numbers2)


# Filter: hof para filtrar con un condicional

numeros = [1, 2, 3, 4]
numeros2 = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros2)


# Reduce: hof para volver toda una lista en un solo valor 
# Reduce hay que importarlo!
import functools

lista = [1, 2, 3, 4]
resultado = functools.reduce(lambda counter, item: counter + item, lista )
print(resultado)