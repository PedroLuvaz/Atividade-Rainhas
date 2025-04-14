from collections import deque
import time
from Utils.util import pode_colocar

def resolver_bfs(n, bloqueios):
    fila = deque()
    fila.append((0, []))  # (linha_atual, rainhas)

    # Inicializar contador de nós e medir tempo
    num_nos = 0
    inicio = time.time()

    while fila:
        linha, rainhas = fila.popleft()
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
                fila.append((linha + 1, rainhas + [(linha, coluna)]))
    
    fim = time.time()
    tempo_total = fim - inicio
    return {
        "solucao": None,
        "num_nos": num_nos,
        "tempo": tempo_total
    }