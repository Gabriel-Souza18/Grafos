import networkx as nx


def main():
    grafo = ler_arquivo("max_flow\grafo.txt")
    Max_flow(grafo)

def ler_arquivo(nome_arquivo):
    grafo = nx.DiGraph()
    arq = open(nome_arquivo, "r")
    for linha in arq:
        origem, destino, peso = linha.strip().split("/");
        grafo.add_edge(origem,destino, capacidade=int(peso), caminho_valido = True)
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

def Selecionar_maior(grafo: nx.DiGraph, node):
    proximo_no = None  
    for nodevizinho in grafo.successors(node):
        if proximo_no is None or grafo[node][nodevizinho]['capacidade'] >= grafo[node][proximo_no]['capacidade'] and grafo[node][nodevizinho]['caminho_valido'] == True:
            
            proximo_no = nodevizinho
    return proximo_no

def menor_capacidade(grafo: nx.DiGraph, caminho: list):
    menor_capacidade = float('inf')
    for i in range(len(caminho) - 1):
        origem, destino = caminho[i], caminho[i + 1]
        capacidade_arco = grafo[origem][destino]['capacidade']
        menor_capacidade = min(menor_capacidade, capacidade_arco)
        
    return menor_capacidade
        
def subtrair_capacidade(grafo: nx.DiGraph, caminho):
    for i in range(len(caminho) - 1):
        origem, destino = caminho[i], caminho[i + 1]
        grafo[origem][destino]['capacidade'] -= menor_capacidade(grafo, caminho)
        if grafo[origem][destino]['capacidade'] == 0:
            grafo[origem][destino]['caminho_valido'] = False
        
def Max_flow(grafo: nx.DiGraph):
    max_flow = 0
    caminho_atual=[]
    
    while True:
        
        print_grafo(grafo)
        caminho_atual = ['s']
        no_atual = Selecionar_maior(grafo, 's')
        caminho_atual.append(no_atual)
        while True:
            proximo = Selecionar_maior(grafo, no_atual)
            caminho_atual.append(proximo)
            no_atual = proximo
            
            if no_atual == 't':
                print(caminho_atual)
                max_flow += menor_capacidade(grafo, caminho_atual)
                subtrair_capacidade(grafo, caminho_atual)
                print(max_flow)
                
                break
       
            
            
            
               


main()