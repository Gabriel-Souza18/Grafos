import networkx as nx
import time

def print_grafo(grafo: nx.DiGraph):
    for i in grafo.nodes:
        sucessores = list(grafo.successors(i))
        for vizinho in sucessores:
            dados_aresta = grafo.get_edge_data(i, vizinho)
            if dados_aresta:
                print(f"Aresta entre {i} e {vizinho}: {dados_aresta}")
            else:
                print(f"Não há aresta entre {i} e {vizinho}")
                
                
def ler_arquivo(nome_arquivo):
    grafo = nx.DiGraph()
    with open(nome_arquivo, "r") as arq:
        for linha in arq:
            origem, destino, peso = linha.strip().split("/")
            grafo.add_edge(origem, destino, capacidade=int(peso), caminho_valido=True)
    return grafo

def Selecionar_maior(grafo: nx.DiGraph, node):
    proximo_no = None
    
    for nodevizinho in grafo.successors(node):
        if grafo[node][nodevizinho]['caminho_valido']:
            if proximo_no is None or (grafo[node][nodevizinho]['capacidade'] >= grafo[node][proximo_no]['capacidade']):
                proximo_no = nodevizinho
                
    if proximo_no == None:
        for pre_node in grafo.predecessors(node):
                grafo[pre_node][node]['caminho_valido']= False
    return proximo_no

def menor_capacidade(grafo: nx.DiGraph, caminho: list):
    menor_capacidade = float('inf')
    for i in range(len(caminho) - 1):
        origem, destino = caminho[i], caminho[i + 1]
        capacidade_arco = grafo[origem][destino]['capacidade']
        menor_capacidade = min(menor_capacidade, capacidade_arco)
    return menor_capacidade

def subtrair_capacidade(grafo: nx.DiGraph, caminho):
    cap_min = menor_capacidade(grafo, caminho)
    for i in range(len(caminho) - 1):
        origem, destino = caminho[i], caminho[i + 1]
        
        grafo[origem][destino]['capacidade'] -= cap_min
        
        if grafo[origem][destino]['capacidade'] == 0:
            grafo[origem][destino]['caminho_valido'] = False
            for node in grafo.predecessors(origem):
                grafo[node][origem]['caminho_valido'] = False
                
                
def Max_flow(grafo: nx.DiGraph):
    max_flow = 0
    while True:
        
        caminho_atual = ['s']
        no_atual = Selecionar_maior(grafo, 's')
        if no_atual is None:
            break 
        caminho_atual.append(no_atual)
        
        while no_atual != 't':
            
            proximo = Selecionar_maior(grafo, no_atual)
            if proximo is None:
                break  
            caminho_atual.append(proximo)
            no_atual = proximo
        if no_atual == 't':
            max_flow += menor_capacidade(grafo, caminho_atual)
            subtrair_capacidade(grafo, caminho_atual)
            print("Caminho percorrido"+str(caminho_atual))
            
            
        print("Maximum flow:", max_flow)
        print_grafo(grafo)

def main():
    grafo = ler_arquivo("max_flow/grafo.txt")
    print_grafo(grafo)
    Max_flow(grafo)

if __name__ == "__main__":
    main()
