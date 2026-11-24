import sys

def main():
    cont = 1
    dados = [
            list(map(str, linha.split()))
            for linha in sys.stdin
        ]

    ponteiro = 0

    for i in range(int(dados[0][0])):
        print("CENARIO {" + str(cont) + "}")
        cont += 1

        ponteiro += 1
        renas = {}

        total_renas = int(dados[ponteiro][0])
        renas_usadas = int(dados[ponteiro][1])

        

        for i in range(total_renas):
            ponteiro += 1
            rena = dados[ponteiro]
            renas[rena[0]] = [int(rena[1]), int(rena[2]), float(rena[3])]


        for i, rena in enumerate(ordenar_renas(renas).keys()):
            if i >= renas_usadas:
                break
            print(f"{i + 1} - {rena}")


def criterio_ordenacao(rena):
    nome = rena[0]
    dados = rena[1]
    
    peso = dados[0]
    idade = dados[1]
    altura = dados[2]

    return (-peso, idade, altura, nome.lower())

def ordenar_renas(renas: dict):
    renas_ordenadas = dict(sorted(renas.items(), key = criterio_ordenacao))
    
    return renas_ordenadas



main()