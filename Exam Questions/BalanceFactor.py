#  File: BalanceFactor.py

#  Description: Determines the balance factor of a binary tree

#  Student Name: Tyler Smedley

#  Student UT EID: tws933

#  Course Name: CS 313E

#  Unique Number: 52020

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Return the integer balance factor of a tree rooted at the given node.
def getHeight(node):
# # add your code here! 
    if node == None:
        return 0
    if node.left != None and node.right != None:
        return 1 + max(getHeight(node.left), getHeight(node.right))
    elif node.left != None:
        return 1 + getHeight(node.left)
    elif node.right != None:
        return 1 + getHeight(node.right)
    else:
        return 1

def balance_factor(node):
# add your code here!
    return getHeight(node.right) - getHeight(node.left)

# ------ DO NOT CHANGE BELOW HERE ------ #
import pickle
import sys


def main():
    data_in = ''.join(sys.stdin.readlines())
    node = pickle.loads(str.encode(data_in))

    print(balance_factor(node))


if __name__ == "__main__":
    main()
