from collections import deque

from Graph import Graph, Vertex


class HollywoodOracle:


    def __init__(self, filename):

        self._graph = FileManager.build_graph_from_file(filename)
        self._distances = SearchAlgorithim.bfs(self._graph, "Fitz-Gerald, Lewis")

    def all_movies(self):
        return self._graph._labels



# classe estática responsável por administrar o conteúdo dos DataSets
class FileManager:

    @staticmethod
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
                    actors = set(part.strip() for part in parts[1:])

                    for actor in actors:
                        if actor not in vertex_map:
                            vertex_map[actor] = graph.insert_vertex(actor)

                    actor_list = [vertex_map[actor] for actor in actors]
                    for i in range(len(actor_list)):
                        for j in range(i + 1, len(actor_list)):
                            if not graph.has_especificEdge(actor_list[i], actor_list[j], movie):
                                graph.insert_edge(actor_list[i], actor_list[j], movie)
        except MemoryError:
            print("Memory Error")

        return graph


class SearchAlgorithim:

    #Define por omissão "Bacon, Kevin", como centro do universo!
    @staticmethod
    def bfs(graph, start_vertex=None):

        if not start_vertex:
            start_vertex = "Bacon, Kevin"


        visited = set()
        queue = deque([(start_vertex, 0)])
        distances = {}

        while queue:
            current_vertex, current_distance = queue.popleft()

            # Processa o vértice atual se ainda não foi visitado
            if current_vertex not in visited:
                visited.add(current_vertex)
                distances[current_vertex] = current_distance

                # Adiciona todos os visinhos a lista
                for neighbor in graph.get_OutNeighbors(current_vertex):
                    if neighbor not in visited:
                        queue.append((neighbor, current_distance + 1))

        return distances

