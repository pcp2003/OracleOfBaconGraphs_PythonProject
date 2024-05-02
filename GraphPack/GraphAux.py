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
        '''Devolve a representação do objeto aresta em string: (origem, destino)w=peso '''
        return'({0},{1})w={2}'.format(self._vertex1, self._vertex2, self._label)

    def __eq__(self, other):
        # define igualdade de duas arestas (deve ser consistente com a função hash)
        return self._vertex1 == other._vertex1 and self._vertex2 == other._vertex2

    def endpoints(self):
        '''Devolve a tupla (u,v) que indica os vértices antecessor e sucessor.'''
        return (self._vertex1, self._vertex2)

    def cost(self):
        '''Devolve o peso associado a este arco.'''
        return self._label

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
