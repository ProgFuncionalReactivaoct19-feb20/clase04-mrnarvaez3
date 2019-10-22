"""
	Ejercicio1
	Roberto N
"""
listaA = [10, 2, 3, 4]

listaB = ["a", "b", "c", "d"]

listaC = sorted(listaB, reverse = True)
listaD = sorted(listaA)



print(list(zip(listaD, listaC)))
print(list(listaA[0], listaC[3]))


