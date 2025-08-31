# Write your solution here

def play_turn(game_board: list, x: int, y: int, piece: str) -> bool:
    game_board[y-1][x-1] = piece

    count_X = 0
    count_O = 0

    # Rows
    for row in game_board:
        for element in row:
            if element == "X":
                count_X += 1
            elif element == "O":
                count_O += 1
            else:
                count_O = 0
                count_X = 0
        if count_O == 3 or count_X == 3:
            return True

    new_board = []
    column_1 = []
    column_2 = []
    column_3 = []
    # Columns
    for row in game_board:
        column_1.append(row[0])
        column_2.append(row[1])
        column_3.append(row[2])
    
    new_board.append(column_1)
    new_board.append(column_2)
    new_board.append(column_3)
    print(new_board)

    for row in new_board:
        for element in row:
            if element == "X":
                count_X += 1
            elif element == "O":
                count_O += 1
            else:
                count_O = 0
                count_X = 0
    if count_O == 3 or count_X == 3:
        return True



    return False


if __name__ == "__main__":
    game_board = [['', '', ''], ['O', '', 'X'], ['X', '', 'O']]
    print(game_board)
    print(play_turn(game_board, 3, 0, "X"))
    print(game_board)