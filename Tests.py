from Graph import Graph, Vertex
import random as rnd
import string  # Importar para usar string.ascii_letters

from HollywoodOracle import HollywoodOracle

# vertice_number = 5
# g = Graph()  # Criar um Grafo não orientado
# lst = [i for i in range(0, vertice_number)]
# vert = []  # lista auxiliar para guardar os vértices inseridos para construção das arestas
#
# for i in lst:
#     vert.append(g.insert_vertex(i))  # inserção dos vertices V = {0, 1, ..., 4} no grafo e na lista de vertices
#
# rnd.seed(10)  # para futura replicação deste grafo
#
# # Vamos criar 9 arestas como no código original
# for i in range(1, 9):  # criação de 9 arestas a partir dos vértices inseridos
#     u, v = rnd.sample(lst, k=2)  # gerar aleatoriamente uma aresta entre 2 vértices deste grafo
#     x = rnd.choice(string.ascii_letters)  # com label sendo uma letra aleatória
#     # print(f"iteração {i} aresta {u} e {v} com label {x}")
#     g.insert_edge(vert[u], vert[v], x)  # inserção desta aresta no grafo
#     # print(f"number of arestas {g._m}")
#
#
#
# print(g)
# print(g.has_node(vert[2]))
# print(g.has_AnyEdge(vert[2], vert[1]))
# print(g.has_especificEdge(vert[2], vert[1], "c"))
# print(g.get_edge(vert[2], vert[1],"c"))

def build_graph_from_file(filename):
    graph = Graph()
    vertex_map = {}  # Cache vertex objects to avoid duplicate creation

    try:

        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split('/')
                if len(parts) < 2:
                    continue
                movie = parts[0].strip()
                actors = set(part.strip() for part in parts[1:])  # Use a set to remove duplicates

                # Ensure all vertex objects are created or retrieved from cache
                for actor in actors:
                    if actor not in vertex_map:
                        vertex_map[actor] = graph.insert_vertex(actor)
                    # No else needed, we only insert if not present

                # Generate edges without re-checking vertex existence
                actor_list = [vertex_map[actor] for actor in actors]
                for i in range(len(actor_list)):
                    for j in range(i + 1, len(actor_list)):
                        if not graph.has_especificEdge(actor_list[i], actor_list[j], movie):
                            graph.insert_edge(actor_list[i], actor_list[j], movie)
    except MemoryError:
        print("Memory Error")

    return graph





g = build_graph_from_file("small_dataset_utf8.txt")

print("Arestas = ")
print( g.size())
