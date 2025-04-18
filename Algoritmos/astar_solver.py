import heapq
import time
from Utils.util import pode_colocar

def heuristica(rainhas, linha, n, bloqueios):
    """
    Heurística melhorada para o problema das N-Rainhas.
    Calcula o número de linhas restantes que ainda podem ser atacadas pelas rainhas já colocadas.
    """
    ataques = set()
    for l, c in rainhas:
        # Adicionar ataques horizontais, diagonais principais e secundárias
        for i in range(linha, n):
            ataques.add((i, c))  # mesma coluna
            ataques.add((i, c + (i - l)))  # diagonal principal
            ataques.add((i, c - (i - l)))  # diagonal secundária

    # Contar as linhas restantes que não podem receber rainhas
    count = 0
    for l in range(linha, n):
        if all((l, c) in ataques or (l, c) in bloqueios for c in range(n)):
            count += 1
    return count

def resolver_astar(n, bloqueios):
    heap = []
    estado_inicial = []
    g = 0
    h = heuristica(estado_inicial, 0, n, bloqueios)
    heapq.heappush(heap, (g + h, g, estado_inicial))

    # Inicializar contador de nós e medir tempo
    num_nos = 0
    inicio = time.time()

    while heap:
        f, g, estado = heapq.heappop(heap)
        num_nos += 1  # Incrementar o contador de nós
        linha = len(estado)
        if linha == n:
            fim = time.time()
            tempo_total = fim - inicio
            return {
                "solucao": estado,
                "num_nos": num_nos,
                "tempo": tempo_total
            }
        for coluna in range(n):
            if pode_colocar(estado, linha, coluna, bloqueios):
                novo_estado = estado + [(linha, coluna)]
                novo_g = g + 1
                novo_h = heuristica(novo_estado, linha + 1, n, bloqueios)
                heapq.heappush(heap, (novo_g + novo_h, novo_g, novo_estado))
    fim = time.time()
    tempo_total = fim - inicio
    return {
        "solucao": None,
        "num_nos": num_nos,
        "tempo": tempo_total
    }