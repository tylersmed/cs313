#  File: Adjacency.py
#  Description: Converts an edge list into an adjacency matrix
#  Student Name: Tyler Smedley
#  Student UT EID: tws933
#  Course Name: CS 313E
#  Unique Number: 52020

def edge_to_adjacency(edge_list):
    
    vert_list = []
    for edge in edge_list:
        start, stop = edge[0], edge[1]
        if start not in vert_list:
            vert_list.append(start)
        if stop not in vert_list:
            vert_list.append(stop)
    vert_list.sort()

    D = len(vert_list)
    adjMat = [[0 for x in range(D)] for x in range(D)]

    for edge in edge_list:
        start, stop, weight = edge[0], edge[1], edge[2]
        start_indx, stop_indx = vert_list.index(start), vert_list.index(stop)
        adjMat[start_indx][stop_indx] = weight

    return adjMat

# ------ DO NOT CHANGE BELOW HERE ------ #
import ast

def main():
    matrix = edge_to_adjacency(ast.literal_eval(input()))

    print('\n'.join([' '.join([str(cell) for cell in row]) for row in matrix]))

if __name__ == "__main__":
    main()
