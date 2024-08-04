import networkx as nx
import matplotlib.pyplot as plt

def plot_grafo(grafo: nx.Graph):
    pos = nx.spring_layout(grafo)  # Define a posição dos nós
    labels = nx.get_edge_attributes(grafo, 'peso')
    nx.draw(grafo, pos, with_labels=True, node_size=500, font_size=10)  # Plota o grafo
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=labels)
    plt.show()  # Exibe o gráfico

def print_grafo(grafo: nx.Graph):
    for n, nbrs in grafo.adj.items():
        for nbr, eattr in nbrs.items():
            wt = eattr['peso']
            print(f"({n}, {nbr}, {wt})")

     
                    
                
def ler_arquivo(nome_arquivo):
    grafo = nx.Graph()
    with open(nome_arquivo, "r") as arq:
        for linha in arq:
            origem, destino, peso = linha.strip().split(", ")
            grafo.add_edge(origem, destino, peso=int(peso))
    return grafo

class Item_fila:
    def __init__(self, no):
        self.no = no
        self.peso = float('inf')
        self.pre_no = None
        
class Fila:
    def __init__(self):
        self.lista = {}
    
    
    def select_min(self):
        min = None
        for item in self.lista.values():
            if min == None or item.peso < min.peso :
                min = item
        
        del self.lista[min]
        return min
        
def prim(grafo : nx.Graph):
    fila = Fila()
    
    for node in grafo.nodes:
        fila.lista[node] = (Item_fila(node))
 
    fila.lista['A'].peso = 0   
    
    while fila.lista:
        no_atual = fila.select_min();
        for adj in grafo.adjacency(no_atual):
            if adj in fila.lista and grafo.get_edge_data(adj, no_atual) < fila.lista[adj].peso:
                fila.lista[adj].pre_no = no_atual
                fila.lista[adj].peso = grafo.get_edge_data(adj, no_atual)
    
    print(fila.lista)

def main():
    grafo = ler_arquivo("prim\grafo.txt")
    
    #plot_grafo(grafo)
    prim(grafo)
    
main()