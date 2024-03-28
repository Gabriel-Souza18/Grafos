import networkx as nx
import matplotlib.pyplot as plt

# Crie um MultiGraph
grafo = nx.MultiGraph()

# Adicione os vértices
grafo.add_nodes_from([1, 5])

# Adicione as arestas paralelas com pesos diferentes e keys distintos
grafo.add_edge(1, 5, weight=10, key=0)  # Primeira aresta com peso 10
grafo.add_edge(1, 5, weight=20, key=1)  # Segunda aresta com peso 20

# Exiba os vértices e arestas
print(list(grafo.nodes))
print(list(grafo.edges))

# Desenhe o grafo
pos = nx.spring_layout(grafo)
nx.draw_networkx(grafo, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=10, font_color='black', font_weight='bold')
labels = {(1, 5, 0): 10, (1, 5, 1): 20}  # Dicionário de rótulos de aresta
nx.draw_networkx_edge_labels(grafo, pos, edge_labels=labels)
plt.axis('off')
plt.show()
