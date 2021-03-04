class Board:
  def __init__(self):
    self.clean_board()


  def take_turn(self, index, symbol):
    col = self._get_col_from_index(index)
    row = self._get_row_from_index(index)

    self._slots[row][col] = symbol

  def clean_board(self):
    self._slots = [[' ' for slot in range(1,4)] for slot in range(1,4)]

  def _get_col_from_index(self, index):
    return (index - 1) % 3

  def _get_row_from_index(self, index):
    return int((index - 1) / 3)

  def _get_index_from_row_and_col(self, row, col):
    return (col + 1) + (3 * row)

  def __str__(self):
    string = ""
    for row_num, row in enumerate(self._slots):
      string += self._get_row_string(row)
      string += self._get_row_formatter(row_num)
    return string

  def _get_row_string(self, row):
    return " {0} | {1} | {2} ".format(row[0], row[1], row[2])

  def _get_row_formatter(self, row_num):
    indexes = [self._get_index_from_row_and_col(row_num, col) for col in range(0, 3)]
    formated_string = "    {0} | {1} | {2} ".format(indexes[0], indexes[1], indexes[2])
    if row_num != 2:
      formated_string += "\n---|---|---   ---|---|---\n"
    return formated_string