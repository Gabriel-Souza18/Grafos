import networkx as nx
import matplotlib.pyplot as plt

def plot_grafo(grafo: nx.Graph, nome):
    pos = nx.spring_layout(grafo)  # Define a posição dos nós
    labels = nx.get_edge_attributes(grafo, 'weight')  
    nx.draw(grafo, pos, with_labels=True, node_size=500, font_size=10)  # Plota o grafo
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=labels)
    plt.savefig("prim/"+nome+".png")  # Exibe o gráfico

def print_grafo(grafo: nx.Graph):
    for n, nbrs in grafo.adj.items():
        for nbr, eattr in nbrs.items():
            wt = eattr.get('weight', 'no weight')  
            print(f"({n}, {nbr}, {wt})")
    
def ler_arquivo(nome_arquivo):
    grafo = nx.Graph()
    with open(nome_arquivo, "r") as arq:
        for linha in arq:
            origem, destino, peso = linha.strip().split(", ")
            grafo.add_edge(origem, destino, weight=int(peso))  
    return grafo

import networkx as nx

class Item_fila:
    def __init__(self, no, peso=float('inf'), pre_no=None):
        self.no = no
        self.peso = peso
        self.pre_no = pre_no

class Fila:
    def __init__(self):
        self.lista = {}

    def select_min(self, arvore_geradora_minima):
        min_item = None
        for item in self.lista.values():
            if item.no not in arvore_geradora_minima.nodes:
                if min_item is None or item.peso < min_item.peso:
                    min_item = item
        if min_item:
            del self.lista[min_item.no]
        return min_item

def prim(grafo: nx.Graph):
    fila = Fila()

    for node in grafo.nodes:
        fila.lista[node] = Item_fila(node)

    start_node = next(iter(grafo.nodes))  
    fila.lista[start_node].peso = 0
    arvore_geradora_minima = nx.Graph()

    while fila.lista:
        no_atual = fila.select_min(arvore_geradora_minima)
        if no_atual is None:
            break
        arvore_geradora_minima.add_node(no_atual.no)  

        for adj, attrs in grafo.adj[no_atual.no].items():  
            peso = attrs.get('weight', float('inf'))  
            if adj in fila.lista and peso < fila.lista[adj].peso:  
                fila.lista[adj].pre_no = no_atual.no
                fila.lista[adj].peso = peso
                arvore_geradora_minima.add_edge(no_atual.no, adj, weight=peso)

    return arvore_geradora_minima

def main():
    grafo = ler_arquivo("prim/grafo.txt")  
    #plot_grafo(grafo, 'completo')

    arvore_min = prim(grafo)
    plot_grafo(arvore_min, 'min')
    
if __name__ == "__main__":
    main()
