class Player:
  def __init__(self, name, symbol):
    self.name = name
    self.symbol = symbol
    self.wins = 0

  def add_win(self):
    self.wins += 1

  def switch_symbol(self):
    self.symbol = 'X' if self.symbol == 'O' else 'O'