

try:
    from memory_profiler import profile
except ImportError:
    def profile(func):
        return func



# Class Vertice
class Vertex:
    ''' Estrutura de Vértice para um grafo: encapsula um elemento que é o identificador deste nó.
        O elemento deve ser hashable:
        - Um objeto hashable é aquele que pode ser utilizado como uma chave num dicionário Python.
        - Isto inclui strings, números, tuplas, etc.
    '''

    def __init__(self, x):
        '''O vértice será inserido no Grafo usando o método insert_vertex(x) que cria um Vertex'''
        self._elemento = x

    def __hash__(self):
        ''' o valor do elemento é usado como hash para o vértice (o elemento deve ser hashable)'''
        return hash(self._elemento)  # devolve o hash do elemento

    def __str__(self):
        '''Devolve a representação do objeto vértice em string.'''
        return'{0}'.format(self._elemento)

    def __eq__(self, x):
        return x == self._elemento # Deve-se garantir que: se hash(x)==hash(elemento), entao x==elemento

    def vertice(self):
        '''Devolve o elemento guardado neste vértice'''
        return self._elemento


# #### Class Edge
class Edge:
    '''Estrutura de Aresta para um Grafo: (origem, destino) e peso '''

    def __init__(self, u, v):
        self._vertex1 = u
        self._vertex2 = v

    def __hash__(self):
        # Função que mapeia a aresta a uma posição no dicionário (hash map)
        return hash( (self._vertex1, self._vertex2) )

    def __str__(self):
        return f'({self._vertex1},{self._vertex2})'


    def __eq__(self, other):
        # define igualdade de duas arestas (deve ser consistente com a função hash)
        return self._vertex1 == other._vertex1 and self._vertex2 == other._vertex2

    def endpoints(self):
        '''Devolve a tupla (u,v) que indica os vértices antecessor e sucessor.'''
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
        '''Construtor: Cria um grafo vazio (dicionário de _vertices).'''
        self._vertices = {}         # dicionário com chave vértice e valor mapa de adjacência
        self._n = 0                 # número de vértices do grafo
        self._m = 0                 # número de arestas do grafo
        self._directed = directed

    def _incident_edges(self, v):

        '''Gerador: devolve todas as listas de arestas de um vértice v.'''
        for edge in self._vertices[v].values(): # para todas as arestas incidentes em v:
            yield edge

    def __str__(self):
        if self._n == 0:
            return "DAA-Graph: <empty>\n"
        else:
            ret = "DAA-Graph:\n"
            ret += "directed: " + str(self._directed) + "\n"
            for v in self._vertices:
                ret += f"vertex {v}: "
                # Collecting edges for each vertex
                connections = []
                # Since each vertex's adjacency list is now directly a dictionary to edges or labels
                for adj_vertex, edge in self._vertices[v].items():
                    if isinstance(edge, list):  # Handle multiple edges between the same vertices
                        for e in edge:
                            connections.append(str(e))
                    else:
                        connections.append(str(edge))
                ret += "; ".join(connections) + "\n"
            return ret


    def is_directed(self):
        '''com base na criação original da instância, devolve True se o Grafo é dirigido; False senão '''
        return self._directed  # True se os dois contentores são distintos

    def order(self):
        '''Ordem de um grafo: a quantidade de vértices no Grafo'''
        return self._n

    def size(self):
        '''Dimensão de um grafo: a quantidade total de arestas do Grafo'''
        return self._m

    def has_node(self, v):
        """Verifica se o vértice v está no grafo."""
        return v in self._vertices


    def has_edge(self, u, v):
        if not self.has_node(u) or not self.has_node(v):
            return False
        else:
            return v in self._vertices[u].keys()

    def insert_vertex(self, x):
        '''Insere e devolve um novo vértice com o elemento x'''
        v = Vertex(x)
        self._vertices[v] = {}      # inicializa o dicionário de adjacências deste vértice a vazio
        self._n += 1                 # mais um vértice no grafo

    def insert_edge(self, u, v):

        if not self.has_node(u):
            self.insert_vertex(u)
        if not self.has_node(v):
            self.insert_vertex(v)
        if not self.has_edge(u, v):

            e = Edge(u, v)            # ''' Cria e insere uma nova aresta entre u e v com id (u,v) . '''
            self._m += 1              # atualiza m apenas se a aresta ainda não existir no grafo
            self._vertices[u][v] = e  # coloca v nas adjacências de u
            self._vertices[v][u] = e  # e u nas adjacências de v (para facilitar a procura de todas as arestas incidentes num vértice)

    def degree(self, v):

        '''Quantidade de arestas originárias ou incidentes no vértice v'''
        return len(self._vertices[v])

    def get_edge(self, u, v):

        if u in self._vertices and v in self._vertices[u]:
            # Guarda numa variavel a lista com os possiveis edges entre um par de vértices
            return self._vertices[u][v]

        return None


    def vertices(self):
        '''Devolve um iterável sobre todos os vértices do Grafo'''
        yield self._vertices.keys()

    def edges(self):
        '''Devolve o conjunto (set) de todas as (Representações) das arestas do Grafo'''
        yield self._edges

    def remove_vertex(self, v):
        '''remove o vértice v. Se o vertice não existir, não faz nada.'''
        # remover todas as arestas de [v]
        # remover todas as arestas com v noutros vertices
        # remover o vértice v

        if v in self._vertices.keys():
            lst = [i for i in self._incident_edges(v)]
            for i in lst:
                x, y = i.endpoints()
                self.remove_edges_list(x,y)
            del self._vertices[v]
            self._n -= 1

    def remove_edges_list(self, u, v):

        if self._vertices[u][v] is not None:

            #Removendo do dicionário
            del self._vertices[u][v]
            del self._vertices[v][u]

            #Removendo do set de pesquisa
            for edge in self._edges:
                if edge[0] == u.vertice() and edge[1] == v.vertice() or edge[0] == v.vertice() and edge[1] == u.vertice():
                    self._edges.discard(edge)


            self._n -= 1


    def has_neighbors(self, v):
        if self._incident_edges(v) != None:
            return True
        else:
            return False

    def get_neighbors(self, v):
        """ Retorna uma lista de vizinhos do vértice 'v'. """
        if v in self._vertices:
            return self._vertices[v].keys()  # Retorna uma lista de vértices vizinhos
        return []  # Retorna uma lista vazia se não há vizinhos ou o vértice não existe



    def printG(self):
        '''Mostra o grafo por linhas'''
        if self._n == 0:
            print('O grafo está vazio!')
        else:
            print('Grafo orientado:', self._directed)
            for v in self.vertices():
                print('\nvertex ', v, ' grau_in: ', self.degree(v,False), end=' ')# mostra o grau (de saída se orientado)
                for i in self._incident_edges(v):
                    print(' ', i, end=' ')

