from checker import Checker, Game_Results
from board import Board


def test_has_board_stored_on_init():
  board = Board()
  checker = Checker(board)

  assert board == checker._board

def test_board_is_full_true():
  board = Board()
  board._slots = [['X', 'X', 'O'], ['O', 'X', 'O'], ['X', 'O', 'X']]
  checker = Checker(board)

  assert checker._board_is_full() == True

def test_board_is_full_false():
  board = Board()
  board._slots = [['X', 'X', 'O'], ['O', 'X', 'O'], ['X', 'O', '9']]
  checker = Checker(board)

  assert checker._board_is_full() == False
  
def test_get_symbols_indexes():
  board = Board()
  board._slots = [
    ['X', 'X', 'O'], 
    ['O', 'O', 'X'], 
    ['X', 'O', 'X']
  ]
  checker = Checker(board)

  assert checker._get_symbols_indexes('X') == {0, 1, 5, 6, 8}

def test_game_results_in_tie_on_full_board():
  board = Board()
  board._slots = [
    ['X', 'X', 'O'], 
    ['O', '5', 'X'], 
    ['X', 'O', '9']
  ]
  checker = Checker(board)

  assert checker.get_result() == Game_Results.not_over

def test_game_results_in_tie_on_full_board():
  board = Board()
  board._slots = [
    ['X', 'X', 'O'], 
    ['O', 'O', 'X'], 
    ['X', 'O', 'X']
  ]
  checker = Checker(board)

  assert checker.get_result() == Game_Results.cats_game

def test_game_results_in_px_win():
  board = Board()
  board._slots = [
    ['X', 'O', 'O'], 
    ['O', 'X', 'X'], 
    ['X', 'O', 'X']
  ]
  checker = Checker(board)

  assert checker.get_result() == Game_Results.player_x

def test_game_results_in_px_win():
  board = Board()
  board._slots = [
    ['O', 'X', 'X'], 
    ['O', 'O', 'X'], 
    ['X', 'X', 'O']
  ]
  checker = Checker(board)

  assert checker.get_result() == Game_Results.player_o