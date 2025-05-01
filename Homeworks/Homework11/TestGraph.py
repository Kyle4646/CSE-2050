
import unittest
from Graph import Graph
from Graph import AdjacencySetGraph
from Graph import EdgeSetGraph

class GraphTestFactory:

    def setUp(self, graph):
        '''Sets up what type of graph we use'''

        self.graph = graph

    def test_is_connected_simple(self):
        '''Sees if vertex in graph is connected to all others it should be'''

        V = {'M', 'O', 'D', 'R', 'I', 'C'}
        E = {('M', 'C'), ('D', 'R'), ('M', 'D'), ('R', 'M')} 

        graph = self.graph(V, E)
        self.assertTrue(graph.is_connected('M', 'C'))
        self.assertTrue(graph.is_connected('R', 'D')) #checks other way too
        self.assertFalse(graph.is_connected('R', 'I'))

        self.assertTrue(graph.is_connected('R', 'C')) #R should be connected to C since R > M > C

    def test_is_connected_cycle(self):
        '''Sees is a cycle does not give infinite loops'''

        V = {'A', 'B', 'C'}
        E = {('A', 'B'), ('B', 'C'), ('C', 'A')} #all connected
        graph = self.graph(V, E)

        self.assertTrue(graph.is_connected('A', 'B'))
        self.assertTrue(graph.is_connected('B', 'C'))
        self.assertTrue(graph.is_connected('A', 'C')) #if works no stuck in infinite loop

    def test_bfs(self):
        '''Sees if bfs works accordining to plan'''

        V = {1, 2, 3, 4, 5, 6}
        E ={(1, 2),(1, 3),(2, 4),(3, 5),(5, 6)}
        graph = self.graph(V, E)

        dict_of_correctness = {1:None, 2: 1, 3:1, 5:3, 6:5, 4:2} 
        tree = graph.bfs(1)
        
        for vertex in tree:
            self.assertEquals(tree[vertex], dict_of_correctness[vertex]) #Sees if all values in BFS in right

    def test_count_trees(self):
        '''Sees if number of trees is correct'''

        V = {1, 2, 3, 4, 5, 6, 7, 97,  8}
        E = {(1, 2), (3, 4), (3, 5), (4, 5), (6, 97), (7, 8), (6, 7), (97, 8)} #3 islands 
        graph = self.graph(V, E)

        dict_of_trees = [{1:None, 2:1}, {3:None, 4:3, 5:3}, {6:None, 7:6, 8:97, 97:6}]
        list_of_trees, num = graph.count_trees()
        self.assertEqual(num, 3)

        for tree in list_of_trees:
            self.assertIn(tree, dict_of_trees)

    def test_shortest_path(self):
        '''Sees if shortest path for two vertices works'''

        V = {1, 2, 3, 4, 5, 6, 7}
        E = {(1, 2), (2, 3), (3, 5), (5, 6), (6, 7), (4, 7), (2, 4)} #Fastest path to 7 from 1 is 1 > 2 > 4> 7
        #slow is 1 > 2 > 3 > 5 > 6 > 7
        graph = self.graph(V, E)

        correct_path = [1, 2, 4, 7]
        path = graph.shortest_path(1, 7)
        self.assertEqual(correct_path, path)
        self.assertEqual(len(path), 4)
                

class TestAdjacency(GraphTestFactory, unittest.TestCase):

    def setUp(self):
        '''Sets up Adjacency graph for testing'''

        super().setUp(AdjacencySetGraph)


class TestEdge(GraphTestFactory, unittest.TestCase): 

    def setUp(self):
        '''Sets up Adjacency graph for testing'''

        super().setUp(EdgeSetGraph)


class NonFactoryTests(unittest.TestCase):

    def test_init_Graph(self):
        '''Sees if calling just a graph calls an error'''

        with self.assertRaises(NotImplementedError): Graph.__init__(self)


if __name__ == '__main__':
    unittest.main()