import networkx as nx
import matplotlib.pyplot as plt
    
def plotar_grafo(grafo):
    pos = nx.circular_layout(grafo)
    nx.draw(grafo, pos, with_labels=True)
    plt.show()

def lergrafo():
    grafo = nx.read_gml("oito_rainhas/Tabuleiro_com_incompatibilidades.gml")
    return grafo

def is_safe(solucao, linha, coluna):#confere se é seguro colocar uma rainha 
    for i in range(linha):
        if solucao[i] == coluna or \
           solucao[i] - i == coluna - linha or \
           solucao[i] + i == coluna + linha:
            return False
    return True

def solve_oito_rainhas(grafo, solucao, linha):
    if linha == len(grafo.nodes()):#condicao de parada
        return True
    
    for coluna in range(len(grafo.nodes())):
        if is_safe(solucao, linha, coluna):
            solucao[linha] = coluna
            if solve_oito_rainhas(grafo, solucao, linha + 1):#funcao recursiva
                return True
            solucao[linha] = -1
    return False

def oito_rainhas(grafo):
    solucao = [-1] * len(grafo.nodes())#todas os valores como -1, ou seja nenhuma rainha colocada
    if solve_oito_rainhas(grafo, solucao, 0):
        return solucao
    else:
        return None

def main():
    grafo = lergrafo()
    solucao = oito_rainhas(grafo)
    if solucao:
        print("Solução encontrada:")
        for linha, coluna in enumerate(solucao):
            print(f"Rainha na linha {linha}, coluna {coluna}")
    else:
        print("Nenhuma solução encontrada")

if __name__ == "__main__":
    main()