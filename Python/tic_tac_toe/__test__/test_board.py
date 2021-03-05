from utils import get_empty_board
from board import Board
from io import StringIO
import sys

def test_board_init_returns_three_rows_of_three():
  board = Board()
  assert board._slots == get_empty_board()

def test_row_from_index_returns_correct_values():
  board = Board()

  assert board.get_row_from_index(1) == 0
  assert board.get_row_from_index(2) == 0
  assert board.get_row_from_index(3) == 0
  assert board.get_row_from_index(4) == 1
  assert board.get_row_from_index(5) == 1
  assert board.get_row_from_index(6) == 1
  assert board.get_row_from_index(7) == 2
  assert board.get_row_from_index(8) == 2
  assert board.get_row_from_index(9) == 2

def test_col_from_index_returns_correct_values():
  board = Board()

  assert board.get_col_from_index(1) == 0
  assert board.get_col_from_index(2) == 1
  assert board.get_col_from_index(3) == 2
  assert board.get_col_from_index(4) == 0
  assert board.get_col_from_index(5) == 1
  assert board.get_col_from_index(6) == 2
  assert board.get_col_from_index(7) == 0
  assert board.get_col_from_index(8) == 1
  assert board.get_col_from_index(9) == 2

def test_index_from_col_and_row_is_correct():
  board = Board()

  assert board.get_index_from_row_and_col(0, 0) == 1
  assert board.get_index_from_row_and_col(0, 1) == 2
  assert board.get_index_from_row_and_col(0, 2) == 3
  assert board.get_index_from_row_and_col(1, 0) == 4
  assert board.get_index_from_row_and_col(1, 1) == 5
  assert board.get_index_from_row_and_col(1, 2) == 6
  assert board.get_index_from_row_and_col(2, 0) == 7
  assert board.get_index_from_row_and_col(2, 1) == 8
  assert board.get_index_from_row_and_col(2, 2) == 9

def test_take_turn_adds_correct_mark():
  board = Board()
  slots = get_empty_board()

  slots [0][0] = 'X'
  board.take_turn(1, 'X')
  assert board._slots == slots
  
  slots [1][2] = 'X'
  board.take_turn(6, 'X')
  assert board._slots == slots
  
  slots [2][1] = 'X'
  board.take_turn(8, 'X')
  assert board._slots == slots

def test_take_turn_is_false_for_taken_slot():
  board = Board()
  board.take_turn(1, 'X')

  assert board.take_turn(1, ')') == False

def test_prints_board():
  empty_board_print  = " 1 | X | 3 \n"
  empty_board_print += "---|---|---\n"
  empty_board_print += " 4 | X | 6 \n"
  empty_board_print += "---|---|---\n"
  empty_board_print += " 7 | X | 9 "

  board = Board()
  board.take_turn(2, "X")
  board.take_turn(5, "X")
  board.take_turn(8, "X")

  assert empty_board_print == str(board)
  