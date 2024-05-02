from GraphPack.Graph import Graph

import random as rnd


vertice_number = 5
g = Graph() # Criar um Grafo não orientado
lst = [i for i in range(0, vertice_number)]
vert = []                  # lista auxiliar para guardar os vértices inseridos para construção das arestas
for i in lst:
    #print(f"creating vertice {i}")
    vert.append(g.insert_vertex(i))  # inserção dos vertices V = {0, 1, ..., 9} no grafo e na lista de vertices
    #print(f"number of vertices {g._n}")

rnd.seed(10)                                # para futura replicação deste grafo
for i in range(1, 9):                       # criação de 20 arestas a partir dos vértices inseridos
    u, v = rnd.sample(lst, k=2)             # gerar aleatoriamente uma aresta entre 2 vértices deste grafo
    x = rnd.randint(1, 10)                  # com peso inteiro aleatório entre 0 e 10
    #print(f"iteração {i} aresta {u} e {v} com peso {x}")
    g.insert_edge(vert[u], vert[v], x)      # inserção desta aresta no grafo
    #print(f"number of arestas {g._m}")

print(g)