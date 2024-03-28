import networkx as nx


def ler_dados_entrada(nome_arquivo):
    grafo = nx.MultiDiGraph()
    arq = open(nome_arquivo, "r") # abre o arquivo
    for i in range(0, 9):
        linha = arq.readline()
        #separa os itens da linha
        edgeComeco = int((linha[0]))
        edgeFinal = int((linha[1]))
        edgePeso = int((linha[2]))

        grafo.add_nodes_from([edgeComeco, edgeFinal])
        grafo.add_edge(edgeComeco, edgeFinal, weight=edgePeso)
    arq.close()
    return grafo


def vizinho_perto(vizinhos, no):
    mais_perto = None
    vizinhos_ordenado = []
    indice = 0
    if vizinhos:
        mais_perto = vizinhos[0]
        for j in vizinhos:
            if peso(grafo, no, j) < peso(grafo, no, mais_perto):
                if mais_perto not in vizinhos_ordenado:
                    vizinhos_ordenado.append(mais_perto)
        print(f'Vizinho mais perto do nó {no}: {mais_perto}')
    return vizinhos_ordenado

def peso(grafo, no1, no2):
    if grafo.has_edge(no1, no2):
        # Retorna o peso da aresta
        return grafo[no1][no2]['weight']
    else:
        # Retorna None se a aresta não existir
        return None

def dijkstra(grafo, origem):
    distancias = {}
    visitados = []
    #Coloca as distancias em infinito
    for i in grafo.nodes:
        distancias[i] = float('inf')
    distancias[origem] = 0 #Menos a da origem

    for i in grafo.nodes:
        vizinhos_i = vizinho_perto(list(grafo.successors(i)), i)
        for j in vizinhos_i:
            vizinhos_j = vizinho_perto(vizinhos_i, j)


def imprimir_dados_das_arestas(grafo):
    for i in grafo.nodes:
        sucessores = list(grafo.successors(i))
        for vizinho in sucessores:
            dados_aresta = grafo.get_edge_data(i, vizinho)
            if dados_aresta:
                print(f"Aresta entre {i} e {vizinho}: {dados_aresta}")
            else:
                print(f"Não há aresta entre {i} e {vizinho}")


grafo = ler_dados_entrada("entrada.txt")

imprimir_dados_das_arestas(grafo)
dijkstra(grafo, 1)
