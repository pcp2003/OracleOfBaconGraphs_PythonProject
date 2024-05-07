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

    def __init__(self, u, v, label):
        self._vertex1 = u
        self._vertex2 = v
        self._label = label

    def __hash__(self):
        # Função que mapeia a aresta a uma posição no dicionário (hash map)
        return hash( (self._vertex1, self._vertex2) )

    def __str__(self):
        return f'({self._vertex1},{self._vertex2},{self._label})'


    def __eq__(self, other):
        # define igualdade de duas arestas (deve ser consistente com a função hash)
        return self._vertex1 == other._vertex1 and self._vertex2 == other._vertex2 and self._label == other._label

    def endpoints(self):
        '''Devolve a tupla (u,v) que indica os vértices antecessor e sucessor.'''
        return (self._vertex1, self._vertex2)

    def show_edge(self):
        print('(',self._vertex1, ', ', self._vertex2, ') label', self._label)

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
        self._edges = set()   # Set to store unique edge identifiers for quick lookup
        self._n = 0                 # número de vértices do grafo
        self._m = 0                 # número de arestas do grafo
        self._directed = directed

    def _incident_edges(self, v):
        '''Gerador: devolve todas as arestas de um vértice v.'''
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

    def has_especificEdge(self, u, v, label):
        return (u.vertice(), v.vertice(), label) in self._edges

    def has_AnyEdge(self, u, v):
        if not self.has_node(u) or not self.has_node(v):
            return False
        else:
            return Vertex(v) in self._vertices[u].keys()


    def insert_vertex(self, x):
        '''Insere e devolve um novo vértice com o elemento x'''
        v = Vertex(x)
        self._vertices[v] = {}      # inicializa o dicionário de adjacências deste vértice a vazio
        self._n +=1                 # mais um vértice no grafo
        return v

    def insert_edge(self, u, v, label):

        edge_key = (u.vertice(), v.vertice(), label)  # Cria identificador único

        if edge_key not in self._edges:

            self._edges.add(edge_key)  # Adiciona ao set para um check-up rápido

            # Adiciona ao dicionário
            edge = Edge(u, v, label)

            self._vertices[u][v] = edge

            if not self._directed:
                self._vertices[v][u] = edge

            self._m += 1



    def degree(self, v, outgoing=True):
        
        '''Quantidade de arestas originárias ou incidentes no vértice v
           Se for um grafo dirigido, conta as arestas outgoing ou incoming,
           de acordo com o valor de outgoing (True or False)
        '''
        adj = self._vertices
        if not self._directed:
            count = len(adj[v])
        else:
            count = 0
            for edge in adj[v].values():
                x, y = edge.endpoints()
                if (outgoing and x == v) or (not outgoing and y == v):
                    count += 1
        return count

    def get_edge(self, u, v, label):

        '''Método interno: Devolve a aresta que liga u a v com uma etiqueta específica ou None se não forem adjacentes ou a aresta com tal etiqueta não existir.'''

        if u in self._vertices and v in self._vertices[u]:
            # Guarda numa variavel a lista com os possiveis edges entre um par de vértices
            edges = self._vertices[u][v]
            if isinstance(edges, list):
                for edge in edges:
                    if edge.label == label:
                        return edge

            # Se não for uma lista compara a label diretamente
            elif edges._label == label:
                return edges
        return None


    def vertices(self):
        '''Devolve um iterável sobre todos os vértices do Grafo'''
        return self._vertices.keys()

    def edges(self):
        '''Devolve o conjunto (set) de todas as arestas do Grafo'''
        result = set()      # avoid double-reporting edges in undirected graph
        for secondary_map in self._vertices.values():
            result.update(secondary_map.values())  # add edges to resulting set
        return list(result)

    def remove_vertex(self, v):
        '''remove o vértice v. Se o vertice não existir, não faz nada.'''
        # remover todas as arestas de [v]
        # remover todas as arestas com v noutros vertices
        # remover o vértice v
        if v in self._vertices.keys():
            lst = [i for i in self.incident_edges(v)]
            for i in lst:
                x, y = i.endpoints()
                self.remove_edge(x,y)
            del self._vertices[v]
            self._n -=1

    def remove_edge(self, u, v, label):
        edge_key = (u.vertice(), v.vertice(), label)
        if edge_key in self._edges:
            self._edges.remove(edge_key)
            # Additional logic to update adjacency structures
            del self._vertices[u][v]
            if not self._directed:
                del self._vertices[v][u]
            self._m -= 1  # Decrement edge count


    def has_neighbors(self, v):
        if self.incident_edges(v) != None:
            return True
        else:
            return False

    def incident_edges(self, v, incoming=True):
        '''Gerador: indica todas as arestas incoming de v
           Se for um grafo dirigido e incoming for False, devolve as arestas outgoing
        '''
        for edge in self._vertices[v].values(): # para todas as arestas relativas a v:
            if not self._directed:
                yield edge
            else:  # senão deve ir procurar em todas as arestas para saber quais entram ou saiem
                x, y = edge.endpoints()
                if (incoming and y == v) or (not incoming and x == v):
                    yield edge

    def get_OutNeighbors(self, v):
        neighbors_list = []
        for edge in self.incident_edges(v):
            if edge._ant not in neighbors_list and edge._ant != v:
                neighbors_list.append(edge._ant)
            elif edge._suc not in neighbors_list and edge._suc != v:
                neighbors_list.append(edge._suc)

        #sort by number of the vertix
        return sorted(neighbors_list, key=lambda x: (x._elemento))

    def is_successor(self, v, x):
        for edge in self.incident_edges(v):
            if edge.get_ant() == x:
                return True
        return False

    def is_predecessor(self, u, v):
        for edge in self.incident_edges(u):
            if edge.get_ant() == v:
                return True
        return False


    def printG(self):
        '''Mostra o grafo por linhas'''
        if self._n == 0:
            print('O grafo está vazio!')
        else:
            print('Grafo orientado:', self._directed)
            for v in self.vertices():
                print('\nvertex ', v, ' grau_in: ', self.degree(v,False), end=' ')# mostra o grau (de saída se orientado)
                for i in self.incident_edges(v):
                    print(' ', i, end=' ')
                if self._directed:          # se orientado, mostrar o grau de saida
                    print('\n \t   grau_out: ', self.degree(v, True), end=' ')
                    for i in self.incident_edges(v, False):    # e mostrar os arcos de saída
                        print(' ', i, end=' ')

