import sys
import heapq
from time import sleep

def main():
    ponteiro = 0
    final = False

    dados = [
        list(map(int, linha.split()))
        for linha in sys.stdin
    ]

    while(not final):
        grafo, ponteiro, final = montar_grafo(dados, ponteiro, final)

        soma_das_arestas = somar_arestas(grafo)
        custo_reduzido = algoritmo_prim(grafo)

        print(int(soma_das_arestas - custo_reduzido))


def montar_grafo(dados: list, ponteiro: int, final: bool):
    numero_nodos = dados[ponteiro][0]
    grafo = {i: [] for i in range(numero_nodos)}

    achou = False
    ponteiro += 1

    while not achou:
        aresta = dados[ponteiro]

        grafo[aresta[0]].append((aresta[1], aresta[2]))
        grafo[aresta[1]].append((aresta[0], aresta[2]))

        ponteiro += 1

        aresta = dados[ponteiro]
        if(len(aresta) == 2):
            achou = True
            if(aresta[0] == 0 and aresta[1] == 0):
                final = True

    return grafo, ponteiro, final

def somar_arestas(grafo):
    soma = 0
    for arestas in grafo.values():
        for aresta in arestas:
            soma += aresta[1]

    return soma / 2

def algoritmo_prim(grafo):
    visited = {v : False for v in grafo.keys()}
    min_heap = [(0, 0, None)]
    custo = 0
    num_edges = 0
    while min_heap:
        weight, current_node, parent = heapq.heappop(min_heap)

        if visited[current_node]:
            continue
        
        visited[current_node] = True

        if parent is not None:
            custo += weight
            num_edges += 1

            if num_edges == len(grafo.keys()) - 1:  # Se já temos |V| - 1 arestas, a árvore geradora mínima está completa
                break
        
        for neighbor, edge_weight in grafo[current_node]:
            if not visited[neighbor]:
                heapq.heappush(min_heap, (edge_weight, neighbor, current_node))
    return custo

main()