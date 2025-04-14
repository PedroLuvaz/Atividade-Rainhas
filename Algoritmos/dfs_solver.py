import time
from Utils.util import pode_colocar

def dfs(n, linha, rainhas, bloqueios, num_nos):
    num_nos[0] += 1  # Incrementar o contador de nós
    if linha == n:
        return rainhas
    for coluna in range(n):
        if pode_colocar(rainhas, linha, coluna, bloqueios):
            resultado = dfs(n, linha + 1, rainhas + [(linha, coluna)], bloqueios, num_nos)
            if resultado:
                return resultado
    return None

def resolver_dfs(n, bloqueios):
    num_nos = [0]  # Usar uma lista para permitir a modificação dentro da função
    inicio = time.time()
    solucao = dfs(n, 0, [], bloqueios, num_nos)
    fim = time.time()
    tempo_total = fim - inicio
    return {
        "solucao": solucao,
        "num_nos": num_nos[0],
        "tempo": tempo_total
    }