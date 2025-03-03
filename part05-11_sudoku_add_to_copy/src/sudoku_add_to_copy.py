import copy

def print_sudoku(sudoku):
    count2 = 0
    for row in sudoku:
        count2 += 1

        count = 0
        for element in row:
            if count >= 3:
                print(" ", end="")
                count = 0

            if element == 0:
                print("_", end=" ")
            else:
                print(element, end=" ")
            count += 1
        if count2 >= 3:
            count2 = 0
            print()
        print()

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):



    grid_copy = copy.deepcopy(sudoku)

    grid_copy[row_no][column_no] = number

    return grid_copy


if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)