import unittest
from typing import List, Tuple
from example_023_minimum_spanning_tree_Prims_algo import Graph

class TestPrimsAlgorithm(unittest.TestCase):
    
    def setUp(self):

        # a test graph
        self.graph1 = Graph()
        self.graph1.add_verticies(range(8))
        self.graph1.add_undirected_edge(0, 1, 2)
        self.graph1.add_undirected_edge(0, 2, 5)
        self.graph1.add_undirected_edge(1, 3, 6)
        self.graph1.add_undirected_edge(1, 5, 2)
        self.graph1.add_undirected_edge(2, 6, 1)
        self.graph1.add_undirected_edge(3, 5, 4)
        self.graph1.add_undirected_edge(4, 6, 1)
        self.graph1.add_undirected_edge(5, 6, 6)
        self.graph1.add_undirected_edge(6, 7, 3)

        # a test graph with a disconnected vertex
        self.discnctd_graph = Graph()
        self.discnctd_graph.add_verticies(range(6))
        self.discnctd_graph.add_undirected_edge(0, 2, 5)
        self.discnctd_graph.add_undirected_edge(0, 3, 5)
        self.discnctd_graph.add_undirected_edge(0, 4, 5)
        self.discnctd_graph.add_undirected_edge(3, 5, 9)

        # a test graph with one vertex
        self.single_vert_graph = Graph()
        self.single_vert_graph.add_verticies(range(1))


    
    def test_prims_algorithm_with_graph1(self):
        
        mst, weight = self.graph1.prims()

        # test total weight is correct
        exp_weight = 18
        self.assertEqual(weight, exp_weight)

        # test mst is correct
        exp_mst = [[0, 1, 2], [1, 5, 2], [5, 3, 4], [0, 2, 5], [2, 6, 1], [6, 4, 1], [6, 7, 3]]
        self.assertEqual(mst, exp_mst)
    
    def test_prims_algorithm_with_graph2(self):
        # testing prims with a graph that has a disconected vertex
        mst, weight = self.discnctd_graph.prims()

        # test total weight is correct
        exp_weight = 24
        self.assertEqual(weight, exp_weight)

        # test mst is correct
        exp_mst = [[0, 2, 5], [0, 3, 5], [0, 4, 5], [3, 5, 9]]
        self.assertEqual(mst, exp_mst)

    def test_prims_algorithm_with_graph3(self):
        # test a graph with only one vertex
        mst, weight = self.single_vert_graph.prims()

        # test total weight
        exp_weight = 0
        self.assertEqual(weight, exp_weight)

        # test mst is correct
        exp_mst = []
        self.assertEqual(mst, exp_mst)

if __name__ == '__main__':
    unittest.main()
