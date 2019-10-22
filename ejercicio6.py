"""
	Ejercicio 6:
	Manejo de colecciones y tuplas
	# Encontrar la siguiente estructura
	#

	[(4.333333333333333, 13, 'Ángel'), (4.666666666666667, 14, 'Ana')]

	Dadas las siguientes estructuras

	paraleloA = [(19, 10, 20), (1, 2, 10), (20, 10, 9), (1, 4, 9)]
	nombres = ["Luis", "Ángel", "José", "Ana"]
	Roberto N
"""
#  Datos del problema
paraleloA = [(19, 10, 20), (1, 2, 10), (20, 10, 9), (1, 4, 9)]
nombres = ["Luis", "Ángel", "José", "Ana"]
#  funciones anonimas para obtener suma y promedio
promedios = list(map(lambda x: sum(x)/len(x), paraleloA))
suma = list(map(lambda x: sum(x),paraleloA))
#  descriminacion de datos y salida de datos
result = (list(zip(promedios, suma, nombres)))
resultFinal = list(filter(lambda x: x[0]<=5, result))
print(resultFinal)