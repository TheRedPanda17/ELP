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
    while self._play_again():
      result = self._game.play()
      self._end_game(result)
      self._reset()

    print('\nThanks for playing!\n')

  def _reset(self):
    self._player1.switch_symbol()
    self._player2.switch_symbol()
    board = Board()
    self._game = Game(self._player1, self._player2, board)

  def _play_again(self):
    if self._games_played == 0: return True
    choice = input("\nPlay Again? (Y\\N)")
    return choice == 'Y' or choice == 'y'

  def _end_game(self, result):
    winner = self._get_winner(result)
    if winner:
      winner.add_win()
      print('\n{0} won!'.format(winner.name))
    else: print("Cat's Game")
    self._games_played += 1

  def _get_winner(self, result):
    symbol = result.name[-1].upper()
    if symbol == self._player1.symbol:
      return self._player1
    elif symbol == self._player2.symbol:
      return self._player2