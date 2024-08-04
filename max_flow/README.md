# Algoritimo Ford_fulkerson
Esse algoritmo calcula o fluxo maximo de um grafo direcionado

## Funcao Principal
```python
    def Max_flow(grafo: nx.DiGraph):
    max_flow = 0
    while True:
        [...]
        
        while no_atual != 't':
            
            proximo = Selecionar_maior(grafo, no_atual)
            if proximo is None:
                break  
            caminho_atual.append(proximo)
            no_atual = proximo
        if no_atual == 't':
           [...]
            
            
        print("Fluxo Maximo:", max_flow)
        print_grafo(grafo)
```
## Exemplo de saida
Fluxo Maximo: 60

Aresta entre s e a: {'capacidade': 10, 'caminho_valido': False}<br>
Aresta entre s e c: {'capacidade': 20, 'caminho_valido': False}<br>
Aresta entre a e b: {'capacidade': 70, 'caminho_valido': False}<br>
Aresta entre a e d: {'capacidade': 30, 'caminho_valido': False}<br>
Aresta entre c e b: {'capacidade': 30, 'caminho_valido': False}<br>
Aresta entre b e t: {'capacidade': 0, 'caminho_valido': False}<br>
Aresta entre d e t: {'capacidade': 0, 'caminho_valido': False}<br>


## Para rodar 
Tem que intalar as bibliotecas:
* Networkx\
Site com tutorial para instalação:
https://networkx.org/documentation/stable/install.html