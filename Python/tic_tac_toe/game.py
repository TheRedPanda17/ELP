class Game:
  def __init__(self, player1, player2, board):
      self.player1 = player1
      self.player2 = player2
      self.board = board
      self._has_winner = False

      self._next_up = player1
  
  def start(self):
    print('\nNew Game\n')
    print('Current score: {0}'.format(self.get_score()))
    while not self._has_winner:
      self.run_turn()

  def run_turn(self):
    print("\n{0}'s turn. \n".format(self._next_up.name))
    print(self.board)

    self._get_slot_and_take_turn()

    print(self.board)
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
    self.board.take_turn(slot, self._next_up.symbol)