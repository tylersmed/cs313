import unittest
from example_022_minimum_spanning_tree_Kruskal_algo import Graph


class TestKruskalAlgorithm(unittest.TestCase):

    def setUp(self):
        # A test graph
        self.graph1 = Graph(8)
        self.graph1.add_edge(0, 1, 2)
        self.graph1.add_edge(0, 2, 5)
        self.graph1.add_edge(1, 3, 6)
        self.graph1.add_edge(1, 5, 2)
        self.graph1.add_edge(2, 6, 1)
        self.graph1.add_edge(3, 5, 4)
        self.graph1.add_edge(4, 6, 1)
        self.graph1.add_edge(5, 6, 6)
        self.graph1.add_edge(6, 7, 3)

        # a disconnected test graph
        self.discnctd_graph = Graph(6)
        self.discnctd_graph.add_edge(0, 2, 5)
        self.discnctd_graph.add_edge(0, 3, 5)
        self.discnctd_graph.add_edge(0, 4, 5)
        self.discnctd_graph.add_edge(3, 5, 9)

        # an empty test graph
        self.empty_graph = Graph(0)

        # a test graph with one vertex
        self.single_vert_graph = Graph(1)

    def test_kruskal_mst(self):
        # Compute the minimum spanning tree using Kruskal's algorithm
        weight, mst = self.graph1.kruskal_algo()
        print(weight, mst)

        # Assert that the total weight of the MST is correct
        self.assertEqual(weight ,18 )

        # Assert that the MST contains the correct edges
        exp_mst = [[2, 6, 1], [4, 6, 1], [0, 1, 2], [1, 5, 2], [6, 7, 3], [3, 5, 4], [0, 2, 5]]

        self.assertEqual(mst, exp_mst)

    def test_kruskal_mst_empty_graph(self):
        # Test with an empty graph
        weight, mst = self.empty_graph.kruskal_algo()
        print(weight, mst)

        exp_mst = []
        
        self.assertEqual(mst, exp_mst)
        pass

    def test_kruskal_mst_single_vertex(self):
        # Test with a graph with a single vertex
        weight, mst = self.single_vert_graph.kruskal_algo()
        print(weight, mst)

        exp_mst = []
        self.assertEqual(mst, exp_mst)

    def test_kruskal_mst_disconnected_graph(self):
        # Test with a disconnected graph
        weight, mst = self.discnctd_graph.kruskal_algo()
        print(weight, mst)


        exp_mst = [[0, 2, 5], [0, 3, 5], [0, 4, 5], [3, 5, 9]]
        self.assertEqual(mst, exp_mst)

if __name__ == '__main__':
    unittest.main()
