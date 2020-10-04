winner = None
draw = False
current_player = 'X'

li = ['_', '_', '_',
      '_', '_', '_',
      '_', '_', '_']


def board():
    print(f'{li[0]} | {li[1]} | {li[2]}')
    print(f'{li[3]} | {li[4]} | {li[5]}')
    print(f'{li[6]} | {li[7]} | {li[8]}\n')


def check_winner():
    global winner
    if li[0:3] == "X" or li[4:7] == "X" or li[8:11] == "X":
        winner = "X"
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    if li[0:3] == "O" or li[4:7] == "O" or li[8:11] == "O":
        winner = 'O'
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    if li[0] == "X" and li[4] == "X" and li[8] == "X":
        winner = "X"
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    if li[2] == "O" and li[4] == "O" and li[6] == "O":
        winner = "O"
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    if li[0] == "X" and li[3] == "X" and li[6] == "X":
        winner = "X"
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    if li[1] == "X" and li[4] == "X" and li[7] == "X":
        winner = "X"
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    if li[2] == "X" and li[5] == "X" and li[8] == "X":
        winner = "X"
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    if li[0] == "O" and li[3] == "O" and li[6] == "O":
        winner = "O"
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    if li[1] == "O" and li[4] == "O" and li[7] == "O":
        winner = "O"
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    if li[2] == "O" and li[5] == "O" and li[8] == "O":
        winner = "O"
    return winner

def check_draw():
    global draw
    if li[0] != '_' and li[1] != '_' and li[2] != '_' and li[3] != '_' and li[4] != '_'and li[5] != '_'and li[6] != '_' and li[7] != '_'and li[8] != '_' and winner is None:
        draw = True
    return draw


def game():
    global current_player
    while True:
        if winner is not None:
            break
        if draw:
            break
        while True:
            check_draw()
            check_winner()
            if winner is not None:
                break
            board()
            if current_player == 'X':
                user = int(input("X's turn:\n")) - 1
                if li[user] == "_":
                    current_player = 'O'
                    li[user] = 'X'
                    break
                else:
                    print("\nThe place is already occupied")
                    pass
            else:
                user = int(input("O's turn:\n")) - 1
                if li[user] == "_":
                    current_player = 'X'
                    li[user] = 'O'
                else:
                    print("\nThe place is already occupied")
                    pass
        if winner is not None:
            print(f"The winner is {winner}")
            board()
        if draw:
            print(f"It's a draw")

game()