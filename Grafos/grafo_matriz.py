from datetime import time
from queue import Queue
from time import sleep
import numpy as np
import sys
sys.setrecursionlimit(10000)

class Grafo:
    
    def __init__(self, n):
        self.matriz_adjacencia =  np.zeros((n, n), dtype="int")
        self.n_arestas = 0
        self.n = n

    def inserir_aresta(self, u, v, direcionado = False):
        if not direcionado:
            self.matriz_adjacencia[u][v] = 1        
            self.matriz_adjacencia[v][u] = 1        
        else:
            self.matriz_adjacencia[u][v] = 1
        self.n_arestas += 1

    def remover_aresta(self, v, w):
        self.matriz_adjacencia[v][w] = 0
        self.n_arestas -= 1
        self.n_arestas = max(0, self.n_arestas)

    def leitura_grafo(self):
        n, m = self.matriz_adjacencia.shape
        for i in range(n):
            for j in range(m):
                self.matriz_adjacencia[i][j] = 0        

    def sao_adjacentes(self, u, v):
        return self.matriz_adjacencia[u][v] == 1

    def retorna_vizinhos(self, v):
        w = 0
        vizinhos = []
        while w < self.n:
            origem, destino = w, v
            if self.sao_adjacentes(origem, destino):
                vizinhos.append(w)
            w += 1
            if (w > self.n):
                w = 0

        return vizinhos

    def imprimir(self):
        print(self.matriz_adjacencia)
    
    def conta_componentes_grafo(self):
        visitados = np.zeros(self.n, dtype="int")        
        conta_componentes = 0
        for v in range(self.n):
            for w in range(self.n):
                if self.sao_adjacentes(v, w):                                                    
                    if visitados[w] == 0:
                        conta_componentes += 1
                        self.conta_componentes(w, visitados)

        return conta_componentes

    def conta_componentes(self, v, visitados):
        visitados[v] = -1 #Marca o vértice como visitado        
        for w in range(self.n):
            if self.sao_adjacentes(v, w):
                if visitados[w] == 0:                    
                    print("v({})->w({})".format(v, w))
                    self.busca_profundidade(w, visitados)           


    def busca_profundidade_grafo(self, v_inicial):
        visitados = np.zeros(self.n, dtype="int")
        print(visitados)        
        self.busca_profundidade(v_inicial, visitados)
        print(visitados)        

    def verifica_caminho(self, inicio, destino, h = 1):
        mapa = self.matriz_adjacencia
        n = len(mapa)
        m = len(mapa[0])                    
        return self.verifica_caminho_(mapa, inicio, destino, n, m, h)

    def verifica_caminho_(self, mapa, inicio, destino, n, m, h = 1):    
        linha  = inicio[0]
        coluna = inicio[1]        
        
        if (linha == destino[0] and coluna == destino[1]) and mapa[linha][coluna] != 0:
            print("achou")
            mapa[linha][coluna] = h
            return True

        if mapa[linha][coluna] == 1:
            mapa[linha][coluna] = h
            if (self.verifica_caminho( (max(0, linha-1), coluna), destino, h+1)):
                return True
            if (self.verifica_caminho( (linha, min(coluna+1, m-1)), destino, h+1)):
                return True                            
            if (self.verifica_caminho( (min(linha+1, n-1), coluna), destino, h+1)):
                return True            
            if (self.verifica_caminho( (linha, max(0, coluna-1)), destino, h+1)):
                return True                

        return False

    def busca_profundidade(self, v_inicial, visitados):        
        visitados[v_inicial] = -1 #Marca o vértice como visitado
        for i in range(self.n):                        
            v = self.matriz_adjacencia[v_inicial][i]            
            if visitados[i] == 0:
                if v == 1: #Verifica se o vértice é vizinho
                    print("v({})->w({})".format(v_inicial, i))
                    self.busca_profundidade(i, visitados)   

    def bsf(self):
        queue = Queue()          
        queue.put((0, 0))  
        row, col = self.matriz_adjacencia.shape  
        visitado = np.zeros((row), dtype="int")    
        while not queue.empty():
            v, w = queue.get()             
            if (visitado[w] == 0) and self.matriz_adjacencia[v][w] != 0:
                visitado[w] = 1  
                print(v, w)                
                for i in range(row):                                        
                    w += 1
                    if (w > self.n):
                        w = 0
                    queue.put((v, w))   

if __name__ == '__main__':
    #Grafo com 6 vértices
    grafo = Grafo(8)    
    grafo.inserir_aresta(1, 1)
    #grafo.inserir_aresta(1, 2)
    grafo.inserir_aresta(1, 3, direcionado=True)
    grafo.inserir_aresta(1, 4)
    grafo.inserir_aresta(1, 5, direcionado=True)
    grafo.inserir_aresta(1, 6, direcionado=True)
    grafo.inserir_aresta(2, 1)
    grafo.inserir_aresta(2, 2)
    #grafo.inserir_aresta(2, 3)
    grafo.inserir_aresta(2, 4)
    grafo.inserir_aresta(2, 5)
    grafo.inserir_aresta(2, 6)
    grafo.inserir_aresta(3, 1, direcionado=True)
    grafo.inserir_aresta(3, 2, direcionado=True)
    grafo.inserir_aresta(3, 4, direcionado=True)
    grafo.inserir_aresta(3, 6, direcionado=True)
    grafo.inserir_aresta(4, 1)
    grafo.inserir_aresta(4, 2)
    grafo.inserir_aresta(4, 4)
    grafo.inserir_aresta(4, 5)
    grafo.inserir_aresta(4, 6)    
    grafo.inserir_aresta(5, 2)    
    grafo.inserir_aresta(5, 4)
    grafo.inserir_aresta(5, 5)
    grafo.inserir_aresta(5, 6)
    grafo.inserir_aresta(6, 1)
    grafo.inserir_aresta(6, 2)    
    grafo.inserir_aresta(6, 4)
    grafo.inserir_aresta(6, 5)
    grafo.inserir_aresta(6, 6)    

    grafo.imprimir()
    if (grafo.verifica_caminho( (6,2), (6, 6), h = 100)):
        print("Achou")
    else:
        print("Não achou")
        

    grafo.imprimir()