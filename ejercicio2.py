"""
		Manejo de colecciones y tuplas

		Roberto N
"""

lista = [(100, 2), (20, 4), (30, 1)]
lista2 = ["b", "a", "c"]

#  salida de datos proceso en una sola linea
print(list(zip(sorted(lista2), sorted(lista, key = lambda x:x[1]) )))