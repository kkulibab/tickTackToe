import itertools


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("This position is occupied. Choose another")
            return game_map, False
        print("   " + " ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map, True

    except IndexError as e:
        print("Error: make sure you input row/column as 0, 1 or 2", e)
        return game_map, False

    except Exception as e:
        print("Something went wrong", e)
        return game_map, False


def win(current_game):

    def all_same(ll):
        if row.count(ll[0]) == len(ll) and ll[0] != 0:
            return True
        else:
            return False

    # Vertical win
    for col in range(len(current_game)):
        check = []
        for row in game:
            check.append(row)

        if all_same(col):
            print(f"Player {check[0]} won vertically")
            return True

    # Horizontal win
    for row in current_game:
        print(row)
        if all_same(row):
            print(f"Player {row[0]} won horizontally")
            return True

    # Diagonal win
    diagonal_1 = []
    for col, row in enumerate(reversed(range(len(current_game)))):
        diagonal_1.append(current_game[row][col])
    if all_same(diagonal_1):
        print(f"Player {diagonal_1[0]} won diagonally (/)")
        return True

    diagonal_2 = []
    for idx in range(len(current_game)):
        diagonal_2.append(current_game[idx][idx])
    if all_same(diagonal_2):
        print(f"Player {diagonal_2[0]} won diagonally (\\)")
        return True
    return False


play = True
players = [1, 2]
while play:
    game_size = int(input("What game size do you want? "))
    game = [[0 for i in range(game_size)] for j in range(game_size)]

    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player: {current_player}")
        played = False
        while not played:
            column_choice = int(input(f"Player {current_player}: What column do you want to play? (0, 1, 2): "))
            row_choice = int(input(f"Player {current_player}: What row do you want to play? (0, 1, 2): "))
            game, played = game_board(game, player=current_player, row=row_choice, column=column_choice)

        if win(game):
            game_won = True
            again = input("Game over, do you want to play again? (y/n) ")
            if again.lower() == "y":
                print("restarting")
            elif again.lower() == "n":
                print("Bye")
                play = False
            else:
                print("Not a valid answer. Bye")
                play = False
