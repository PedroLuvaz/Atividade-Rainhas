import heapq
from Utils.util import pode_colocar


def resolver_ucs(n, bloqueios):
    heap = []
    heapq.heappush(heap, (0, 0, []))  # (custo, linha, rainhas)

    while heap:
        custo, linha, rainhas = heapq.heappop(heap)
        if linha == n:
            return rainhas
        for coluna in range(n):
            if pode_colocar(rainhas, linha, coluna, bloqueios):
                novo_estado = rainhas + [(linha, coluna)]
                heapq.heappush(heap, (custo + 1, linha + 1, novo_estado))
    return None
