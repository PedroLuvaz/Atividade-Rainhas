import heapq
import time
from Utils.util import pode_colocar

def resolver_ucs(n, bloqueios):
    heap = []
    heapq.heappush(heap, (0, 0, []))  # (custo, linha, rainhas)

    # Inicializar contador de nós e medir tempo
    num_nos = 0
    inicio = time.time()

    while heap:
        custo, linha, rainhas = heapq.heappop(heap)
        num_nos += 1  # Incrementar o contador de nós
        if linha == n:
            fim = time.time()
            tempo_total = fim - inicio
            return {
                "solucao": rainhas,
                "num_nos": num_nos,
                "tempo": tempo_total
            }
        for coluna in range(n):
            if pode_colocar(rainhas, linha, coluna, bloqueios):
                novo_estado = rainhas + [(linha, coluna)]
                heapq.heappush(heap, (custo + 1, linha + 1, novo_estado))
    
    fim = time.time()
    tempo_total = fim - inicio
    return {
        "solucao": None,
        "num_nos": num_nos,
        "tempo": tempo_total
    }