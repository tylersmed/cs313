#  File: Symmetric.py

#  Description: Determines if a square 2d list of 1s and 0s has some "symmetry" where the matrix is
#               the same as its transpose

#  Student Name: Tyler Smedley

#  Student UT EID: tws933

#  Course Name: CS 313E

#  Unique Number: 52020

# Prints your 2d list
# Can be used for debugging purposes
def print_arr(temp):
    mx = max((len(str(ele)) for sub in temp for ele in sub))
    for row in temp:
        print(" ".join(["{:<{mx}}".format(ele,mx=mx) for ele in row]))
    print()


# Input: matrix is a 2d square list of 1s and 0s
# Output: return True if the matrix is equal to its transpose (rows and columns swapped)
# return False otherwise
def matrix_has_symmetry(matrix):
    n = len(matrix)
    for row in range(n):
        for col in range(n):
            if matrix[row][col] != matrix[col][row]:
                return False
    return True

def main():
    # read dimension of square matrix
    n = int(input())

    matrix = []
    # read data from standard input
    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    # get the result from your call to matrix_has_symmetry()
    result = matrix_has_symmetry(matrix)

    # print the result to standard output
    print(result)

if __name__ == "__main__":
    main()
