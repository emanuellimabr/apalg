#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os
import sys

##########################   VARIAVEIS GLOBAIS   #################################
debug = False
arestas = 0
vertices = 0
partida = 0
list_adj = []
caminhos = []
visitados = []
##########################   FUNCOES    ############################################
# 	--------------------- Ler arquivo  -----------------------------------------   #
# ler arquivo e cria estrutura do grafos com array list e dicionarios
def read(arquivo):
	file = open(arquivo, 'r')
	
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
def todosCaminhos(atual,caminho,peso):
	global visitados, caminhos
	caminho = caminho + str(atual) + ">"
	for x in xrange(0,len(list_adj[atual])):
		pesoFinal,logica = ligadoPartida(atual)
		if 0 not in visitados and logica:
			caminhos.append(caminho + ":" + str(peso+pesoFinal))
			break
		visitados[atual]=1
		if visitados[list_adj[atual][x]["destino"]] == 0:
			# print "Indo para: " + str(list_adj[atual][x]["destino"])
			todosCaminhos(list_adj[atual][x]["destino"],caminho,list_adj[atual][x]["peso"]+peso)
			# print "Voltando para: " + str(atual)
			visitados[list_adj[atual][x]["destino"]] = 0

#	--------------------- verifica se pode finalizar  --------------------------------- #
#   ver se o atual esta ligado ao partida e se todos os vertices ja foram visitados     #
def ligadoPartida(atual):
	global partida
	for x in xrange(0,len(list_adj[atual])):
		if list_adj[atual][x]["destino"] == partida:
			return list_adj[atual][x]["peso"],True
	return 0,False
#	--------------------- Menor caminho  --------------------------------- #
#   define menor caminho dentro dos caminhos que chegam ate a partida      #
def menorCaminho():
	global caminhos
	xpath, menorPeso = caminhos[0].split(":")
	menorCaminho = ""
	for x in xrange(0,len(caminhos)):	
		caminho,peso = caminhos[x].split(":")		
		if int(peso) <= int(menorPeso):			
			menorPeso = peso
			menorCaminho = caminho			
	return str(menorCaminho) + '\tCusto total:' + str(menorPeso)

######################       MAIN ()         ######################################
if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "\nFALTA INFORMAR PONTO DE PARTIDA\n"
		sys.exit()
	else:
		partida = int(sys.argv[1])
		read(raw_input('Nome do Arquivo(com extensao): '))
		if int(partida)>vertices-1:
			print "\nO VERTICE INDIDADO NAO EXISTE\n"
			sys.exit()

		else:
			if len(sys.argv) == 3:
				debug = bool(sys.argv[2])
			if debug:
				print "\n>>DEBUG ON<<"
				print "\nARQUIVO DE ENTRADA LIDO\n"
				print "Numero de Vertices:  " + str(vertices)
				print "Numero de Arestas :  " + str(arestas)
				printOrganizado()
			if debug:
				print "\nBUSCANDO CAMINHOS\n"
			todosCaminhos(partida,"0",0)
			if debug:
				if not caminhos:
					print "Nao foram encontrados caminhos!!"
				else:
					print "Caminhos:  " + str(caminhos) + "\n"
					print "Menor caminho encontrado: " + menorCaminho()
			

################################################################################