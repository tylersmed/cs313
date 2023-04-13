import unittest
from example_022_minimum_spanning_tree_Kruskal_algo import Graph, Edge, kruskal_mst


class TestKruskalAlgorithm(unittest.TestCase):

    def setUp(self):
        # Create your Test Graphs here. 
        pass


    def test_kruskal_mst(self):
        # Compute the minimum spanning tree using Kruskal's algorithm
        # mst = kruskal_mst(self.graph)

        # WRITE YOUR CODE

        # Assert that the total weight of the MST is correct
        # self.assertEqual( , )

        # Assert that the MST contains the correct edges
        expected_mst = [Edge(0, 1, 2), Edge(1, 2, 3), Edge(1, 4, 5), Edge(0, 3, 6)]
        self.assertEqual(mst, expected_mst)

    def test_kruskal_mst_empty_graph(self):
        # Test with an empty graph
        

        # ... 

        # YOUR CODE 
        # self.assertEqual(   ,   )
        pass

    def test_kruskal_mst_single_vertex(self):
        # Test with a graph with a single vertex
        # ...

        # YOUR CODE
        # self.assertEqual(   ,   )
        pass



    def test_kruskal_mst_disconnected_graph(self):
        # Test with a disconnected graph
        
        # ...

        # YOUR CODE
        # self.assertEqual(   ,   )
        pass

if __name__ == '__main__':
    unittest.main()
