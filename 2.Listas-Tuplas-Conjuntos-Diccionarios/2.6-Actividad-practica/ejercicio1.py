# a. Identifica el tipo de dato (int, float, string, list o touple) de los siguientes valores literales.

dato1 = type("Hola Mundo")
print("Dato 1: ", dato1)

dato2 = type([1, 10, 100])
print("Dato 2: ", dato2)

dato3 = type(-25)
print("Dato 3: ", dato3)

dato4 = type((8, 100, -12))
print("Dato 4: ", dato4)

dato5 = type(1.167)
print("Dato 5: ", dato5)

dato6 = type(' ')
print("Dato 6: ", dato6)
	
dato7 = type((1, -5, "Hola!"))
print("Dato 7: ", dato7)

# b. Determina mentalmente (sin programar) el resultado que aparecerá por pantalla a partir de las siguientes variables:
a = 10
b = -5
c = "Hola"
d = [1, 2, 3]
e= (4,5,6)

print(a * 5)        # 50
print(a - b)        # 15
print(c + "Mundo")	# HolaMundo
print(c * 2)	    # HolaHola
print(c[-1])	    # a
print(c[1:])	    # ola
print(d + d)        # [1, 2, 3, 1, 2, 3]	
print(e[1])	        # 5
print(e+(7,8,9))    # (4, 5, 6, 7, 8, 9)