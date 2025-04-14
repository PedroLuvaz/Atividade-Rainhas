import matplotlib.pyplot as plt
import numpy as np
import json
from collections import defaultdict

def carregar_dados_estatisticas(caminho_arquivo):
    with open(caminho_arquivo, 'r') as f:
        return json.load(f)

def organizar_dados_brutos(dados_brutos):
    algoritmos = defaultdict(lambda: {"tempo": {}, "nos": {}})
    todos_ns = set()
    
    ignorar_algoritmos = {"Genético", "PSO"}  # <-- Aqui ignoramos esses dois

    for entrada in dados_brutos:
        n = entrada["tamanho"]
        alg = entrada["algoritmo"]
        if alg in ignorar_algoritmos:
            continue
        tempo = entrada["tempo"]
        nos = entrada["nos"]
        algoritmos[alg]["tempo"][n] = tempo
        algoritmos[alg]["nos"][n] = nos
        todos_ns.add(n)

    n_values = sorted(todos_ns)
    resultado = {
        "n_values": n_values,
        "algorithms": {},
        "colors": {
            "DFS": "blue",
            "BFS": "orange",
            "UCS": "green",
            "A*": "red",
        }
    }

    for alg, dados in algoritmos.items():
        resultado["algorithms"][alg] = {
            "tempo": [dados["tempo"].get(n, None) for n in n_values],
            "nos": [dados["nos"].get(n, None) for n in n_values],
        }

    return resultado


def plotar_grafico_comparacao(data):
    plt.figure(figsize=(12, 6))

    def plotar_linha(tempos, label, cor):
        x_validos = [n for n, t in zip(data['n_values'], tempos) if t is not None]
        y_validos = [t for t in tempos if t is not None]
        plt.plot(x_validos, y_validos, label=label, marker='o', color=cor)

    for alg, dados in data.get("algorithms", {}).items():
        plotar_linha(dados["tempo"], f"{alg} (Tempo)", data["colors"].get(alg, "black"))

    plt.title("Comparação de Tempo entre Algoritmos para o Problema das N-Rainhas com Bloqueios")
    plt.xlabel("Tamanho do Tabuleiro (N)")
    plt.ylabel("Tempo (s)")
    plt.ylim(0, 1100)
    plt.xscale('log', base=2)
    plt.xticks(data["n_values"], labels=[str(n) for n in data["n_values"]])
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()


def plotar_grafico_nos(data):
    plt.figure(figsize=(12, 6))

    def plotar_linha(nos, label, cor):
        x_validos = [n for n, t in zip(data['n_values'], nos) if t is not None]
        y_validos = [t for t in nos if t is not None]
        plt.plot(x_validos, y_validos, label=label, marker='o', color=cor)

    for alg, dados in data.get("algorithms", {}).items():
        plotar_linha(dados["nos"], f"{alg} (Nós)", data["colors"].get(alg, "black"))

    plt.title("Comparação de Nós Gerados entre Algoritmos para o Problema das N-Rainhas com Bloqueios")
    plt.xlabel("Tamanho do Tabuleiro (N)")
    plt.ylabel("Número de Nós")
    plt.yscale('log')  # Escala logarítmica para facilitar a visualização
    plt.xscale('log', base=2)
    plt.xticks(data["n_values"], labels=[str(n) for n in data["n_values"]])
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    dados_brutos = carregar_dados_estatisticas("estatisticas.json")
    dados_formatados = organizar_dados_brutos(dados_brutos)
    plotar_grafico_comparacao(dados_formatados)  # Gráfico de tempo
    plotar_grafico_nos(dados_formatados)        # Gráfico de nós gerados