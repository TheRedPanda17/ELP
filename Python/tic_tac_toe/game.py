class Game:
  def __init__(self, player1, player2, board):
      self.player1 = player1
      self.player2 = player2
      self.board = board

      self._next_up = player1
  
  def change_turns(self):
    if self._next_up == self.player1:
      self._next_up = self.player2
    else:
      self._next_up = self.player1