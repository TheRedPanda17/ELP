from checker import Checker, Game_Results

class Game:
  def __init__(self, player1, player2, board):
      self.player1 = player1
      self.player2 = player2
      self.board = board
      self._checker = Checker(self.board)

      self._next_up = player1
  
  def play(self, result = Game_Results.not_over):
    print('\nNew Game\n\nCurrent score: {0}'.format(self.get_score()))
    
    while result == Game_Results.not_over:
      self.run_turn()
      result = self._checker.get_result()

    return result

  def run_turn(self):
    print("\n{0}'s turn. Pick a slot\n".format(self._next_up.name))
    print(self.board)

    if self._get_slot_and_take_turn():
      self.change_turns()

  def change_turns(self):
    if self._next_up == self.player1:
      self._next_up = self.player2
    else:
      self._next_up = self.player1

  def get_score(self):
    return "{0} has {1} wins. {2} has {3} wins.".format(
      self.player1.name,
      self.player1.wins,
      self.player2.name,
      self.player2.wins,
    )

  def _get_slot_and_take_turn(self):
    slot = int(input())
    return self.board.take_turn(slot, self._next_up.symbol)