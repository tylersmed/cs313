#  File: TestBinaryTree.py
#  Description: Creates functions for a binary search tree
#  Student Name: Tyler Smedley
#  Student UT EID: tws933
#  Partner Name:
#  Partner UT EID:
#  Course Name: CS 313E
#  Unique Number: 52020
#  Date Created: 3/14/23
#  Date Last Modified: 3/22/23

import sys

class Node (object):
    # constructor
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None

    def print_node(self, level=0):

        if self.lChild != None:
            self.lChild.print_node(level + 1)
        print(' ' * 3 * level + '->', self.data)
        if self.rChild != None:
            self.rChild.print_node(level + 1)

    def get_height(self):
        if self.lChild != None and self.rChild != None:
            return 1 + max(self.lChild.get_height(), self.rChild.get_height())
        elif self.lChild != None:
            return 1 + self.lChild.get_height()
        elif self.rChild != None:
            return 1 + self.rChild.get_height()
        else:
            return 1

class Tree(object):
    # constructor
    def __init__(self):
        self.root = None

    def print(self, level):
        self.root.print_node(level)

    def get_height(self):
        return self.root.get_height()

    # Inserts data into Binary Search Tree and creates a valid BST
    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            return
        else:
            parent = self.root
            curr = self.root
            # finds location to insert new node
            while curr != None:
                parent = curr
                if data < curr.data:
                    curr = curr.lChild
                else:
                    curr = curr.rChild
            # inserts new node based on comparision to parent node
            if data < parent.data:
                parent.lChild = new_node
            else:
                parent.rChild = new_node
            return

    def bst_to_list(self, current):
        if current == None:
            return []
        return [current.data] + self.bst_to_list(current.lChild) + self.bst_to_list(current.rChild)
        
    # Returns the range of values stored in a binary search tree of integers.
    # The range of values equals the maximum value in the binary search tree minus the minimum value.
    # If there is one value in the tree the range is 0. If the tree is empty the range is undefined.
    def range(self):
        bst_list = self.bst_to_list(self.root)
        return max(bst_list) - min(bst_list)
    
    # Given a node, returns its level within the tree
    def find_node_level(self, current, aNode):
        level = 0
        while current.data != aNode.data:
            if aNode.data > current.data:
                current = current.rChild
            else:
                current = current.lChild
            level += 1
        return level
    
    # This is a helper function that is used to recursively iterate
    # through the tree and returns all nodes that are at the desired level
    def get_level_helper(self, level, current):
        if current == None:
            return []
        # Only return a value if the node is at the correct height
        elif self.find_node_level(self.root, current) == level:
            return [current]
        return self.get_level_helper(level, current.lChild) + self.get_level_helper(level, current.rChild)

    # Returns a list of nodes at a given level from left to right
    def get_level(self, level):
        nodes_in_level = self.get_level_helper(level, self.root)
        return nodes_in_level

    # Returns the list of the node that you see from left side
    # The order of the output should be from top to down
    def left_side_view(self):
        height = self.root.get_height()
        left_nodes = []
        # only the first value in the list returned by get_level()
        # would be seen from a left side view
        for level in range(height):
            level_nodes = self.get_level(level)
            left_nodes.append(level_nodes[0].data)
        return left_nodes

    # retruns a list of values that correspond to leaf nodes
    def find_leaf_nodes(self, current):
        if current == None:
            return []
        # only return a value if the current node is a leaf node
        if current.rChild == None and current.lChild == None:
            return [current.data]
        return self.find_leaf_nodes(current.lChild) + self.find_leaf_nodes(current.rChild)
    
    # returns the sum of the value of all leaves.
    # a leaf node does not have any children.
    def sum_leaf_nodes(self):
        leaf_nodes = self.find_leaf_nodes(self.root)
        return sum(leaf_nodes)
        
def make_tree(data):
    tree = Tree()
    for d in data:
        tree.insert(d)
    return tree


# Develop your own main function or test cases to be able to develop.
# Our tests on the Gradescop will import your classes and call the methods.

def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list(map(int, line)) 	# converts elements into ints
    t1 = make_tree(tree1_input)
    t1.print(t1.get_height())

    print("Tree range is: ",   t1.range())
    print("Tree left side view is: ", t1.left_side_view())
    print("Sum of leaf nodes is: ", t1.sum_leaf_nodes())
    print("##########################")

# Another Tree for test.
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list(map(int, line)) 	# converts elements into ints
    t2 = make_tree(tree2_input)
    t2.print(t2.get_height())

    print("Tree range is: ",   t2.range())
    print("Tree left side view is: ", t2.left_side_view())
    print("Sum of leaf nodes is: ", t2.sum_leaf_nodes())
    print("##########################")

# Another Tree
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list(map(int, line)) 	# converts elements into ints
    t3 = make_tree(tree3_input)
    t3.print(t3.get_height())

    print("Tree range is: ",   t3.range())
    print("Tree left side view is: ", t3.left_side_view())
    print("Sum of leaf nodes is: ", t3.sum_leaf_nodes())
    print("##########################")


if __name__ == "__main__":
    main()
