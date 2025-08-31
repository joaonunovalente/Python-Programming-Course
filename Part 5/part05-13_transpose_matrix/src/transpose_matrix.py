import copy

def transpose(matrix):

    matrix_transposed = [row[:] for row in matrix]

    for i in (range(len(matrix))):
        for j in (range(len(matrix))):
            matrix_transposed[i][j] = matrix[j][i]
    matrix.clear()

    for row in matrix_transposed:
        matrix.append(row[:])

if __name__ == "__main__":
    matrix = [
        [1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]
        ]
    transpose(matrix)
    print(matrix)