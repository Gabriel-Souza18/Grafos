import networkx as nx

INF = 1000000 # Usado como "infinito" so pra ficar mais facil de escrever
ORIGEM = 4 # no de origem, tem que estar no grafo


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

#retorna o no mais perto
def minimo(lista, chave=None):
    minimo = None
    
    for item in lista:
        valor_chave = chave(item) if chave else item
        if minimo is None or (chave and chave(item) < chave(minimo)) or (not chave and item < minimo):
            minimo = item
    return minimo

def peso(grafo, no1, no2):
    if grafo.has_edge(no1, no2): #retorna o peso da aresta
        return (grafo[no1][no2][0]['weight'])
    else: #retorna None se a aresta não existir
        return None

def dijkstra(grafo, origem):
    distancias ={}
    caminhos = {}
    caminhos[origem] = [origem]

    for i in  grafo.nodes: # preenche as distancias como infinito, nesse caso so um numero grande
        distancias[i] = INF
    distancias[origem] = 0 #distancia da origem é 0

    aberto = list(grafo.nodes)
    fechado = []
    print(aberto)

    while aberto:
        no_atual = minimo(aberto, chave=lambda no: distancias[no])
        aberto.remove(no_atual)
        fechado.append(no_atual)
       

        for vizinho in grafo.successors(no_atual):
            caminho_atual =[] # deixar aqui pra limpar o caminho atual
            #soma a distancia do no atual com o peso pro proximo no
            dist_teste = distancias[no_atual]+ peso(grafo, no_atual,vizinho) 
            if dist_teste < distancias[vizinho]:
                distancias[vizinho] = dist_teste
                caminho_atual.append(no_atual)
                caminho_atual.append(vizinho)
                caminhos[vizinho] = caminho_atual

    imprimir_distancias_e_caminho(distancias, caminhos)
    return distancias
  
        

def imprimir_distancias_e_caminho(distancias, caminho):
    for i in distancias:
        print(f'\nDistacia da origem ate {i}: {distancias[i]}')
        print(f'Caminho percorrido: {list(caminho[i])} ')

def imprimir_dados_das_arestas(grafo): # pra testar se leu o arquivo corretamente 
    for i in grafo.nodes:
        sucessores = list(grafo.successors(i))
        for vizinho in sucessores:
            dados_aresta = grafo.get_edge_data(i, vizinho)
            if dados_aresta:
                print(f"Aresta entre {i} e {vizinho}: {dados_aresta}")
            else:
                print(f"Não há aresta entre {i} e {vizinho}")


grafo = ler_dados_entrada("entrada.txt")

#imprimir_dados_das_arestas(grafo)
dijkstra(grafo, ORIGEM)
