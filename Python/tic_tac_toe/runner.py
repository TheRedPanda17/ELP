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
      self._add_score_to_winner(result)
      self._reset()
      self._games_played += 1

    print('\nThanks for playing!\n')

  def _reset(self):
    self._player1.switch_symbol()
    self._player2.switch_symbol()
    board = Board()
    self._game = Game(self._player1, self._player2, board)

  def _play_again(self):
    if self._games_played == 0: return True
    print("\nPlay Again? (Y\\N)")
    choice = input()
    return choice == 'Y' or choice == 'y'

  def _add_score_to_winner(self, result):
    symbol = result.name[-1].upper()
    if symbol == self._player1.symbol:
      self._player1.add_win()
      print('\n{0} won!'.format(self._player1.name))
    elif symbol == self._player2.symbol:
      self._player2.add_win()
      print('\n{0} won!'.format(self._player2.name))
    else: print('Tie game!')