from board import Board
from player import Player

def get_player(player_number):
  print("Player {0}, what is your name?".format(player_number))
  return Player(input())

def get_board():
  return Board()