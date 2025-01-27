# Las tuplas son estructuras de datos que, al igual que las listas, permiten almacenar una colección ordenada de elementos. 
# Las tuplas son inmutables, lo que significa que una vez creadas, sus elementos no pueden ser modificados. 
# Esta característica hace que las tuplas sean útiles para almacenar datos que no deben cambiar a lo largo del programa.

# Características de las Tuplas
    # 1. Inmutabilidad: Una vez definida, no se pueden cambiar los elementos de una tupla.
    # 2. Definición: Se definen utilizando paréntesis () en lugar de corchetes [].
    # 3. Acceso Rápido: Al ser inmutables, Python puede optimizar el acceso a sus elementos, lo que las hace ligeramente más rápidas que las listas para algunas operaciones.
    # 4. Heterogeneidad: Al igual que las listas, las tuplas pueden contener elementos de diferentes tipos.


# Definiendo una tupla
mi_tupla = (1, 2, 3, 4, 5)


# Tupla de números enteros
numeros = (10, 20, 30, 40, 50)

# Tupla de cadenas de texto
nombres = ("Alice", "Bob", "Charlie")

# Tupla heterogénea (diferentes tipos de datos)
datos = (25, "Python", 3.14, False)


# Accediendo a elementos de la tupla
primer_numero = numeros[0]  # 10
segundo_nombre = nombres[1]  # "Bob"

# Accediendo a elementos de una tupla heterogénea
primer_dato = datos[0]  # 25
segundo_dato = datos[1]  # "Python"


# Definiendo una tupla de números
numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Slicing: obteniendo los primeros cinco elementos
primeros_cinco = numeros[0:5]  # (0, 1, 2, 3, 4)

# Slicing: obteniendo elementos desde el índice 5 hasta el final
desde_cinco = numeros[5:]  # (5, 6, 7, 8, 9)

# Slicing: obteniendo un subconjunto de elementos
sub_tupla = numeros[2:7]  # (2, 3, 4, 5, 6)