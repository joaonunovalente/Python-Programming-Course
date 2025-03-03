def row_correct(sudoku: list, row_no: int) -> bool:
    # Method 1 - We can use argument-unpacking operator i.e. *.
    numbers = [*range(1,10)]

    # Method 2 - We can use the extend() function to unpack the result of range function.
    _extended_list = []
    _extended_list.extend(range(0,10))

    row = sudoku[row_no]
    for n in numbers:
        if row.count(n) > 1:
            return False
        
    return True


if __name__ == "__main__":
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(row_correct(sudoku, 0))
    print(row_correct(sudoku, 1))
