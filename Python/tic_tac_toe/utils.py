from player import Player
from board import Board
from game import Game

def get_game(): return Game(Player('P1', 'X'), Player('P2', 'O'))
  
def get_empty_board(): 
  return [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]