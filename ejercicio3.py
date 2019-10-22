"""
		Manejo de colecciones y tuplas
		Roberto N
"""

lista = [(100, 2), (20, 4), (30, 1)]
lista2 = ["a", "b", "c"]

#  funcion anonima para pasar a masyuculas
resultado = map(lambda x: x.upper(), lista2)
#  salida de datos e invierto la lista 2 
print(list(zip(sorted(lista), sorted(resultado, reverse = True))))