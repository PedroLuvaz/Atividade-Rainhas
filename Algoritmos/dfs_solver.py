from Utils.util import pode_colocar


def dfs(n, linha, rainhas, bloqueios):
    if linha == n:
        return rainhas
    for coluna in range(n):
        if pode_colocar(rainhas, linha, coluna, bloqueios):
            resultado = dfs(n, linha + 1, rainhas + [(linha, coluna)], bloqueios)
            if resultado:
                return resultado
    return None

def resolver_dfs(n, bloqueios):
    return dfs(n, 0, [], bloqueios)
