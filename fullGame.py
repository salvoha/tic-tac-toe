import random

class Player:
    def __init__(self, name: str, symbol: str):
        self.name = name
        self.symbol = symbol  # "X" or "O"


def intro():
    print("Welcome to this exciting game of Tic-Tac-Toe.\n"
          "You will play by putting your symbol (X or O)\n"
          "into the grid by calling a number between 1 and 9.")
    print()
    print("To visualize where you can put your symbol, see this grid:\n")

    print("1 | 2 | 3")
    print("--+---+--")
    print("4 | 5 | 6")
    print("--+---+--")
    print("7 | 8 | 9\n")

    print("But first, let's see who you are :)\n")


def print_board(board):
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()


WINNING_COMBINATIONS = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]


def check_win(board, symbol):
    for a, b, c in WINNING_COMBINATIONS:
        if board[a] == board[b] == board[c] == symbol:
            return True
    return False


def is_board_full(board):
    return " " not in board


def get_player_move(board, player: Player):
    while True:
        move = input(f"{player.name} ({player.symbol}), choose a position (1-9): ")

        if not move.isdigit():
            print("Please enter a number between 1 and 9.")
            continue

        pos = int(move) - 1

        if pos < 0 or pos > 8:
            print("Position must be between 1 and 9.")
            continue

        if board[pos] != " ":
            print("That field is already taken.")
            continue

        return pos


def create_players():
    name1 = input("Player 1, enter your name: ").strip() or "Player 1"
    name2 = input("Player 2, enter your name: ").strip() or "Player 2"

    while True:
        symbol1 = input(f"{name1}, choose your symbol (X/O): ").strip().upper()
        if symbol1 in ("X", "O"):
            break
        print("Invalid choice. Please type X or O.")

    symbol2 = "O" if symbol1 == "X" else "X"

    player1 = Player(name1, symbol1)
    player2 = Player(name2, symbol2)

    print(f"\n{player1.name} is {player1.symbol}")
    print(f"{player2.name} is {player2.symbol}\n")

    return player1, player2

#choosing starting player 
def choose_starting_player(player1, player2):
    starting_player = random.choice([player1, player2])
    print(f"Coin flip result: {starting_player.name} starts the first round!\n")
    return starting_player


def play_single_round(starting_player: Player, other_player: Player):
    """Play ONE game of Tic-Tac-Toe. Does not ask 'play again'."""
    board = [" "] * 9
    current_player = starting_player

    while True:
        print_board(board)
        move = get_player_move(board, current_player)
        board[move] = current_player.symbol

        # Check win
        if check_win(board, current_player.symbol):
            print_board(board)
            print(f"{current_player.name} ({current_player.symbol}) wins this round!\n")
            break

        # Check draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw!\n")
            break

        # Switch player
        current_player = other_player if current_player is starting_player else starting_player


def main():
    intro()
    player1, player2 = create_players()

    # First game: random coin flip
    starting_player = choose_starting_player(player1, player2)
    other_player = player1 if starting_player is player2 else player2

    while True:
        # Play one round with the current starting player
        play_single_round(starting_player, other_player)

        # Ask if they want to play again
        answer = input("Do you want to play again? (y/n): ").strip().lower()
        if answer not in ("y", "yes"):
            print("\nThanks for playing. Goodbye!")
            break

        # Swap starting player for the next game:
        # the player who did NOT begin last time starts now.
        starting_player, other_player = other_player, starting_player
        print(f"\nNew round! This time {starting_player.name} starts.\n")


if __name__ == "__main__":
    main()
