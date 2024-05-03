from GraphPack.Graph import Graph
import random as rnd
import string  # Importar para usar string.ascii_letters

vertice_number = 5
g = Graph()  # Criar um Grafo não orientado
lst = [i for i in range(0, vertice_number)]
vert = []  # lista auxiliar para guardar os vértices inseridos para construção das arestas

for i in lst:
    vert.append(g.insert_vertex(i))  # inserção dos vertices V = {0, 1, ..., 4} no grafo e na lista de vertices

rnd.seed(10)  # para futura replicação deste grafo

# Vamos criar 9 arestas como no código original
for i in range(1, 9):  # criação de 9 arestas a partir dos vértices inseridos
    u, v = rnd.sample(lst, k=2)  # gerar aleatoriamente uma aresta entre 2 vértices deste grafo
    x = rnd.choice(string.ascii_letters)  # com label sendo uma letra aleatória
    # print(f"iteração {i} aresta {u} e {v} com label {x}")
    g.insert_edge(vert[u], vert[v], x)  # inserção desta aresta no grafo
    # print(f"number of arestas {g._m}")

print(g)
print(g.has_node(vert[2]))
print(g.has_AnyEdge(vert[2], vert[1]))
print(g.has_especificEdge(vert[2], vert[1], "c"))
print(g.get_edge(vert[2], vert[1],"c"))
