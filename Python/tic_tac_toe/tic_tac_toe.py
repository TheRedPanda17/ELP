# Create players
from runner import Runner
from setup import get_player

print('\nWelcome to Python Tic Tac Toe!')

player1 = get_player(1)
player2 = get_player(2)
runner = Runner(player1, player2)

runner.run()