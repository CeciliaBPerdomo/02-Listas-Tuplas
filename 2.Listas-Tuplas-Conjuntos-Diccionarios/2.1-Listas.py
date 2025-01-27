# Para definir una lista en Python, se utilizan corchetes [] y los elementos de la lista se separan por comas. 
# A continuación, se presentan algunos ejemplos de listas:

# Lista de números enteros
numeros = [1, 2, 3, 4, 5]

# Lista de cadenas de texto
frutas = ["manzana", "banana", "cereza"]

# Lista heterogénea (contiene diferentes tipos de datos)
mi_lista = [1, "Hola", 3.14, True]

# Las listas son mutables, lo que significa que se pueden modificar después de haber sido creadas. 
# Se pueden agregar, eliminar o cambiar elementos dentro de una lista.


# Definiendo una lista de números
numeros = [10, 20, 30, 40, 50]

# Definiendo una lista de cadenas de texto
nombres = ["Alice", "Bob", "Charlie"]

# Definiendo una lista heterogénea
datos = [25, "Python", 3.14, False]

# Los elementos de una lista se pueden acceder utilizando su índice. El índice comienza en 0 para el primer elemento.

# Accediendo a elementos de la lista
primer_numero = numeros[0]  # 10
segundo_nombre = nombres[1]  # "Bob"

# Accediendo a elementos de una lista heterogénea
primer_dato = datos[0]  # 25
segundo_dato = datos[1]  # "Python"

# Python permite extraer subconjuntos de una lista utilizando la técnica de slicing. 
# Esto se hace utilizando el operador : dentro de los corchetes.


# Definiendo una lista de números
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Slicing: obteniendo los primeros cinco elementos
primeros_cinco = numeros[0:5]  # [0, 1, 2, 3, 4]

# Slicing: obteniendo elementos desde el índice 5 hasta el final
desde_cinco = numeros[5:]  # [5, 6, 7, 8, 9]

# Slicing: obteniendo un subconjunto de elementos
sub_lista = numeros[2:7]  # [2, 3, 4, 5, 6]

# Slicing con el tercer parámetro (paso):
# Obteniendo elementos desde el índice 0 hasta el 9 con un paso de 2
pares = numeros[0:10:2]  # [0, 2, 4, 6, 8]


# Algunas operaciones básicas que se pueden realizar con listas incluyen agregar, eliminar y modificar elementos

# Lista inicial
mi_lista = [1, 2, 3]

# Agregar un elemento al final de la lista
mi_lista.append(4)  # [1, 2, 3, 4]

# Insertar un elemento en una posición específica
mi_lista.insert(1, 1.5)  # [1, 1.5, 2, 3, 4]

# Eliminar un elemento específico
mi_lista.remove(1.5)  # [1, 2, 3, 4]

# Modificar un elemento existente
mi_lista[0] = 5  # [5, 2, 3, 4]



# La función len() se puede utilizar para obtener el número de elementos en una lista.
print(len(numeros))  # 5

# La función count() se puede utilizar para contar el número de veces que un elemento específico aparece en una lista.
print(numeros.count(1))  # 1

# La función index() se puede utilizar para obtener el índice de la primera aparición de un elemento específico en una lista.
print(numeros.index(3))  # 2

# La función append() se puede utilizar para agregar un elemento al final de una lista.
numeros.append(6)  # Agrega un elemento al final de la lista

# La función insert() se puede utilizar para insertar un elemento en una posición específica de una lista.
numeros.extend([7, 8, 9])  # Agrega varios elementos al final de la lista

# La función del se puede utilizar para eliminar un elemento de una lista utilizando su índice.
del numeros[0]  # Elimina el primer elemento de la lista

# La función pop() se puede utilizar para eliminar y devolver un elemento de una lista.
numeros.pop(0)  # Elimina y devuelve el primer elemento de la lista

# La función clear se puede utilizar para eliminar todos los elementos de una lista.
numeros.clear()  # Elimina todos los elementos de la lista