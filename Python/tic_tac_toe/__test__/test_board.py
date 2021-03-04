from board import Board

def get_empty_board(): return [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def test_board_init_returns_three_rows_of_three_slots():
  board = Board()
  assert board._slots == get_empty_board()

def test_row_from_index_returns_correct_values():
  board = Board()

  assert board._get_row_from_index(1) == 0
  assert board._get_row_from_index(2) == 0
  assert board._get_row_from_index(3) == 0
  assert board._get_row_from_index(4) == 1
  assert board._get_row_from_index(5) == 1
  assert board._get_row_from_index(6) == 1
  assert board._get_row_from_index(7) == 2
  assert board._get_row_from_index(8) == 2
  assert board._get_row_from_index(9) == 2

def test_col_from_index_returns_correct_values():
  board = Board()

  assert board._get_col_from_index(1) == 0
  assert board._get_col_from_index(2) == 1
  assert board._get_col_from_index(3) == 2
  assert board._get_col_from_index(4) == 0
  assert board._get_col_from_index(5) == 1
  assert board._get_col_from_index(6) == 2
  assert board._get_col_from_index(7) == 0
  assert board._get_col_from_index(8) == 1
  assert board._get_col_from_index(9) == 2

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
