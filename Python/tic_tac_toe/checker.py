from board import Board
from enum import Enum

class Checker:
  winning_combos = [
    {0,1,2}, {3,4,5}, {6,7,8}, {0,3,6},
    {1,4,7}, {2,5,8}, {0,4,8}, {2,4,6} 
  ]

  def __init__(self, board):
      self._board = board

  def get_result(self):
    if self._player_wins('X'): return Game_Results.player_x
    elif self._player_wins('O'): return Game_Results.player_o
    elif self._board_is_full(): return Game_Results.cats_game
    return Game_Results.not_over

  def _player_wins(self, symbol):
    indexes = self._get_symbol_indexes(symbol)
    for combo in self.winning_combos:
      if combo.issubset(indexes): return True

  def _get_symbol_indexes(self, symbol):
    indexes = set()
    for index, slot in enumerate(self._get_flat_board()):
      if slot == symbol: indexes.add(index)
    return indexes

  def _board_is_full(self):
    return len(list(filter(
      lambda slot: slot != 'X' and slot != 'O', self._get_flat_board()))) == 0

  def _get_flat_board(self):
    return list([item for sublist in self._board._slots for item in sublist])

class Game_Results(Enum):
  player_x = 1
  player_o = 2
  cats_game = 3
  not_over = 4