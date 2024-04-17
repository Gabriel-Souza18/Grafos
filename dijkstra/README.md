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