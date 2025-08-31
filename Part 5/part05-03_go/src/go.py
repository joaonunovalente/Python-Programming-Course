# Write your solution here

def who_won(game_board: list) -> int:
    result = 0

    for row in game_board:
        for item in row:
            if item == 2:
                result -= 1
            elif item == 1:
                result += 1
    if result > 0:
        player = 1
    elif result < 0:
        player = 2
    else:
        player = 0

    return player

if __name__ == "__main__":
    game_board = [[1, 2, 1], [0, 0, 1], [2, 1, 0]]
    who_won(game_board)