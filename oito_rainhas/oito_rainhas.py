import networkx as nx
import matplotlib.pyplot as plt
    
def plotar_grafo(grafo):
    pos = nx.spring_layout(grafo)
    nx.draw_networkx(grafo, pos, with_labels=True, arrows=True)
    plt.show()

def lergrafo():
    grafo = nx.read_gml("oito_rainhas/Tabuleiro_com_incompatibilidades.gml")
    return grafo


def oito_rainhas(grafo: nx.Graph):
    nodes = list(grafo.nodes())
    solucao = []
    ultimos_selecionados = []
    
    while len(solucao)< 8:
        nao_considerados = nodes.copy()
        solucao = []
        for i in ultimos_selecionados:
            nao_considerados.remove(i)
        while nao_considerados:
            node_selecionado = nao_considerados.pop(0)
            ultimos_selecionados.append(node_selecionado)
            if node_selecionado not in solucao:
                solucao.append(node_selecionado)
                
                if node_selecionado in nao_considerados:
                    nao_considerados.remove(node_selecionado)
                    
                for vizinho in grafo.neighbors(node_selecionado):
                    if vizinho in nao_considerados:
                        nao_considerados.remove(vizinho)
                         
        return solucao
def main():
    grafo = lergrafo()
    print(oito_rainhas(grafo))
if __name__ == "__main__":
    main()