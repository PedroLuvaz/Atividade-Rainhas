import heapq
import time
from Utils.util import pode_colocar

def heuristica(rainhas, linha, n, bloqueios):
    count = 0
    for l in range(linha, n):
        if not any(pode_colocar(rainhas, l, c, bloqueios) for c in range(n)):
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