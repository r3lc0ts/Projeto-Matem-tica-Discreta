import time
import sys

ESTADO_RESOLVIDO = ((0, 1, 2, 3, 4, 5, 6), (0, 0, 0, 0, 0, 0, 0))
MOVE = {
    "U": {"perm": (3, 0, 1, 2, 4, 5, 6), "ori": (0, 0, 0, 0, 0, 0, 0)},
    "F": {"perm": (0, 1, 3, 4, 5, 2, 6), "ori": (0, 0, 1, 2, 1, 2, 0)},
    "R": {"perm": (0, 2, 5, 3, 4, 6, 1), "ori": (0, 1, 2, 0, 0, 1, 2)},
    "U'": {"perm": (1, 2, 3, 0, 4, 5, 6), "ori": (0, 0, 0, 0, 0, 0, 0)},
    "F'": {"perm": (0, 1, 5, 2, 3, 4, 6), "ori": (0, 0, 1, 2, 1, 2, 0)},
    "R'": {"perm": (0, 6, 1, 3, 4, 2, 5), "ori": (0, 1, 2, 0, 0, 1, 2)},
    "U2": {"perm": (2, 3, 0, 1, 4, 5, 6), "ori": (0, 0, 0, 0, 0, 0, 0)},
    "F2": {"perm": (0, 1, 4, 5, 2, 3, 6), "ori": (0, 0, 0, 0, 0, 0, 0)},
    "R2": {"perm": (0, 5, 6, 3, 4, 1, 2), "ori": (0, 0, 0, 0, 0, 0, 0)},
}


def movimento(estado: tuple, perm: tuple, ori: tuple):
    p_atual, o_atual = estado[0], estado[1]
    novo_p, novo_o = [0]*len(perm), [0]*len(ori)

    for i in range(7):
        novo_p[i] = p_atual[perm[i]]
        novo_o[i] = (o_atual[perm[i]] + ori[i]) % 3

    return (tuple(novo_p), tuple(novo_o))


def mapeamento():
    visitados = {ESTADO_RESOLVIDO: 0}
    camada_atual = [ESTADO_RESOLVIDO]
    distancia = 0 
    total_estados = 0

    print("Iniciando a prova do Número de Deus...")
    print("-" * 50)

    inicio = time.time()

    # O loop roda enquanto houver estados novos a explorar na camada
    while camada_atual:
        qtd_estados_camada = len(camada_atual)
        total_estados += qtd_estados_camada
        print(
            f"Distância {distancia:2d}: {qtd_estados_camada:9,d} estados | Total acumulado: {total_estados:9,d}")

        proxima_camada = []

        # Percorre todos os estados da camada atual
        for atual in camada_atual:
            # Testa os 9 movimentos
            for dados_mov in MOVE.values():
                vizinho = movimento(atual, dados_mov["perm"], dados_mov["ori"])

                if vizinho not in visitados:
                    visitados[vizinho] = distancia + 1
                    proxima_camada.append(vizinho)

        camada_atual = proxima_camada
        if camada_atual:
            distancia += 1

    fim = time.time()
    tempo_total = fim - inicio

    print("-" * 50)
    print(f"Tempo total de execução: {tempo_total:.2f} segundos")
    print(f"Total de estados alcançados: {total_estados:,}")
    print(f"Número de Deus HTM: {distancia}")

    return visitados

if __name__ == "__main__":
    tabela_distancias = mapeamento()