import networkx as nx
import matplotlib.pyplot as plt

INF = 100000

def plot_graph(grafo):
    pos = nx.circular_layout(grafo)  # Posições para todos os nós

    # Nós
    nx.draw_networkx_nodes(grafo, pos, node_size=200)

    # Arestas
    nx.draw_networkx_edges(grafo, pos, edgelist=grafo.edges, width=2)
    
    edge_labels = nx.get_edge_attributes(grafo, 'weight')
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=edge_labels)
    # Rótulos
    nx.draw_networkx_labels(grafo, pos, font_size=12, font_family='sans-serif')

    plt.axis('on')
    plt.show()

def peso(grafo, no1, no2):
    if grafo.has_edge(no1, no2): #retorna o peso da aresta
        return (grafo[no1][no2]['weight'])
    else: #retorna None se a aresta não existir
        return None

def ler_dados_entrada(nome_arquivo):
    grafo = nx.DiGraph()
    arq = open(nome_arquivo, "r") # abre o arquivo
    for linha in arq:
        origem, destino, peso = linha.strip().split(",");
        grafo.add_edge(int(origem),int(destino), weight=int(peso))
    return grafo

def imprimir_dados_das_arestas(grafo): # pra testar se leu o arquivo corretamente 
    for i in grafo.nodes:
        sucessores = list(grafo.successors(i))
        for vizinho in sucessores:
            dados_aresta = grafo.get_edge_data(i, vizinho)
            if dados_aresta:
                print(f"Aresta entre {i} e {vizinho}: {dados_aresta}")
            else:
                print(f"Não há aresta entre {i} e {vizinho}")

def pert_cpm(grafo):
    tempo_max = {no: 0 for no in grafo.nodes}
    tempo_min ={no: INF for no in grafo.nodes}
    folga = {no: 0 for no in grafo.nodes}
    #calcula tempo maximo
    for no in grafo.nodes:
        vizinhos = grafo.predecessors(no)
        for vizinho in vizinhos:
            peso_aresta = peso(grafo, vizinho, no)
            tempo_max[no] = max(tempo_max[no],tempo_max[vizinho] + peso_aresta)
    print(f"Tempo Maximo:"+str(dict(tempo_max)))

    #calcula folga
    for no in reversed(list(grafo.nodes)):
        vizinhos = grafo.successors(no)
        for vizinho in vizinhos:
            peso_aresta = peso(grafo, no, vizinho)
            if tempo_max[vizinho] - peso_aresta > tempo_max[no]:
                folga[no] = tempo_max[vizinho] - tempo_max[no]
    print(f"Folgas: "+str(dict(folga)))
    
grafo = ler_dados_entrada("pert\entrada.txt")


pert_cpm(grafo)
plot_graph(grafo)
