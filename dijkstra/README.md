# Algoritimo de Dijkstra
Esse programa lê um arquivo de entrada e cria um grafo, partit desse grafo e de uma origem, mede o caminho minimo para todos os vertices.
## Funçao principal
```python
def dijkstra(grafo, origem):

    [...]

    while aberto:
        no_atual = minimo(aberto, chave=lambda no: distancias[no])
        aberto.remove(no_atual)
        fechado.append(no_atual)
       

        for vizinho in grafo.successors(no_atual):
            caminho_atual =[] 
            dist_teste = distancias[no_atual]+ peso(grafo, no_atual,vizinho) 
            if dist_teste < distancias[vizinho]:
                distancias[vizinho] = dist_teste
                caminho_atual.append(no_atual)
                caminho_atual.append(vizinho)
                caminhos[vizinho] = caminho_atual

    imprimir_distancias_e_caminho(distancias, caminhos)
    return distancias
```
## Exemplo de saida
```
Distacia da origem ate 1: 3
Caminho percorrido: [4, 1] 

Distacia da origem ate 2: 4
Caminho percorrido: [1, 2] 

Distacia da origem ate 5: 5
Caminho percorrido: [1, 5]

Distacia da origem ate 3: 5
Caminho percorrido: [2, 3]

Distacia da origem ate 4: 0
Caminho percorrido: [4]
```