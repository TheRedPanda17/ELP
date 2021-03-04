# Create players
from game import Game
from board import Board
from setup import get_player

player1 = get_player(1)
player2 = get_player(2)

board = Board()

game = Game(player1, player2, board)