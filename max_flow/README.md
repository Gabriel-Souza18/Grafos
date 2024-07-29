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
# Exemplo de saida
