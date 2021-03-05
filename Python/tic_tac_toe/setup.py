from board import Board
from player import Player

def get_player(player_number):
  symbol = 'X' if player_number == 1 else 'O'
  name = input("Player {0}, what is your name?\n".format(player_number))
  return Player(name, symbol)

def get_board():
  return Board()