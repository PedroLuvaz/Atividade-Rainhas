import random

def gerar_bloqueios(n, semente=42):
    random.seed(semente)
    total = n * n
    minimo = int(0.07 * total)
    maximo = int(0.13 * total)
    qtd_bloqueios = random.randint(minimo, maximo)
    bloqueios = set()
    while len(bloqueios) < qtd_bloqueios:
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        bloqueios.add((i, j))
    return bloqueios

def pode_colocar(rainhas, linha, coluna, bloqueios):
    if (linha, coluna) in bloqueios:
        return False
    for r, c in rainhas:
        if c == coluna or abs(r - linha) == abs(c - coluna):
            return False
    return True

def imprimir_tabuleiro(n, solucao, bloqueios):
    tabuleiro = [["." for _ in range(n)] for _ in range(n)]
    for i, j in bloqueios:
        tabuleiro[i][j] = "X"
    for i, j in solucao:
        tabuleiro[i][j] = "Q"
    for linha in tabuleiro:
        print(" ".join(linha))
