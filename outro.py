import os
import sys

##########################   VARIAVEIS GLOBAIS   #################################
arestas = 0
vertices = 0
partida = 0
list_adj = []
caminhos = []
visitados = []
##########################   FUNCOES    ############################################
# 	--------------------- Ler arquivo  -----------------------------------------   #
# ler arquivo e cria estrutura do grafos com array list e dicionarios
def read():
	file = open(os.path.dirname(os.path.realpath(__file__)) + "/grafo.txt")
	
	global arestas, vertices, list_adj, visitados

	vertices = int(file.readline())
	arestas  = int(file.readline())

	visitados = [0]*vertices
	list_adj = [[]]*vertices

	for line in file.readlines():
		origem, destino, peso = line.split(" ")
		list_adj[int(origem)] = list_adj[int(origem)] + [{"destino":int(destino),"peso":int(peso)}]
		list_adj[int(destino)] = list_adj[int(destino)] + [{"destino":int(origem),"peso":int(peso)}]


#	--------------------- Exibir Grafo --------------------------------------------- #
# exibe o grafo de maneira oraganizada                                             #
def printOrganizado():
	for i in xrange(0,vertices):
		print "Vertice: " + str(i)
		for j in xrange(0,len(list_adj[i])):
			print "\tArestas:  " + str(list_adj[i][j])
#	--------------------- Todos caminhos  ---------------------------------------- #
# percorre o grafo definindo todos os caminhos sem repetir vertices e voltando a partida#
def do(atual):
	global visitados,caminhos
	for x in xrange(0,len(list_adj[atual])):
		if 0 not in visitados and ligadoPartida(atual):
			break
		visitados[atual]=1
		if visitados[list_adj[atual][x]["destino"]] == 0:
			print "Indo para: " + str(list_adj[atual][x]["destino"])
			do(list_adj[atual][x]["destino"])
			print "Voltando para: " + str(atual)
			visitados[list_adj[atual][x]["destino"]] = 0

#	--------------------- verifica se pode finalizar  --------------------------------- #
#   ver se o atual esta ligado ao partida e se todos os vertices ja foram visitados     #
def ligadoPartida(atual):
	global partida
	for x in xrange(0,len(list_adj[atual])):
		if list_adj[atual][x]["destino"] == partida:
			return True
	return False

######################       MAIN ()         ######################################
if __name__ == '__main__':
	if len(sys.argv) != 2:
		print "\nFALTA INFORMAR PONTO DE PARTIDA\n"
		sys.exit()
	else:
		partida = int(sys.argv[1])
		read()
		if int(partida)>vertices-1:
			print "\nO VERTICE INDIDADO NAO EXISTE\n"
			sys.exit()
		else:
			print "\nARQUIVO DE ENTRADA LIDO\n"
			print "Numero de Vertices:  " + str(vertices)
			print "Numero de Arestas :  " + str(arestas)
			printOrganizado()
			print "\nBuscando Caminhos"
			do(partida)

			print "MELHOR CAMINHO:  " + str(caminhos)

################################################################################