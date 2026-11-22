import sys
from collections import deque

def main():
    dados = [
        list(map(int, linha.split()))
        for linha in sys.stdin
    ]

    ponteiro = 0

    while ponteiro < len(dados):
        n = dados[ponteiro][0]
        ponteiro += 1

        if n == 0:
            break

        grafo = {}

        for _ in range(n):
            aluno = dados[ponteiro][0]
            ponteiro += 1

            amigos = dados[ponteiro]
            ponteiro += 1

            grafo.setdefault(aluno, [])

            for amigo in amigos:
                grafo[aluno].append(amigo)
                grafo.setdefault(amigo, [])
                grafo[amigo].append(aluno)

        print("SIM" if bipartido(grafo) else "NAO")


def bipartido(grafo):
    cores = {}

    for inicio in grafo:
        if inicio not in cores:
            cores[inicio] = 0
            fila = deque([inicio])

            while fila:
                atual = fila.popleft()

                for vizinho in grafo[atual]:
                    if vizinho not in cores:
                        cores[vizinho] = 1 - cores[atual]
                        fila.append(vizinho)

                    elif cores[vizinho] == cores[atual]:
                        return False

    return True


main()
