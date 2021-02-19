game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


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


def vertical_win(current_game):
    for col in range(len(current_game)):
        check = []
        for row in game:
            check.append(row)

        if check.count(check[0]) == len(check) and check[0] != 0:
            print("Winner")


def horizontal_win(current_game):
    for row in current_game:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print("Winner")


game = game_board(game, just_display=True)
game = game_board(game, player=1, row=2, column=1)
