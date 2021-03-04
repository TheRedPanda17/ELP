class Board:
  def __init__(self):
    self._slots = [[' ' for slot in range(1,4)] for slot in range(1,4)]


  def take_turn(self, index, symbol):
    col = self._get_col_from_index(index)
    row = self._get_row_from_index(index)

    print("Row: {0}".format(row))
    print("Col: {0}".format(col))

    self._slots[row][col] = symbol

  def _get_col_from_index(self, index):
    return (index - 1) % 3

  def _get_row_from_index(self, index):
    return int((index - 1) / 3)