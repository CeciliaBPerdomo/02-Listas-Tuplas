# Los conjuntos y diccionarios son otro tipo de colecciones que, permiten almacenar múltiples elementos en una sola variable. 
# Aunque ambos se utilizan para agrupar datos, tienen características y usos distintos que los diferencian de otros tipos de colecciones.

# 1. Son colecciones no ordenadas de elementos únicos. No permiten duplicados y no mantienen el orden de los elementos.
# 2. Son mutables, es decir, se pueden agregar o eliminar elementos después de su creación.
# 3. No permiten el acceso a elementos mediante índices ya que no mantienen un orden.
# 4. Se definen utilizando llaves {} y los elementos se separan por comas  o la función set().
# 5. Los conjuntos no permiten elementos duplicados. Si se intenta agregar un duplicado, será ignorado.
# 6. Se utilizan para almacenar elementos únicos y realizar operaciones matemáticas como unión, intersección y diferencia.
    # a. Unión: Combina todos los elementos de dos conjuntos, eliminando duplicados.
    #    python conjunto1 = {1, 2, 3} conjunto2 = {3, 4, 5} union = conjunto1 | conjunto2 # Resultado: {1, 2, 3, 4, 5}

    # b. Intersección: Devuelve los elementos que están presentes en ambos conjuntos.
    #    python interseccion = conjunto1 & conjunto2 # Resultado: {3}

    # c. Diferencia: Devuelve los elementos que están en el primer conjunto pero no en el segundo.
    #    python diferencia = conjunto1 - conjunto2 # Resultado: {1, 2}
# 7. Además de las operaciones básicas, los conjuntos en Python tienen varios métodos útiles:
    # a. add(): Agrega un elemento al conjunto.
    #    python numeros.add(6) # numeros ahora es {1, 2, 3, 4, 5, 6}

    # b. remove(): Elimina un elemento del conjunto. Genera un error si el elemento no existe.
    #    python numeros.remove(6) # numeros ahora es {1, 2, 3, 4, 5}

    # c. discard(): Elimina un elemento del conjunto si está presente. No genera error si el elemento no existe.
    #    python numeros.discard(6) # No genera error

    # d. clear(): Elimina todos los elementos del conjunto.
    #    python numeros.clear() # numeros ahora es un conjunto vacío


# Definiendo un conjunto de números
numeros = {1, 2, 3, 4, 5}

# Usando la función set()
letras = set(['a', 'b', 'c', 'd'])

# Conjunto vacío
conjunto_vacio = set()

mi_conjunto = {"hola", 1, 2, 3, 4, 4, 4, "adios"}
print(mi_conjunto)  # {'hola', 1, 2, 3, 4, 'adios'}

# Convertir un conjunto en una lista.
mi_lista = list(mi_conjunto)
mi_conjunto.add("nuevo")

# Para modificar se convierte a lista, se modifica y luego se convierte a conjunto.

# Remove y discard eliminan un elemento del conjunto.
mi_conjunto.remove("hola")
mi_conjunto.discard("adios")