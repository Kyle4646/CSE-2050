class Graph_ES:

    def __init__(self, V = set(), E = set()):
        self.V = V
        self.E = E

    def __len__(self):
        return(len(self.V))

    def __iter__(self):
        for i in self.V:
            yield i

    def add_vertex(self, v):
        self.V.add(v)

    def remove_vertex(self, v):
        if v in self.V:
            self.V.remove(v)
            return
        raise KeyError
    
    def add_edge(self, e):
        self.E.add(e)

    def remove_edge(self, e):
        if e in self.E:
            self.E.remove(e)
            return
        raise KeyError
    
    def _neighbors(self, v):
        for i, j in self.E:
            if i == v:
                yield j

class Graph_AS:

    def __init__(self, V = set(), E = set()):
        self._neighbors_d = {}
        for v in V:
            self.add_vertex(v)
        for e in E:
            self.add_edge(e)

    def add_vertex(self, v):
        self._neighbors_d[v] = set()

    def add_edge(self, e):
        self._neighbors_d[e[0]].add(e[1])

    def __len__(self):
        return(len(self._neighbors_d))
    
    def __iter__(self):
        for key in self._neighbors_d.keys():
            yield key

    def remove_vertex(self, v):
        del self._neighbors_d[v]

    def remove_edge(self, e):
        self._neighbors_d[e[0]].remove(e[1])

    def _neighbors(self, v):
        for edge in self._neighbors_d[v]:
            yield edge