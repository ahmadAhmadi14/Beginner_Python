import math
import random

class Player:
    def __init__(safe, letter):
        #letter is x or o
        self.letter = letter

    #we want all players to get their next move given a game
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(safe, letter):
        super().__init__(letter)

    def get_game(self, game):
        pass

class HumanPlayer():
    def __init__(safe, letter):
        super().__init__(letter)

    def get_game(self, game):
        pass