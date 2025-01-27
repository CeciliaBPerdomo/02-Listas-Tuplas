# Los diccionarios en Python son estructuras de datos que permiten almacenar colecciones de pares clave-valor. 
# A diferencia de las listas y tuplas, que son secuencias de elementos, los diccionarios son colecciones no ordenadas, 
# lo que significa que no mantienen el orden de inserción de los elementos. 
# Cada clave en un diccionario es única y se utiliza para acceder a su valor correspondiente de manera rápida y eficiente.


# Para definir un diccionario en Python, se utilizan llaves {} y los pares clave-valor se separan por comas, con la clave y el valor separados por dos puntos :. 
# A continuación, se presentan algunos ejemplos de cómo definir y utilizar diccionarios:


# Definiendo un diccionario con claves y valores
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Otro ejemplo de diccionario
inventario = {
    "manzanas": 10,
    "naranjas": 5,
    "peras": 7
}


# Definiendo un diccionario
alumno = {
    "nombre": "Ana",
    "edad": 22,
    "curso": "Matemáticas"
}

# Accediendo a valores utilizando claves
nombre_alumno = alumno["nombre"]  # "Ana"
edad_alumno = alumno["edad"]  # 22


# Modificando un valor existente
alumno["edad"] = 23  # La edad ahora es 23

# Agregando un nuevo par clave-valor
alumno["ciudad"] = "Barcelona"  # Se añade la clave "ciudad" con el valor "Barcelona"
print(alumno)  # {'nombre': 'Ana', 'edad': 23, 'curso': 'Matemáticas', 'ciudad': 'Barcelona'}

# Eliminando un par clave-valor
del alumno["curso"]  # Se elimina la clave "curso" y su valor


#keys(): Devuelve una vista de las claves del diccionario.
python_claves = alumno.keys() # dict_keys(['nombre', 'edad', 'ciudad'])

#values(): Devuelve una vista de los valores del diccionario.
python_valores = alumno.values() # dict_values(['Ana', 23, 'Barcelona'])

#items(): Devuelve una vista de los pares clave-valor del diccionario.
python_items = alumno.items() # dict_items([('nombre', 'Ana'), ('edad', 23), ('ciudad', 'Barcelona')])

#get(): Devuelve el valor para una clave dada, o None si la clave no existe.
python_curso = alumno.get("curso") # None, ya que la clave "curso" fue eliminada

#update(): Actualiza el diccionario con los pares clave-valor de otro diccionario o con pares clave-valor proporcionados como argumentos.
python_alumno = alumno.update({"edad": 24, "curso": "Física"}) # Actualiza la edad y añade el curso