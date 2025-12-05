# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

#0. Flip a coin
#1. Ask the player to make a move
#2. If the square is already occupied go to step #1
#3. If win end the game
#4. If draw end the game
#5. Switch player
#6. Repeat to step #1

#import library
import random

#Defining a Player
class Player():
    def __init__(self, symbol):
        self.symbol = symbol
        print(f"Enter the name of the Player ({self.symbol}):")
        self.name = input()
        print(f"Welcome to the game {self.name}.")
    
    def __repr__(self):
        return f"{self.name} ({self.symbol})"


# Display the board
def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")


# Ask player to chose a cell and checks if it's valid
def player_turn(player, board):
    while True:
        cell = int(input(f"{player}, select a cell (1-9): ")) - 1  # Index start with 0, so we adjust it with -1
        if board[cell] == ' ' and 0 <= cell < 9:
            return cell
        else:
            print("You can't do this {player.name}. Please choose an empty cell (1-9).")

# Check if a player won the game
def check_win(player, board):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    for combo in winning_combinations:
        if all(board[i] == player.symbol for i in combo): #not sure why
            return True
    return False


# Tic-tac-toe game
if __name__ == "__main__":

    # Start a new round of Tic-tac-toe
    print("Welcome to a new round of Tic-Tac-Toe!")

    # Create players with names
    players = [Player('X'),Player('O')]

    # Chose who starts randomly
    print("Who is going to start the game? Let's flip a coin!")
    active_player = random.choice([players[0],players[1]])
    print(f"{factive_player.name} starts the game.")

    # Create board
    my_board = [" "]*9  # board with 9 spaces

    game_finished = False
    # Keep on playing until game is not finished
    while game_finished == False:
        display_board(my_board)
        move = player_turn(active_player, my_board)
        
    
    # ask player to make a choice
    player_turn(active_player, my_board)
    