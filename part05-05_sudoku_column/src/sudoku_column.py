def column_correct(sudoku: list, column_no: int):

    numbers = [*range(1,10)]
    column = []

    for row in sudoku:
        column.append(row[column_no])

    print(column)
    for number in numbers:
        if column.count(number) > 1:
            return False
        
    return True


if __name__ == "__main__":
    sudoku = [
    [ 9, 0, 1, 0, 8, 0, 3, 0, 1 ],
    [ 2, 2, 0, 0, 5, 0, 7, 0, 0 ],
    [ 0, 2, 0, 3, 0, 0, 4, 0, 4 ],
    [ 2, 9, 4, 0, 0, 0, 2, 0, 0 ],
    [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],
    [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],
    [ 0, 0, 7, 8, 0, 3, 9, 8, 6 ],
    [ 3, 0, 1, 0, 0, 0, 0, 0, 1 ],
    [ 3, 0, 0, 0, 2, 0, 2, 0, 1 ],
    ]

    print(column_correct(sudoku, 3))
