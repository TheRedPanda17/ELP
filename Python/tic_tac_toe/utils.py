from player import Player
from board import Board
from game import Game

def get_game(): return Game(Player('P1'), Player('P2'), Board())
  
def get_empty_board(): 
  return [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]