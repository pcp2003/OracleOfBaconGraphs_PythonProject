from Graph import Graph, Vertex


class HollywoodOracle:

    def __init__(self, filename):

        self.build_graph_from_file(filename)


    def build_graph_from_file(filename):
        """
        Constrói um grafo a partir de um arquivo de texto com dados de filmes e atores.

        Parâmetros:
        filename (str): O caminho para o arquivo .txt contendo os dados.

        Retorna:
        Graph: O objeto grafo construído com atores como vértices e filmes como arestas.
        """
        graph = Graph()
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split('/')
                if len(parts) < 2:
                    continue  # Ignora linhas sem atores suficientes ou mal formatadas
                movie = parts[0].strip()
                actors = [part.strip() for part in parts[1:]]

                # Adiciona cada ator ao grafo como um vértice (se ainda não estiver presente)
                for actor in actors:
                    if not graph.has_node(Vertex(actor)):
                        graph.insert_vertex(actor)

                # Adiciona uma aresta entre cada par de atores para este filme
                for i in range(len(actors)):
                    for j in range(i + 1, len(actors)):
                        actor1 = Vertex(actors[i])
                        actor2 = Vertex(actors[j])
                        # Verifica se já existe uma aresta para esse filme entre os dois atores
                        if not graph.has_especificEdge(actor1, actor2, movie):
                            graph.insert_edge(actor1, actor2, movie)

        return graph
