# Comprehensions son listas, diccionarios y conjuntos creados a partir de un cilo for y en una sola linea de comando

#List comprehensions ejemplos
numbers = [i for i in range(1, 11)]
print(numbers)

# Al elemento "i" se puede ver modificado matematicamente
numbers2 = [i * 2 for i in range (1, 11)]
print(numbers2)

# Se pueden agregar condicionales 
numbers3 = [i for i in range(1, 11) if i % 2 == 0]
print(numbers3)

# Diccionarios igual que las lsitas, obviamente lleva clave y valor 
dict1 = {i: i*2 for i in range(1, 11)}
print(dict1)

# Diccionario a partir de una lista 
list = ["Daniel", "Maria", "Juan", "Ramiro"]
dict3 = {i: i[0:1] for i in list}
print(dict3)
