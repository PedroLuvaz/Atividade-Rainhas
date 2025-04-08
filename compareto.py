import matplotlib.pyplot as plt
import numpy as np
import json
from collections import defaultdict

def carregar_dados_estatisticas(caminho_arquivo):
    with open(caminho_arquivo, 'r') as f:
        return json.load(f)

def organizar_dados_brutos(dados_brutos):
    algoritmos = defaultdict(dict)
    todos_ns = set()
    
    for entrada in dados_brutos:
        n = entrada["tamanho"]
        alg = entrada["algoritmo"]
        tempo = entrada["tempo"]
        algoritmos[alg][n] = tempo
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
            "Genético": "purple",
            "PSO": "brown"
        }
    }

    for alg, tempos_por_n in algoritmos.items():
        resultado["algorithms"][alg] = [tempos_por_n.get(n, None) for n in n_values]

    return resultado

def plotar_grafico_comparacao(data):
    plt.figure(figsize=(12, 6))

    def plotar_linha(tempos, label, cor):
        x_validos = [n for n, t in zip(data['n_values'], tempos) if t is not None]
        y_validos = [t for t in tempos if t is not None]
        plt.plot(x_validos, y_validos, label=label, marker='o', color=cor)
        for n, t in zip(data['n_values'], tempos):
            if t is None:
                plt.scatter(n, 1000, marker='x', color=cor)
                plt.text(n, 1050, f"{label}\nInviável", ha='center', fontsize=8)

    for alg, tempos in data.get("algorithms", {}).items():
        plotar_linha(tempos, alg, data["colors"].get(alg, "black"))

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

if __name__ == "__main__":
    dados_brutos = carregar_dados_estatisticas("estatisticas.json")
    dados_formatados = organizar_dados_brutos(dados_brutos)
    plotar_grafico_comparacao(dados_formatados)
