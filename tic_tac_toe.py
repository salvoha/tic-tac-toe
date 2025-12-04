# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

# 1. Ask the player to make a move
# 2. If the square is already occupied go to step 1
# 3. If win end the game
# 4. If draw end the game
# 5. Switch player
# 6. Repeat to step 1


# Following our group Flow-chat:
# Start.

class TicTacToe:
    def __init__(self):
        self.board = ['0 - empty', '1 - empty', '2 - empty', '3 - empty', '4 - empty', '5 - empty', '6 - empty', '7 - empty', '8 - empty']
        self.rounds_played = 0
       # self.current_player = 1
        self.symbol_player_1 = ''
        self.symbol_player_2 = ''

   
    # Function for ... (displaying the board?)
    def display_board(self):
        row_1_data = [self.board[0], self.board[1], self.board[2]]
        row_2_data = [self.board[3], self.board[4], self.board[5]]
        row_3_data = [self.board[6], self.board[7], self.board[8]]
        col_1_data = [self.board[0], self.board[3], self.board[6]]
        col_2_data = [self.board[1], self.board[4], self.board[7]]
        col_3_data = [self.board[2], self.board[5], self.board[8]]
        diagonal_1 = [self.board[0], self.board[4], self.board[8]]
        diagonal_2 = [self.board[2], self.board[4], self.board[6]]
        
        row_1 = ''
        row_2 = ''
        row_3 = ''

        for field in row_1_data:
            row_1 += field + ' | '

        for field in row_2_data:
            row_2 += field + ' | '

        for entry in row_3_data:
            row_3 += entry + ' | '
        
        print(row_1)
        print(row_2)
        print(row_3)
        

    # Function for... (choosing a player?)
    # something with modulo
    def choose_a_player(self):
        if self.rounds_played == 0 or self.rounds_played % 2 == 0:
            print('It is player\'s 1 turn')
        else:
            print('It is player\'s 2 turn')


    # ... write as many functions as you need
    def choose_a_symbol(self):
        self.symbol_player_1 = input('Player 1, pick your symbol. Please type your choice. You can pick \'X\' or \'O\'').lower()
        if self.symbol_player_1 == 'x':
            self.symbol_player_2 = 'o'
            print(f'Player 1 picked: {self.symbol_player_1}. Player 2 gets {self.symbol_player_2} assigned.')
        elif self.symbol_player_1 == 'o':
            self.symbol_player_2 = 'x'
            print(f'Player 1 picked: {self.symbol_player_1}. Player 2 gets {self.symbol_player_2} assigned.')
        else:
            print(f'You choosed a wrong symbol!')

    def ask_for_player_input(self):
        player_input = int(input('Please type the number of the field you pick'))
        if self.rounds_played == 0 or self.rounds_played % 2 == 0:
            self.board[player_input] = f'{player_input} - {self.symbol_player_1}'       
        else:
            self.board[player_input] = f'{player_input} - {self.symbol_player_2}'


    def check_for_winner():
        pass

    def check_for_draw():
        pass

    def play(self):
        self.display_board()
        self.choose_a_player()
        self.choose_a_symbol()
        self.ask_for_player_input()
        self.display_board()
    






# Tic-tac-toe game
if __name__ == "__main__":

    # Start a new round of Tic-tac-toe
    print("Welcome to a new round of Tic-Tac-Toe!")

    current_game = TicTacToe()
    current_game.play()

    




