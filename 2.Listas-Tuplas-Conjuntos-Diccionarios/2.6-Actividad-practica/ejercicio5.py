# Crear un conjunto en Python que posea los siguientes elementos:
# Países: Inglaterra, USA, México.
paises = {"Inglaterra", "USA", "México"}
print(paises)

# Posteriormente agrega nuestro set de países, los elementos de: Islandia, Italia, Argentina y Portugal, USA
paises.add("Islandia")
paises.add("Italia")
paises.add("Argentina")
paises.add("Portugal")
paises.add("USA")
print(paises)

#Elimina a los países: Chile e Italia
paises.discard("Chile") # No genera error
paises.remove("Italia")
print(paises)

# Pregunta: ¿Qué pasa si queremos eliminar al país Chile utilizando el método remove?, ¿Qué pasó con el element de USA?
# Respuesta: Se genera un error, ya que el elemento "Chile" no existe en el conjunto. 
# El elemento "USA" sigue existiendo en el conjunto, se muestra una sola vez.