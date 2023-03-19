#  File: ExpressionTree.py
#  Description: Given an infix expression, creates an expression tree, evaluates 
    # the expression, and converts to the expressions prefix and postfix versions
#  Student Name: Tyler Smedley
#  Student UT EID: tws933
#  Partner Name:
#  Partner UT EID:
#  Course Name: CS 313E
#  Unique Number: 52020
#  Date Created: 03/14/23
#  Date Last Modified: 03/19/23

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
    
    # this is a helper function to tell if a given string represents a number
    def is_num(self, value):
        try:
            float(value)
            return True
        except:
            return False
        
    # this function takes in the input string expr and 
    # creates the expression tree
    def create_tree (self, expr):
        self.root = Node()  # the empty tree should be an empty node, not None
        tokens = expr.split()
        stk = Stack()
        current = self.root
        for token in tokens:
            if token == '(':
                stk.push(current)
                current.lChild = Node()
                current = current.lChild
            elif token in operators:
                current.data = token
                stk.push(current)
                current.rChild = Node()
                current = current.rChild
            elif self.is_num(token):
                current.data = token
                current = stk.pop()
            elif token == ')':
                if not stk.is_empty():
                    current = stk.pop()

    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate (self, aNode):
        if self.is_num(aNode.data):
            return float(aNode.data)
            # return float here so eval() never returns an integer 
        return eval(f"{self.evaluate(aNode.lChild)} {aNode.data} {self.evaluate(aNode.rChild)}")

    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, aNode):
        if aNode == None:
            return ''
        return str(aNode.data) +' '+ self.pre_order(aNode.lChild) + self.pre_order(aNode.rChild)

    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, aNode):
        if aNode == None:
            return ''
        return self.post_order(aNode.lChild) + self.post_order(aNode.rChild) +' '+ str(aNode.data)
        
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
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
    main()
