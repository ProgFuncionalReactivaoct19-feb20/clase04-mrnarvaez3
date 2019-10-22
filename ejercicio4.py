"""
	Ejercicio 4:
	Manejo Dadase colecciones y tuplas

	# Encontrar la siguiente estructura
	#		
	[(16.333333333333332, 'Ángel'), (16.666666666666668, 'José'), (13.0, 'Ana')]
	Dadas las siguientes estructuras:		
	paraleloA = [(19, 10, 20), (20, 20, 10), (20, 10, 9)]
	nombres = ["Ángel", "José", "Ana"]
	Roberto N
"""
paraleloA = [(19, 10, 20), (20, 20, 10), (20, 10, 9)]

nombres = ["Ángel", "José", "Ana"]

#  Funcion anonima para obtener promedio
resultado = list(map(lambda x: (x[0]+x[1]+x[2])/3, paraleloA))

print(list(zip(resultado,nombres)))