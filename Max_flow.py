import networkx as nx


def main():
    grafo = ler_arquivo("grafo.txt")
    print_grafo(grafo)

def ler_arquivo(nome_arquivo):
    grafo = nx.DiGraph()
    arq = open(nome_arquivo, "r")
    for linha in arq:
        origem, destino, peso = linha.strip().split(" ");
        grafo.add_edge(origem,destino, capacidade=int(peso))
    return grafo

def print_grafo(grafo: nx.DiGraph):
    for i in grafo.nodes:
        sucessores = list(grafo.successors(i))
        for vizinho in sucessores:
            dados_aresta = grafo.get_edge_data(i, vizinho)
            if dados_aresta:
                print(f"Aresta entre {i} e {vizinho}: {dados_aresta}")
            else:
                print(f"Não há aresta entre {i} e {vizinho}")

        


main()