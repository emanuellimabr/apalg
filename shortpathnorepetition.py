import os
import sys
import copy

arestas = 0
vertices = 0
visitados = []
list_adj = []
caminho = []

#--------------METODOS----------------------------------------------------------
def read():#Ler o arquivo e cria tabela
	file = open(os.path.dirname(os.path.realpath(__file__)) + "\grafo.txt")
	
	global arestas, vertices, visitados, list_adj, caminho

	vertices = int(file.readline())
	arestas  = int(file.readline())

	for i in xrange(vertices):
		list_adj.append([0] * vertices)

	for line in file.readlines():
		origem, destino, peso = line.split(" ")
		list_adj[int(origem)][int(destino)] = int(peso)

	visitados = [0]*vertices
	caminho = [0]*vertices

def do():
	global o, list_adj, vertices, visitados,caminho,count

	for d in xrange(0,vertices):
		if (list_adj[o][d] != 0 and visitados[d] == 0):
			peso = list_adj[o][d]
			o = d
			print("Atual : " + str(o))
			visitados[o] = peso
			caminho[o] = o
			break
#--------------METODOS FIM-------------------------------------------------------

read()
print "INICIANDO"
print "Vertices:  " + str(vertices)
print "Arestas:   " + str(arestas)
print "Visitados: " + str(visitados)
print "Caminho:   " + str(caminho)
print "List_adj:  " + str(list_adj)
print "\n\n"

o = 0
do()
while 0 in visitados and o!=0 and sum(list_adj[o])!=0:
	do()

print "\n\nFINALIZANDO"
if o != 0 or 0 in visitados:
	print"Nao foi possivel voltar passando por todos os vertices"
else:
	print"Foi possivel voltar passando por todos os vertices"

print "\n\n"
print "Vertices:  " + str(vertices)
print "Arestas:   " + str(arestas)
print "Visitados: " + str(visitados)
print "Caminho:   " + str(caminho)
print "List_adj:  " + str(list_adj)