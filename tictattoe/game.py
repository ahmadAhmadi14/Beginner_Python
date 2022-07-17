import math
import time
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer

 #STEP 1 create class tictactoe 
class TicTacToe():
    def __init__(self):
        self.board = self.make_board() #use a single list to rep 3X3 board
        self.current_winner = None # keep track a winner!

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

#STEP 2 create print_board function
    def print_board(self):
        #this is just getting rows
            for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
                print('| ' + ' | '.join(row) + ' |')

#STEP 3 create fill a numb of board
    @staticmethod
    def print_board_nums():
            # 0 | 1 | 2 (tell us what number corresponds to what box)
            number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
            for row in number_board:
                print('| ' + ' | '.join(row) + ' |') 
     #STEP 7a          
    def make_move(self, square, letter):
        # if valid move, then make the move (assign square to letter)
        # then return true. if invalid, return false
        # STEP 8
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    #STEP 5

    # STEP 9
    def winner(self, square, letter):
            # check the row
            row_ind = math.floor(square / 3)
            row = self.board[row_ind*3:(row_ind+1)*3]
            # print('row', row)
            if all([s == letter for s in row]):
                return True

            # check column    
            col_ind = square % 3
            column = [self.board[col_ind+i*3] for i in range(3)]
            # print('col', column)
            if all([s == letter for s in column]):
                return True

            # Check diagonals
            # but only if the square is an even number (0, 2, 4, 6, 8)
            #these are the only moves possible to win a diagonal
            if square % 2 == 0:
                diagonal1 = [self.board[i] for i in [0, 4, 8]] # left to right diagonal
                # print('diag1', diagonal1)
                if all([s == letter for s in diagonal1]):
                    return True
                diagonal2 = [self.board[i] for i in [2, 4, 6]] # right to left diagonal
                # print('diag2', diagonal2)
                if all([s == letter for s in diagonal2]):
                    return True

            #if all these fail
            return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]

#STEP 4
def play(game, x_player, o_player, print_game=True):

    if print_game:
        game.print_board_nums()

# STEP 6
    letter = 'X' #starting letter
    # iterate while the game still has empty squares
    # (we don't have to worry about winner because we'll just return that)
    # which breaks the loop)
    while game.empty_squares():
        #get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        #let's define a function to make a move!
        #STEP 7a
        if game.make_move(square, letter):

            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')

            # STEP 9
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter  # ends the loop and exits the game
        
            # after we made our move, we need to alternate letters
            letter = 'O' if letter == 'X' else 'X'  # switches player

        time.sleep(.8)

    if print_game:
        print('It\'s a tie!')
   

if __name__ == '__main__':
    x_player = SmartComputerPlayer('X')
    o_player = HumanPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)