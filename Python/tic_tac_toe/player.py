class Player:
  player_count = 0

  def __init__(self, name):
    self.name = name
    self.symbol = 'X' if self.player_count < 1 else 'O'
    self.wins = 0

    Player.player_count += 1