#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os
import copy

## Abre o arquivo para leitura
file = open(os.path.dirname(os.path.realpath(__file__)) + "\grafo2.txt")

vertices = int(file.readline())
arestas  = int(file.readline())

## Dicionário cujas chaves são os nós do grafo. 
## Para cada chave, o valor correspondente é uma lista que 
## contém os nós que estão ligados por um aresta direta a partir deste nó
grafo = {}  

# Ler cada linha do arquivo e preenche o dicionário
for line in file.readlines():
    aux = {}    # Dicionário auxiliar
    origem, destino, peso = line.split(" ")     # 
    aux[int(destino)] = int(str(peso.split()).replace('[','').replace(']','').replace('\'',''))

    # Verifica se já existe uma entrada para o nó de origem 
    # Se existir, adiciona o destino a entrada origem
    # Se não, cria uma nova entrada no dicionario
    if grafo.has_key(int(origem)): 
        grafo[int(origem)][int(destino)] = aux[int(destino)]
    else:
        grafo[int(origem)] = aux

## Fecha o arquivo
file.close()

print
print "Representacao do Grafo: "

for key, value in grafo.iteritems():
    print key, value
#print grafo
#print'\n'

## Encontra todos os caminhos a partir de uma origem até o destino
def encontra_caminhos(grafo, origem, destino, caminho=[]):
        
    caminho = caminho + [origem]
    if origem == destino:
        return [caminho]
    if not grafo.has_key(origem):
        return []
    caminhos = []
    for vertice in grafo[origem]:
        if vertice not in caminho:
            novoscaminhos = encontra_caminhos(grafo, vertice, destino, caminho)
            for novocaminho in novoscaminhos:
                caminhos.append(novocaminho)
    return caminhos

# Encontra um ciclo, ou seja, origem e destino são os mesmos
def encontra_ciclo(grafo):
    ciclos = []
    origem = 0
    for startnode in grafo:
        for endnode in grafo:
            novoscaminhos = encontra_caminhos(grafo, startnode, endnode)
            for caminho in novoscaminhos:
                if (len(caminho)==len(grafo)):
                    if caminho[0] in grafo[caminho[len(grafo)-1]]:                        
                        caminho.append(caminho[0])
                        if caminho[0] == origem:                           
                            ciclos.append(caminho)
    return ciclos

def min_caminho(grafo, origem, destino):
    caminhos = encontra_ciclo(grafo)
    #print caminhos
    mt=10**99
    mcaminho=[]
    #print 'Todos os caminhos {} para {}: {}'.format(origem,destino,caminhos)
    print "Avaliando todos os caminhos encontrados para o ciclo:"
    for caminho in caminhos:
        t=sum(grafo[i][j] for i,j in zip(caminho,caminho[1::]))
        print 'Avaliando custo do caminho: {}, custo: {}'.format(caminho, t)
        if t<mt: 
            mt=t
            mcaminho=caminho

    menor_cam=' '.join('{}->{}:{}'.format(i,j,grafo[i][j]) for i,j in zip(mcaminho,mcaminho[1::]))
    menor_som=str(sum(grafo[i][j] for i,j in zip(mcaminho,mcaminho[1::])))
    print
    print 'Menor caminho: \n'+menor_cam+'   Total: '+menor_som

print
print("Buscando Ciclos...")
a = encontra_ciclo(grafo)
if (a ==[]):
    print "Nao foi encontrado nenhum caminho"
else:
    print "Numero de Ciclos Encontrados = ", len(a)
    for any in a:
       for d in any:
           print d, "->",
       print
print
min_caminho(grafo,0,0)
