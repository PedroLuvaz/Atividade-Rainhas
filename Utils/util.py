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
    """
    Imprime o tabuleiro com as rainhas e bloqueios.
    """
    tabuleiro = [["." for _ in range(n)] for _ in range(n)]

    # Adicionar bloqueios
    for i, j in bloqueios:
        tabuleiro[i][j] = "X"

    # Adicionar rainhas
    if isinstance(solucao[0], int):  # Caso do algoritmo genético
        for i, j in enumerate(solucao):
            tabuleiro[i][j] = "Q"
    else:  # Caso dos outros algoritmos
        for i, j in solucao:
            tabuleiro[i][j] = "Q"

    # Imprimir o tabuleiro
    for linha in tabuleiro:
        print(" ".join(linha))
