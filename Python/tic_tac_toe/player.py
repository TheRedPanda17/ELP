class Player:
  player_count = 0

  def __init__(self, name):
    self.name = name
    self.symbol = 'X' if self.player_count < 1 else 'O'
    self.wins = 0

    Player.player_count += 1

  def add_win(self):
    self.wins += 1

  def switch_symbol(self):
    self.symbol = 'X' if self.symbol == 'O' < 1 else 'O'