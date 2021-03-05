class Board:
  def __init__(self):
    self.clean_board()


  def take_turn(self, index, symbol):
    col = self._get_col_from_index(index)
    row = self._get_row_from_index(index)

    self._slots[row][col] = symbol

  def clean_board(self):
    self._slots = [[' ' for _ in range(1,4)] for slot in range(1,4)]

  def _get_col_from_index(_, index):
    return (index - 1) % 3

  def _get_row_from_index(_, index):
    return int((index - 1) / 3)

  def _get_index_from_row_and_col(self, row, col):
    return (col + 1) + (3 * row)

  def __str__(self):
    string = ""
    for row_num in range(0, 3):
      string += self._get_row_string(row_num)
      if row_num != 2:
        string += "\n---|---|---\n"
    return string

  def _get_row_string(self, row_num):
    return " {0} | {1} | {2} ".format(
      self._get_slot_for_print(row_num, 0), 
      self._get_slot_for_print(row_num, 1), 
      self._get_slot_for_print(row_num, 2))

  def _get_slot_for_print(self, row_num, col_num):
    if self._slots[row_num][col_num] != ' ':
      return self._slots[row_num][col_num]
    else:
      return self._get_index_from_row_and_col(row_num, col_num)