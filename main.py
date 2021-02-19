import itertools


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        print("   0  1  2")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map

    except IndexError as e:
        print("Error: make sure you input row/column as 0, 1 or 2", e)

    except Exception as e:
        print("Something went wrong", e)


def win(current_game):
    # Vertical win
    for col in range(len(current_game)):
        check = []
        for row in game:
            check.append(row)

        if check.count(check[0]) == len(check) and check[0] != 0:
            print(f"Player {check[0]} won vertically")

    # Horizontal win
    for row in current_game:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print(f"Player {row[0]} won horizontally")

    # Diagonal win
    diagonal_1 = []
    for col, row in enumerate(reversed(range(len(current_game)))):
        diagonal_1.append(current_game[row][col])
    if diagonal_1.count(diagonal_1[0]) == len(diagonal_1) and diagonal_1[0] != 0:
        print(f"Player {diagonal_1[0]} won diagonally (/)")

    diagonal_2 = []
    for idx in range(len(current_game)):
        diagonal_2.append(current_game[idx][idx])
    if diagonal_2.count(diagonal_2[0]) == len(diagonal_2) and diagonal_2[0] != 0:
        print(f"Player {diagonal_2[0]} won diagonally (\\)")


play = True
players = [1, 2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    game_won = False
    game = game_board(game, just_display=True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        column_choice = int(input(f"Player {current_player}: What column do you want to play? (0, 1, 2): "))
        row_choice = int(input(f"Player {current_player}: What row do you want to play? (0, 1, 2): "))
        game = game_board(game, player=current_player, row=row_choice, column=column_choice)
