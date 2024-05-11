# Class Vertice
class Vertex:
    def __init__(self, x, vertex_type):
        self._elemento = x
        self._vertex_type = vertex_type
        self._hash = hash((self._elemento, self._vertex_type))  # Pré-calcule o hash

    def __hash__(self):
        return self._hash

    def __eq__(self, other):
        return isinstance(other, Vertex) and self._elemento == other._elemento

    def __str__(self):
        return f'{self._elemento}'

    @property
    def elemento(self):
        return self._elemento

    @property
    def vertex_type(self):
        return self._vertex_type


class Edge:
    def __init__(self, u, v):
        self._vertex1 = u
        self._vertex2 = v
        self._hash = hash((u, v))

    def __hash__(self):
        return self._hash

    def __eq__(self, other):
        return isinstance(other, Edge) and self._vertex1 == other._vertex1 and self._vertex2 == other._vertex2

    def __str__(self):
        return f'({self._vertex1}, {self._vertex2})'

    @property
    def endpoints(self):
        return (self._vertex1, self._vertex2)

    def show_edge(self):
        print('(',self._vertex1, ', ', self._vertex2)

    # métodos novas
    def get_ant(self):
        return self._vertex1

    def get_suc(self):
        return self._vertex2

    def opposite(self, v):
        '''Indica o vértice oposto ao v neste arco; v tem de ser um dos vértices.'''
        return self._vertex2 if v is self._vertex1 else self._vertex1



class Graph:
    '''
    Representação de um grafo usando dicionários encadeados (nested dictionaries).

    Atributos:
    ----------
    vertices: Dicionário exterior que associa um vértice (Vertex) a um mapa de adjacências (dicionario)
    n: Número de vértices no Grafo
    m: Número de arestas no Grafo
    ----------
'''

    def __init__(self, directed=False):
        self._vertices = {}
        self._directed = directed
        self._vertex_map = {}       # Chave: nome do elemento, Valor: objeto Vertex


    def _incident_edges(self, v):

        '''Gerador: devolve todas as listas de arestas de um vértice v.'''
        for edge in self._vertices[v].values(): # para todas as arestas incidentes em v:
            yield edge

    def is_directed(self):
        '''com base na criação original da instância, devolve True se o Grafo é dirigido; False senão '''
        return self._directed  # True se os dois contentores são distintos

    @property
    def order(self):
        return len(self._vertices)

    @property
    def size(self):
        return sum(len(adj) for adj in self._vertices.values())

    def has_node(self, v):
        return v in self._vertices

    def has_edge(self, u, v):
        return v in self._vertices.get(u, {})

    def get_vertex(self, vertex_name):
        # Busca direta pelo nome do vértice
        return self._vertex_map.get(vertex_name)

    def insert_vertex(self, element, vertex_type):

        if element not in self._vertex_map:

            vertex = Vertex(element, vertex_type)
            self._vertices[vertex] = {}
            self._vertex_map[element] = vertex
            return vertex
        return self._vertex_map[element]

    def insert_edge(self, u, v):
        if v not in self._vertices[u]:
            edge = Edge(u, v)
            self._vertices[u][v] = edge
            if not self._directed:
                self._vertices[v][u] = edge

    def degree(self, v):
        '''Quantidade de arestas originárias ou incidentes no vértice v'''
        return len(self._vertices[v])

    def get_edge(self, u, v):

        if u in self._vertices and v in self._vertices[u]:
            # Guarda numa variavel a lista com os possiveis edges entre um par de vértices
            return self._vertices[u][v]

        return None

    @property
    def vertices(self):
        '''Devolve um iterável sobre todos os vértices do Grafo'''
        return self._vertices

    def edges(self):
        '''Devolve o conjunto (set) de todas as (Representações) das arestas do Grafo'''
        yield self._vertices.values()

    def remove_vertex(self, v):
        if v in self._vertices:
            for adj in list(self._vertices[v]):
                self.remove_edge(v, adj)  # Aproveita o remove_edge para remover cada aresta conectada
            del self._vertices[v]  # Agora remove o próprio vértice

    def remove_edge(self, u, v):
        """Remove a aresta entre u e v, se existir."""
        self._vertices.get(u, {}).pop(v, None)
        if not self._directed:
            self._vertices.get(v, {}).pop(u, None)

    def has_neighbors(self, v):

        if self._incident_edges(v) is not None:
            return True
        else:
            return False

    def get_neighbors(self, v):
        return self._vertices.get(v, {})

    def print_graph(self):
        print('Grafo orientado:', self._directed)
        for v in self.vertices:
            print('\nvertex ', v, ' grau_in: ', self.degree(v), end=' ')
            for i in self._incident_edges(v):
                print(' ', i, end=' ')

