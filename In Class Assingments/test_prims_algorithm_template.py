import unittest
from typing import List, Tuple
from example_023_minimum_spanning_tree_Prims_algo import prims_algorithm

class TestPrimsAlgorithm(unittest.TestCase):
    
    def setUp(self):
        self.graph1 = {
            'A': [('B', 2), ('C', 3)],
            'B': [('A', 2), ('C', 4), ('D', 1)],
            'C': [('A', 3), ('B', 4), ('D', 2)],
            'D': [('B', 1), ('C', 2)]
        }
        self.expected_output1 = [('A', 'B', 2), ('B', 'D', 1), ('D', 'C', 2)]

        # Create your Test Graphs here.

        # YOUR CODE





    
    def test_prims_algorithm_with_graph1(self):
        # ...

        # YOUR CODE
        # self.assertEqual(   ,   )
        pass
        
    def test_prims_algorithm_with_graph2(self):
        # ...

        # YOUR CODE
        # self.assertEqual(   ,   )
        pass

    def test_prims_algorithm_with_graph3(self):
        # ...

        # YOUR CODE
        # self.assertEqual(   ,   )
        pass

if __name__ == '__main__':
    unittest.main()
