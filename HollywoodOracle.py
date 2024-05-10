import profile
from collections import deque

from Graph import Graph, Vertex

# Tenta importar o decorador profile do memory_profiler, se não estiver disponível, define um que não faz nada
try:
    from memory_profiler import profile
except ImportError:
    def profile(func):
        return func


class HollywoodOracle:


    def __init__(self, filename):

        self._graph = FileManager.build_graph_from_file(filename)
        # self._bfs_result = SearchAlgorithim.bfs(self._graph, Vertex("Fitz-Gerald, Lewis"))

    def all_movies(self):
        return self._graph._labels

    def all_actors(self):
        return self._graph._vertices

    def movies_from(self, actor):
        edges = self._graph._incident_edges(actor)
        if edges is None:
            return None
        return self._graph.get_unique_labels(edges)

    def cast_of(self, movie):

        edgesWithMovie = filter(lambda tupla: tupla[2] == movie, self._graph._edges)

        cast_of = set()

        for edge in edgesWithMovie:
            cast_of.add(edge[0])
            cast_of.add(edge[1])

        return cast_of

    def set_center_of_universe(self, actor):
        self._bfs_result = SearchAlgorithim.bfs(self._graph, actor)

    def number_of_X(self, Actor):
        if Actor in self._bfs_result:
            return self._bfs_result[Actor][0]  # Retorna o caminho incluindo filmes
        else:
            return None  # Não há caminho se o ator não está conectado


    # Após executar o BFS, você pode extrair o caminho para qualquer ator
    def path_to_X(self, actor):
        if actor in self._bfs_result:
            return self._bfs_result[actor][1]  # Retorna o caminho incluindo filmes
        else:
            return None  # Não há caminho se o ator não está conectado

# classe estática responsável por administrar o conteúdo dos DataSets

class FileManager:


    @staticmethod
    @profile
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
            start_vertex = Vertex("Bacon, Kevin")

        queue = deque([start_vertex])
        visited = {start_vertex: (0, [(start_vertex, None)])}  # Inicia com distância 0 e caminho apenas com o ator inicial

        while queue:

            current_vertex = queue.popleft()
            current_distance, path_to_here = visited[current_vertex]

            for neighbor in graph.get_neighbors(current_vertex):
                if neighbor not in visited:
                    visited[neighbor] = (current_distance + 1, path_to_here + [neighbor])
                    queue.append(neighbor)

        return visited

