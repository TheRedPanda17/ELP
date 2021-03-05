class Board:
  def __init__(self):
    self._slots = [[' ' for _ in range(1,4)] for slot in range(1,4)]

  def take_turn(self, index, symbol):
    col = self.get_col_from_index(index)
    row = self.get_row_from_index(index)

    if self._slots[row][col] == " ":
      self._slots[row][col] = symbol
      return True
    return False

  def __str__(self, string = ""):
    for row in range(0, 3):
      string += self._get_row_string(row)
      if row != 2:
        string += "\n---|---|---\n"
    return string

  def _get_row_string(self, row):
    return " {0} | {1} | {2} ".format(
      self._slot_str(row, 0), 
      self._slot_str(row, 1), 
      self._slot_str(row, 2))

  def _slot_str(self, row, col):
    if self._slots[row][col] != ' ':
      return self._slots[row][col]
    else:
      return self.get_index_from_row_and_col(row, col)
 
  def get_col_from_index(_, index):
    return (index - 1) % 3

  def get_row_from_index(_, index):
    return int((index - 1) / 3)

  def get_index_from_row_and_col(_, row, col):
    return (col + 1) + (3 * row)