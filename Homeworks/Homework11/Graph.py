
from LazyQueue import LazyQueue

class Graph:
    
    def __init__(self):
        '''Initialzes Graph Class'''

        raise NotImplementedError('Use EdgeSet or Adjancey Graph')
    
    def is_connected(self, v1, v2):
        '''Uses helper to see if two vertices connected'''

        return self._is_connected(v1, v2, set())
    
    def _is_connected(self, v1, v2, visited):
        '''Function to see recursivley if neighbors lead to graph'''

        if v1 in visited:
            return False #returns false if already checked
        if v1 == v2:
            return True #if neighbor is second vector, then yes there is path
        visited.add(v1)
        for n in self.nbrs(v1):
            if self._is_connected(n, v2, visited) == True:
                return True
        return False
    
    def bfs(self, v):
        '''Conducts a breadth first search'''

        tree = {}
        to_visit = LazyQueue()
        to_visit.enqueue((None, v))
        while not to_visit.isEmpty():
            prev, curr = to_visit.dequeue()
            if curr not in tree:
                tree[curr] = prev
                for n in self.nbrs(curr):
                    to_visit.enqueue((curr, n))
        return tree
    
    def shortest_path(self, v1, v2):
        '''Finds shortest path between two vertices'''

        tree = self.bfs(v1) #BFS finds shortest path to all vertices
        if v2 not in tree:
            return None
        path = []
        v1 = v2
        while v1 is not None:
            path.append(v1)
            v1 = tree[v1] #keeps taking link until v2 reached using BFS path (shortest path)
        path.reverse()
        return path
    
    def count_trees(self):
        '''Counts the number of different trees on a graph'''

        visisted = set()
        counter = 0
        list_of_trees = []

        for v in self:
            if v not in visisted:
                tree = self.bfs(v)
                list_of_trees.append(tree)
                for v in tree.keys():
                    visisted.add(v) #adds all vertices in a tree
                counter += 1
        return list_of_trees, counter

class EdgeSetGraph(Graph):
    
    def __init__(self, V = set(), E = set()):
        '''Initialzes both sets for EdgeSet'''

        self.V = set()
        self.E = set()
        for v in V:
            self.add_vertex(v)
        for e in E:
            self.add_edge(e)

    def __iter__(self):
        '''Iterates over the vertices'''

        for v in self.V:
            yield v

    def add_vertex(self, v):
        '''Adds vertex to vertex set'''

        self.V.add(v)

    def add_edge(self, e):
        '''Adds edge to edge set adds reverse since unweighted'''

        if e[0] in self.V and e[1] in self.V:
            self.E.add(e)
            self.E.add((e[1], e[0])) 
        else:
            raise KeyError('Vertex not in graph')
    
    def nbrs(self, v):
        '''Iterates through every neighbor of v by checking every edge to see whats connected'''

        for v1, v2 in self.E:
            if v1 == v:
                yield v2


class AdjacencySetGraph(Graph):
    
    def __init__(self, V = set(), E = set()):
        '''Initalizes V and E and adds them to neighbor dictionary'''

        self.nbrs_dict = {}
        for v in V:
            self.add_vertex(v)
        for e in E:
            self.add_edge(e)

    def __iter__(self):
        '''Iterates through all vertices in the graph'''

        for v in self.nbrs_dict.keys():
            yield v

    def add_vertex(self, v):
        '''Adds vertex to dictionary'''

        if v not in self.nbrs_dict:
            self.nbrs_dict[v] = set()

    def add_edge(self, e):
        '''Adds edge to graph both ways'''

        if e[0] in self.nbrs_dict.keys() and e[1] in self.nbrs_dict.keys():
            self.nbrs_dict[e[0]].add(e[1])
            self.nbrs_dict[e[1]].add(e[0])
        else:
            raise KeyError('Vertex not in graph')
        
    def nbrs(self, v):
        '''Iterates through all neighbors in graph quickly by only looking at edges connected to vertice'''

        for edge in self.nbrs_dict[v]:
            yield edge 
