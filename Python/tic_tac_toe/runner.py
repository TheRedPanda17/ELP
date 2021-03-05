from board import Board
from game import Game
from checker import Game_Results

class Runner:
  def __init__(self, player1, player2):
    self._player1 = player1
    self._player2 = player2
    self._games_played = 0
    board = Board()
    self._game = Game(self._player1, self._player2, board)

  def run(self):
    print('\nWelcome to Tic Tac Toe in Python')
    while self._play_again():
      result = self._game.play()
      self._reset()
      self._add_score_to_winner(result)
      self._games_played += 1

  def _reset(self):
    self._player1.switch_symbol()
    self._player2.switch_symbol()
    board = Board()
    self._game = Game(self._player1, self._player2, board)

  def _play_again(self):
    if self._games_played == 0: return True
    print("\nPlay Again? (Y\\N)\n")
    choice = input()
    return choice == 'Y' or choice == 'y'

  def _add_score_to_winner(self, result):
    if result == Game_Results.player_1: self._player1.add_win()
    elif result == Game_Results.player_2: self._player2.add_win()