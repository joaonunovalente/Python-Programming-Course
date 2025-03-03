from random import shuffle


def roll(die: str) -> int:
    # number: int
    dice_A = [3, 3, 3, 3, 3, 6]
    dice_B = [2, 2, 2, 5, 5, 5]
    dice_C = [1, 4, 4, 4, 4, 4]

    if die == "A":
        shuffle(dice_A)
        number = dice_A[0]
    elif die == "B":
        shuffle(dice_B)
        number = dice_B[0]
    elif die == "C":
        shuffle(dice_C)
        number = dice_C[0]            
    
    return number


def play(die1: str, die2: str, times: int) -> tuple:
    win = 0
    lose = 0
    draw = 0
    for i in range(1, times + 1):
        dice_1 = roll(die1)
        dice_2 = roll(die2)

        if dice_1 > dice_2:
            win += 1
        elif dice_1 < dice_2:
            lose += 1
        else:
            draw += 1
    





    
    return (win, lose, draw)


if __name__ == "__main__":
    result = play("A", "C", 1000)
    print(result)
