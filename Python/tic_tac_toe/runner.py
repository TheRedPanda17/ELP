class Runner:
  def __init__(self, game):
    self._game = game
    self._games_played = 0

  def run(self):
    print('\nWelcome to Tic Tac Toe in Python')
    while self._play_again():
      self._game.start()

  def _play_again(self):
    if self._games_played == 0: return True
    print("\nPlay Again? (Y\\N)\n")
    choice = input()
    return choice == 'Y' or choice == 'y'
