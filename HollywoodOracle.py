from collections import deque

from Graph import Graph

ACTOR = 0
FILM = 1


class HollywoodOracle:

    def __init__(self, filename):

        self._graph = FileManager.build_graph_from_file(filename)
        self._bfs_result = SearchAlgorithim.bfs(self._graph, self._graph.get_vertex("Fitz-Gerald, Lewis"))

    @property
    def bfs_result(self):
        return self._bfs_result

    def all_movies(self):

        movies = set()
        for vertex in self._graph.vertices:
            if vertex.vertex_type == FILM:
                movies.add(vertex)
        return movies

    def all_actors(self):

        actors = set()
        for vertex in self._graph.vertices:
            if vertex.vertex_type == ACTOR:
                actors.add(vertex)
        return actors

    def movies_from(self, actor_name):

        actor = self._graph.get_vertex(actor_name)
        return self._graph.get_neighbors(actor)

    def cast_of(self, movie_name):

        movie = self._graph.get_vertex(movie_name)
        return self._graph.get_neighbors(movie)

    def set_center_of_universe(self, actor_name):

        actor = self._graph.get_vertex(actor_name)
        self._bfs_result = SearchAlgorithim.bfs(self._graph, actor)

    def number_of_x(self, actor_name):

        actor = self._graph.get_vertex(actor_name)

        if actor in self._bfs_result:
            return self._bfs_result[actor][0]  # Retorna a distancia do centro do universo.
        else:
            return None  # Não há caminho se o ator não está conectado

    # Após executar o BFS, você pode extrair o caminho para qualquer ator
    def path_to_x(self, actor_name):

        actor = self._graph.get_vertex(actor_name)

        if actor in self._bfs_result:
            return self._bfs_result[actor][1]  # Retorna o caminho incluindo filmes
        else:
            return None  # Não há caminho se o ator não está conectado

    def max_number_of_x(self):

        chave, valor = next(reversed(self._bfs_result.items()))
        return valor[0]

    def count_number_of_x(self, number):
        count = 0
        for chave, valor in self._bfs_result.items():
            if valor[0] == number:
                count = count + 1
        return count

    def avarage_number_of_x(self):
        avarage = 0
        count = 0
        for chave, valor in self._bfs_result.items():
            avarage = avarage + valor[0]
            count = count + 1
        return avarage/count




# classe estática responsável por administrar o conteúdo dos DataSets

class FileManager:
        @staticmethod
        def build_graph_from_file(filename):
            graph = Graph(directed=True)  # Assumindo que o grafo é direcionado se necessário
            try:
                with open(filename, 'r', encoding='utf-8') as file:
                    for line in file:
                        parts = line.strip().split('/')
                        if len(parts) < 2:
                            continue  # Pula linhas sem dados suficientes

                        movie_title = parts[0].strip()
                        actors = [part.strip() for part in parts[1:]]

                        # Insere ou obtém o vértice do filme
                        movie_vertex = graph.insert_vertex(movie_title, FILM)

                        # Processa cada ator listado para o filme
                        for actor in actors:

                            actor_vertex = graph.insert_vertex(actor, ACTOR)
                            graph.insert_edge(actor_vertex, movie_vertex), graph.insert_edge(movie_vertex, actor_vertex)

            except MemoryError:
                print("Memory Error")
            return graph


class SearchAlgorithim:

    # Define por omissão "Bacon, Kevin", como centro do universo!

    @staticmethod
    def bfs(graph, start_vertex=None):

        # Se nenhum vértice inicial é fornecido, usa-se um padrão

        if start_vertex is None:
            start_vertex = graph.get_vertex("Kevin, Bacon")

        queue = deque([start_vertex])
        visited = {start_vertex: (0, [start_vertex])}  # (distância, caminho até aqui)

        while queue:

            current_vertex = queue.popleft()
            current_distance, path_to_here = visited[current_vertex]

            for neighbor in graph.get_neighbors(current_vertex):

                if neighbor not in visited:

                    if neighbor.vertex_type == FILM:
                        new_distance = current_distance
                    else:
                        new_distance = current_distance + 1

                    visited[neighbor] = (new_distance, path_to_here + [neighbor])
                    queue.append(neighbor)

        return visited


