#  File: Spiral.py
#  Description:
#  Student Name: Tyler Smedley
#  Student UT EID: tws933
#  Partner Name:
#  Partner UT EID:
#  Course Name: CS 313E
#  Unique Number: 52020
#  Date Created: 01/12/2023
#  Date Last Modified: 01/17/2023

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n

import math
import sys

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

def changeDirection(direction):
    """based on the current direction, returns the next direction
    in order of r -> u -> l -> d -> r"""
    if direction == 'r':
        return 'u'
    elif direction == 'd':
        return 'r'
    elif direction == 'l':
        return 'd'
    else:
        return 'l'

def movePostion(spiralPosition, direction):
    # moves the current position on the spiral one spot over in the given direction
    if direction == 'r':
        spiralPosition[1] += 1
    elif direction == 'l':
        spiralPosition[1] -= 1
    elif direction == 'u':
        spiralPosition[0] += 1
    else:
        spiralPosition[0] -= 1

    return spiralPosition

def create_spiral(spiralSize):

    spiral = createBlankSpiral(spiralSize)  # calls the function to create a blank spiral
    number = 1               # the number that will be added to the spiral
    directionTurns = 0       # number of times the direction has changed
    traveled = 0             # the number of times the sprial has moved in one direction
    travelLimit = 1          # length the sprial can go in one direction before changing direction
    direction = 'r'          # the current direction the sprial is moving in
    spiralPosition = [math.floor(spiralSize/2), math.floor(spiralSize/2)]
    """Variables for the position on the spiral in terms of row and column.
    math.floor(spiralSize) makes the variables start in the middle of the sprial"""

    while number <= spiralSize ** 2:
        # once number = spiralSize ** 2, the spiral will be full
        addToSpiral(spiral, spiralPosition, number)
        if traveled == travelLimit:
            direction = changeDirection(direction)
            traveled = 0
            directionTurns += 1
            """once the distance moved in one direction = travelLimit, 
            the direction numbers are added in must change"""
        if directionTurns == 2:
            travelLimit += 1
            directionTurns = 0
            """After two direction changes, the travel limit must increase so 
            that the spiral can expand"""
        movePostion(spiralPosition, direction)
        traveled += 1
        number += 1
        
    return spiral
    
# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0

def locate_num(spiral, num):
    location = [0, 0]
    for row in spiral:
        if num in row:
            location[1] = row.index(num)
            break
        location[0] += 1 
    return location
    
def position_exists(spiral, position):
    length = len(spiral) - 1
    if position[0] < 0 or position[0] > length:
        return False
    elif position[1] < 0 or position[1] > length:
        return False
    else:
        return True

def sum_adjacent_numbers(spiral, num):
    
    spiral_position = locate_num(spiral, num)
    sum = 0
    directions = ['r', 'd', 'l', 'l', 'u', 'u', 'r', 'r']

    for direction in directions:
        adjacent_position = movePostion(spiral_position, direction)
        if position_exists(spiral, adjacent_position):
            adjacent_num = spiral[adjacent_position[0]][adjacent_position[1]]
            sum += adjacent_num

    return sum

def main():

    inFile = sys.stdin.read().strip().split('\n')
    spiralSize = int(inFile[0])
    inFile.pop(0)
    if spiralSize % 2 == 0: spiralSize += 1
    """Takes the first line from spiral.in and converts it to an integer.
    If the first number in the file was even, it is increased by one.
    This will be the length and width of the spiral"""

    # create the spiral
    spiral = create_spiral(spiralSize)

    for num in inFile:
        sum = sum_adjacent_numbers(spiral, int(num))
        print(sum)

if __name__ == "__main__":
    main()