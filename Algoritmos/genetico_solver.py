import random
import time

def fitness(individuo, n):
    """
    Calcula o fitness de um indivíduo.
    O fitness é o número de pares de rainhas que não se atacam.
    """
    ataques = 0
    for i in range(n):
        for j in range(i + 1, n):
            # Verificar ataques na mesma coluna ou diagonais
            if individuo[i] == individuo[j] or abs(individuo[i] - individuo[j]) == abs(i - j):
                ataques += 1
    return -ataques  # Fitness negativo para minimizar ataques

def gerar_populacao(tamanho_populacao, n):
    """
    Gera uma população inicial de indivíduos.
    Cada indivíduo é uma permutação aleatória das colunas.
    """
    return [random.sample(range(n), n) for _ in range(tamanho_populacao)]

def selecionar_pais(populacao, fitnesses):
    """
    Seleciona dois pais usando torneio.
    """
    torneio = random.sample(list(zip(populacao, fitnesses)), k=5)
    torneio.sort(key=lambda x: x[1], reverse=True)
    return torneio[0][0], torneio[1][0]

def cruzamento(pai1, pai2, n):
    """
    Realiza o cruzamento (crossover) entre dois pais.
    Usa o método de cruzamento de ordem (Order Crossover - OX).
    """
    ponto1, ponto2 = sorted(random.sample(range(n), 2))
    filho = [-1] * n
    filho[ponto1:ponto2] = pai1[ponto1:ponto2]

    pos = ponto2
    for gene in pai2:
        if gene not in filho:
            if pos >= n:
                pos = 0
            filho[pos] = gene
            pos += 1
    return filho

def mutacao(individuo, taxa_mutacao, n):
    """
    Realiza a mutação em um indivíduo.
    Troca duas colunas aleatoriamente com base na taxa de mutação.
    """
    if random.random() < taxa_mutacao:
        i, j = random.sample(range(n), 2)
        individuo[i], individuo[j] = individuo[j], individuo[i]
    return individuo

def backtracking_corrigir(individuo, n):
    """
    Usa backtracking para corrigir conflitos em um indivíduo.
    """
    def is_safe(tabuleiro, linha, coluna):
        for i in range(linha):
            if tabuleiro[i] == coluna or \
               abs(tabuleiro[i] - coluna) == abs(i - linha):
                return False
        return True

    def backtrack(tabuleiro, linha):
        if linha == n:
            return tabuleiro
        for coluna in range(n):
            if is_safe(tabuleiro, linha, coluna):
                tabuleiro[linha] = coluna
                resultado = backtrack(tabuleiro, linha + 1)
                if resultado:
                    return resultado
        return None

    # Corrigir o indivíduo usando backtracking
    tabuleiro = [-1] * n
    for i in range(len(individuo)):
        tabuleiro[i] = individuo[i]

    return backtrack(tabuleiro, len(individuo))

def resolver_genetico_com_backtracking(n, tamanho_populacao=1000, geracoes=5000, taxa_mutacao=0.3):
    """
    Resolve o problema das N-Rainhas usando um algoritmo genético com backtracking.
    """
    inicio = time.time()
    populacao = gerar_populacao(tamanho_populacao, n)
    fitnesses = [fitness(individuo, n) for individuo in populacao]
    total_individuos_avaliados = tamanho_populacao  # Contador inicial

    for geracao in range(geracoes):
        nova_populacao = []
        for _ in range(tamanho_populacao // 2):
            pai1, pai2 = selecionar_pais(populacao, fitnesses)
            filho1 = cruzamento(pai1, pai2, n)
            filho2 = cruzamento(pai2, pai1, n)
            filho1 = mutacao(filho1, taxa_mutacao, n)
            filho2 = mutacao(filho2, taxa_mutacao, n)
            nova_populacao.extend([filho1, filho2])

        populacao = nova_populacao
        fitnesses = [fitness(individuo, n) for individuo in populacao]
        total_individuos_avaliados += tamanho_populacao  # Incrementar o contador

        # Verificar se encontramos uma solução
        for i, f in enumerate(fitnesses):
            if f == 0:  # Sem ataques
                fim = time.time()
                return {
                    "solucao": populacao[i],
                    "geracoes": geracao + 1,
                    "tempo": fim - inicio,
                    "num_nos": total_individuos_avaliados,
                    "melhor_fitness": max(fitnesses),
                    "media_fitness": sum(fitnesses) / len(fitnesses),
                    "geracao": geracao + 1
                }

    # Fase de Backtracking
    for individuo in populacao:
        if fitness(individuo, n) > -10:  # Apenas indivíduos com poucos ataques
            solucao = backtracking_corrigir(individuo, n)
            if solucao:
                fim = time.time()
                return {
                    "solucao": solucao,
                    "geracoes": geracoes,
                    "tempo": fim - inicio,
                    "num_nos": total_individuos_avaliados,
                    "melhor_fitness": max(fitnesses),
                    "media_fitness": sum(fitnesses) / len(fitnesses),
                    "geracao": geracoes
                }

    fim = time.time()
    return {
        "solucao": None,
        "geracoes": geracoes,
        "tempo": fim - inicio,
        "num_nos": total_individuos_avaliados,
        "melhor_fitness": max(fitnesses),
        "media_fitness": sum(fitnesses) / len(fitnesses),
        "geracao": geracoes
    }