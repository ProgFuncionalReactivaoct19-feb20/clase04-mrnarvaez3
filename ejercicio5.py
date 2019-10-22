"""
Ejercicio 5:
	Manejo de colecciones y tuplas
	# Encontrar la siguiente estructura

	[(16.333333333333332, 'Ángel'), (16.666666666666668, 'José'), (13.0, 'Ana')]
	(16.666666666666668, 'José')
	[(13.0, 'Ana'), (16.666666666666668, 'José'), (16.333333333333332, 'Ángel')]

	Dadas las siguientes estructuras
	paraleloA = [(19, 10, 20), (20, 20, 10), (20, 10, 9)]
	nombres = ["Ángel", "José", "Ana"]
	Roberto N
"""
#  Datos del problema
paraleloA = [(19, 10, 20), (20, 20, 10), (20, 10, 9)]
nombres = ["Ángel", "José", "Ana"]

#  Funcion para obtener promedio
promedios = list(map(lambda x: (x[0]+x[1]+x[2])/3, paraleloA))

#  Salida de datos
print(list(zip(promedios, nombres)))
print(max(zip(promedios, nombres)))
print(list(zip(promedios, sorted(nombres))))
