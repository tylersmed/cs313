#  File: Spiral.py
#  Description:
#  Student Name: Tyler Smedley
#  Student UT EID: tws933
#  Partner Name:
#  Partner UT EID:
#  Course Name: CS 313E
#  Unique Number: 52020
#  Date Created: 01/12/2023
#  Date Last Modified:

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n

import math

def createBlankSpiral(spiralSize):
    """creates a two dimensional list where the length of every list is the arbitrary integer 
    sprialSize, contains only zeros, and then returns the created list"""
    size = [0] * spiralSize
    blankSpiral = [[x for x in size] for i in size]
    return blankSpiral

def addToSpiral(spiral, spiralPoition, number):
    # adds the next number to the spiral at the current position
    row = spiralPoition[0]
    column = spiralPoition[1]
    spiral[row][column] = number

def movePostion(spiralPostion, direction, travelLimit):

    moveRight = (0, 1)
    moveLeft = (0, -1)
    moveUp = (1, 0)
    moveDown = (-1, 0)


def create_spiral(spiralSize):

    spiral = createBlankSpiral(spiralSize)
    # calls the function to create a blank spiral

    number = 1
    # the number that will be added to the spiral
    travelLimit = 1
    # length the sprial can go in one direction before changing direction
    spiralPosition = (math.ceil(spiralSize), math.ceil(spiralSize))
    """Variables for the position on the spiral in terms of row and column.
    math.ceil(spiralSize) makes the variables start in the middle of the sprial"""

    while number <= spiralSize ** 2:
        addToSpiral(spiral, spiralPosition, number)


    return spiral
    
    
# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers(spiral, n):
    print("REMOVE THIS PRINT AND ADD YOUR CODE")


def main():

    inFile = open('spiral.in', 'r')
    spiralSize = int(inFile.readline())
    if spiralSize % 2 == 0: spiralSize += 1
    """Takes the first line from spiral.in and converts it to an integer.
    If the first number in the file was even, it is increased by one.
    This will be the length and width of the spiral"""

    # create the spiral
    spiral = create_spiral(spiralSize)
    print(spiral)

# add the adjacent numbers

# print the result

if __name__ == "__main__":
    main()