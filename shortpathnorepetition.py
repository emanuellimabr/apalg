import os
import copy
import numpy

file = open(os.path.dirname(os.path.realpath(__file__)) + "\grafo.txt")

vertices = int(file.readline())
arestas  = int(file.readline())

print(vertices)
print(arestas)

adj_list = numpy.zeros([vertices, vertices])
visitados = numpy.zeros([vertices])

for line in file.readlines():
    origem, destino, peso = line.split(" ")

    adj_list[int(origem)][int(destino)] = int(peso)

print(adj_list)

o = 0 

while 0 in visitados:
	for d in xrange(0,vertices):
		if (adj_list[o][d] != 0):
			if visitados[d] == 0:				
				o = d
				print("O Atual : " + str(o))
				visitados[o] = 1				
				break	
			
print("cabou porraa")
if o != 0 :
	print("Nao voulto nego")
else:
	print("voltou nego")
print(visitados)
	