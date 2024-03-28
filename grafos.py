import networkx as nx

grafo = nx.MultiDiGraph()
arq = open("entrada.txt", "r")
for i in range(0, 9):
    linha = arq.readline()
    edgeComeco = int((linha[0]))
    edgeFinal = int((linha[1]))
    edgePeso = int((linha[2]))

    grafo.add_nodes_from([edgeComeco, edgeFinal])
    grafo.add_edge(edgeComeco, edgeFinal, weight=edgePeso)

print(list(grafo.nodes))
print(list(grafo.edges))
print(list(grafo.successors(5)))
print(list(grafo.predecessors(5)))
