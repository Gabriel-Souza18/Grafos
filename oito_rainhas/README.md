# Oito Rainhas
Esse programa resolve o problema das 8 rainhas, lendo um arquivo contendo um grafo, com incompatibilidades das rainhas, e imprimindo a solução

## Função principal
```
def oito_rainhas(grafo: nx.Graph):
    [...]
    
    while len(solucao)< 8:
        [...]
        while nao_considerados:
            node_selecionado = nao_considerados.pop(0)
            ultimos_selecionados.append(node_selecionado)
            if node_selecionado not in solucao:
                solucao.append(node_selecionado)
                
                if node_selecionado in nao_considerados:
                    nao_considerados.remove(node_selecionado)
                    
                for vizinho in grafo.neighbors(node_selecionado):
                    if vizinho in nao_considerados:
                        nao_considerados.remove(vizinho)
                         
        return solucao
```
## Exemplo de saida
```
['3', '9', '22', '28', '32', '47', '53', '58']
```
## Para rodar 
Tem que intalar as bibliotecas:
* Networkx\
Site com tutorial para instalação:
https://networkx.org/documentation/stable/install.html

* Matplotlib\
Site com tutorial para instalação:
https://matplotlib.org/stable/users/installing/index.html

### Feito por
 Gabriel da Silva Souza<br>
* Email - gabrielsisou@gmail.com
