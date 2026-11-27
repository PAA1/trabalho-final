import sys
from collections import deque

def main():
    dados = [
            list(map(str, linha.split()))
            for linha in sys.stdin
        ]

    simbolos_lista = []

    for lista in dados:
        if len(lista) == 2:
            simbolos_lista.append(lista[0])
            simbolos_lista.append(lista[1])

    simbolos_lista = set(simbolos_lista)
    grafo = {i: [] for i in simbolos_lista}

    for lista in dados:
        if len(lista) == 2:
            grafo[lista[0]].append(lista[1])
            grafo[lista[1]].append(lista[0])

    caminho_entrada_queijo = bfs_caminho(grafo, 'Entrada', '*')
    caminho_queijo_saida = bfs_caminho(grafo, '*', 'Saida')

    print(len(caminho_entrada_queijo) - 1 + len(caminho_queijo_saida) - 1)


def bfs_caminho(grafo, inicio, objetivo):
    # Guarda o nó anterior (pai) de cada nó visitado. O início não tem pai.
    pais = {inicio: None}
    fila = deque([inicio])
    
    while fila:
        no_atual = fila.popleft()
        
        # Se chegamos ao objetivo, reconstruímos o caminho
        if no_atual == objetivo:
            caminho = []
            while no_atual is not None:
                caminho.append(no_atual)
                no_atual = pais[no_atual]
    
            return caminho[::-1]
        
        # Explora os vizinhos
        for vizinho in grafo[no_atual]:
            # Se o vizinho ainda não está em 'pais', ele não foi visitado
            if vizinho not in pais:
                pais[vizinho] = no_atual  # Registra de onde viemos
                fila.append(vizinho)
                
    return None  

main()