from collections import deque
from Utils.util import pode_colocar


def resolver_bfs(n, bloqueios):
    fila = deque()
    fila.append((0, []))  # (linha_atual, rainhas)

    while fila:
        linha, rainhas = fila.popleft()
        if linha == n:
            return rainhas
        for coluna in range(n):
            if pode_colocar(rainhas, linha, coluna, bloqueios):
                fila.append((linha + 1, rainhas + [(linha, coluna)]))
    return None
