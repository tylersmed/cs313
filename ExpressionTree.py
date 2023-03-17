#  File: ExpressionTree.py
#  Description:
#  Student Name: Tyler Smedley
#  Student UT EID: tws933
#  Partner Name:
#  Partner UT EID:
#  Course Name: CS 313E
#  Unique Number: 52020
#  Date Created: 03/14/23
#  Date Last Modified:

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append (data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

class Node (object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree (object):
    def __init__ (self):
        self.root = None
    
    # this function takes in the input string expr and 
    # creates the expression tree
    def create_tree (self, expr):
        self.root = Node()
        tokens = expr.split()
        stk = Stack()
        current = self.root
        print(tokens)
        for token in tokens:
            if token == '(':
                current.lChild = Node()
                stk.push(current)
                current = current.lChild
            elif token == ')':
                if not stk.is_empty:
                    current = stk.pop()
            elif token in operators:
                current.data = token
                stk.push(current)
                current.rChild = Node()
                current = current.rChild
            else:
                current.data = token
                current = stk.pop()

    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate (self, aNode):
        pass

    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, aNode):
        pass

    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, aNode):
        pass

# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
 
    tree = Tree()
    tree.create_tree(expr)
    
    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    # print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    # print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
    main()
