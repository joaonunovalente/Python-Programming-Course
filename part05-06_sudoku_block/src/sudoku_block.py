# Write your solution here

def block_correct(boardgame: list, row_no: int, column_no: int) -> bool:

    block: list = []
    for row in boardgame[row_no:row_no+3]:
        block.extend(row[column_no:column_no+3])

    for i in range(1, 10):
        if block.count(i) > 1:
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

    print(block_correct(sudoku, 0, 0))
    # print(block_correct(sudoku, 1, 2))