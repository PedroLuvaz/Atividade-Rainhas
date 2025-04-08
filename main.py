import time
import json
from Utils.util import gerar_bloqueios, imprimir_tabuleiro
from Algoritmos.dfs_solver import resolver_dfs
from Algoritmos.bfs_solver import resolver_bfs
from Algoritmos.ucs_solver import resolver_ucs
from Algoritmos.astar_solver import resolver_astar



def salvar_estatisticas(tempo, tamanho, algoritmo):
    dados = {
        "tamanho": tamanho,
        "algoritmo": algoritmo,
        "tempo": tempo
    }
    try:
        with open("estatisticas.json", "r") as arquivo:
            historico = json.load(arquivo)
    except FileNotFoundError:
        historico = []

    historico.append(dados)

    with open("estatisticas.json", "w") as arquivo:
        json.dump(historico, arquivo, indent=4)


def executar_algoritmo(n, opcao):
    bloqueios = gerar_bloqueios(n)
    inicio = time.time()

    if opcao == "1":
        solucao = resolver_dfs(n, bloqueios)
        algoritmo = "DFS"
    elif opcao == "2":
        solucao = resolver_bfs(n, bloqueios)
        algoritmo = "BFS"
    elif opcao == "3":
        solucao = resolver_ucs(n, bloqueios)
        algoritmo = "UCS"
    elif opcao == "4":
        solucao = resolver_astar(n, bloqueios)
        algoritmo = "A*"
    else:
        print("Opção inválida.")
        return None, None

    fim = time.time()
    tempo_total = fim - inicio

    if solucao:
        print(f"\nSolução encontrada para n={n} em {tempo_total:.3f}s usando {algoritmo}")
        imprimir_tabuleiro(n, solucao, bloqueios)
        salvar_estatisticas(tempo_total, n, algoritmo)
    else:
        print(f"\nNenhuma solução encontrada para n={n} usando {algoritmo}.")

    return solucao, tempo_total


def main():
    while True:
        print("=== Problema das N-Rainhas com Bloqueios ===")
        print("1 - Rodar de forma comum")
        print("2 - Rodar de forma iterativa (intervalo de n)")
        escolha = input("Escolha uma opção (1-2): ").strip()

        if escolha == "1":
            while True:
                try:
                    n = int(input("Informe o valor de n (entre 8 e 512): "))
                    if 8 <= n <= 512:
                        break
                    else:
                        print("Por favor, insira um valor entre 8 e 512.")
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número inteiro.")

            print("\nAlgoritmos disponíveis:")
            print("1 - Busca em Profundidade (DFS)")
            print("2 - Busca em Largura (BFS)")
            print("3 - Busca de Custo Uniforme (UCS)")
            print("4 - A*")

            opcao = input("Escolha o algoritmo (1-4): ")
            executar_algoritmo(n, opcao)

        elif escolha == "2":
            while True:
                try:
                    n_inicio = int(input("Informe o valor inicial de n (mínimo 8): "))
                    if n_inicio >= 8:
                        break
                    else:
                        print("Por favor, insira um valor maior ou igual a 8.")
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número inteiro.")

            while True:
                try:
                    n_fim = int(input("Informe o valor final de n (máximo 512): "))
                    if n_fim <= 512:
                        break
                    else:
                        print("Por favor, insira um valor menor ou igual a 512.")
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número inteiro.")

            print("\nAlgoritmos disponíveis:")
            print("1 - Busca em Profundidade (DFS)")
            print("2 - Busca em Largura (BFS)")
            print("3 - Busca de Custo Uniforme (UCS)")
            print("4 - A*")

            opcao = input("Escolha o algoritmo (1-4): ")

            for n in range(n_inicio, n_fim + 1):
                print(f"\nExecutando para n={n}...")
                executar_algoritmo(n, opcao)

        else:
            print("Opção inválida.")
            continue

        repetir = input("\nDeseja rodar novamente? (s/n): ").strip().lower()
        if repetir != "s":
            break


if __name__ == "__main__":
    main()
