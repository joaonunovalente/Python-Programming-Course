def column_correct(sudoku: list):
    for column_no in range(9):
        numbers = [*range(1,10)]
        column = []

        for row in sudoku:
            column.append(row[column_no])

        print(column)
        for number in numbers:
            if column.count(number) > 1:
                return False
        
    return True

def row_correct(sudoku: list) -> bool:
    for row in sudoku:
        numbers = [*range(1,10)]
        for n in numbers:
            if row.count(n) > 1:
                return False
        
    return True

def block_correct(boardgame: list) -> bool:

    for row_no in range(0, 9, 3):
        for column_no in range(0, 9, 3):
            block: list = []
            for row in boardgame[row_no:row_no+3]:
                block.extend(row[column_no:column_no+3])

            for i in range(1, 10):
                if block.count(i) > 1:
                    return False

        
    return True

def sudoku_grid_correct(sudoku: list) -> bool:
    result = [False, False, False]

    result[0] = column_correct(sudoku)
    result[1] = row_correct(sudoku)
    result[2] = block_correct(sudoku)

    if False in result:
        return False
    for
    

    return True

if __name__ == "__main__":
    sudoku = [
    [ 6, 4, 9, 2, 8, 3, 1, 5, 7 ],
    [ 0, 5, 0, 6, 4, 9, 2, 3, 8 ],
    [ 2, 3, 8, 1, 5, 7, 6, 4, 9 ],
    [ 9, 2, 3, 8, 1, 5, 0, 6, 4 ],
    [ 7, 6, 4, 9, 2, 3, 8, 1, 5 ],
    [ 8, 1, 5, 7, 0, 4, 9, 2, 0 ],
    [ 5, 7, 6, 4, 9, 2, 3, 2, 1 ],
    [ 4, 0, 2, 3, 8, 1, 5, 0, 6 ],
    [ 3, 0, 1, 5, 0, 6, 4, 9, 0 ],
    ]

    print(sudoku_grid_correct(sudoku))

