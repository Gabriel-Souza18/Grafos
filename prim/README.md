# Algoritmo de Prim
O algoritmo de Prim é usado para encontrar uma árvore geradora mínima em um grafo não direcionado e ponderado. A árvore geradora mínima é um subconjunto das arestas do grafo que conecta todos os vértices juntos sem ciclos e com o peso total mínimo.

# Função Principal
```
def prim(grafo: nx.Graph):
    fila = Fila()

    [...]

    while fila.lista:
        no_atual = fila.select_min(arvore_geradora_minima)
        arvore_geradora_minima.add_node(no_atual.no)  

        for adj, attrs in grafo.adj[no_atual.no].items():  
            peso = attrs.get('weight', float('inf')) 
            if adj in fila.lista and peso < fila.lista[adj].peso:  
                [...]
                arvore_geradora_minima.add_edge(no_atual.no, adj, weight=peso)

    return arvore_geradora_minima
```
# Dependências
Para rodar o algoritmo de Prim, você precisará das seguintes bibliotecas:

* NetworkX: Biblioteca para criação, manipulação e estudo da estrutura, dinâmica e funções de grafos complexos.
* Matplotlib: Biblioteca para geração de gráficos e visualização de dados.

# Como Usar
Prepare o arquivo de entrada:

Crie um arquivo de texto com o formato origem, destino, peso, onde origem e destino são os vértices e peso é o peso da aresta entre eles.
Execute o script:

Certifique-se de que o arquivo de entrada está no mesmo diretório que o script ou forneça o caminho correto.
Execute o script Python que contém a função main()

Visualize a saída:
O algoritmo gerará um arquivo PNG com a visualização da árvore geradora mínima na pasta prim/.