# Create players
from runner import Runner
from game import Game
from board import Board
from setup import get_player

player1 = get_player(1)
player2 = get_player(2)

runner = Runner(player1, player2)

runner.run()