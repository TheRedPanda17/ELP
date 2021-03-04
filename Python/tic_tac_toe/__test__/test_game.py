from player import Player
from board import Board
from game import Game

def get_game():
  return Game(Player('P1'), Player('P2'), Board())

def test_game_initalizes_with_players_and_bard():
  player1 = Player('P1')
  player2 = Player('P2')
  board = Board()

  game = Game(player1, player2, board)

  assert game.player1 == player1
  assert game.player2 == player2
  assert game.board == board

def test_player_1_is_next_up():
  player1 = Player('P1')
  game = Game(player1, Player('P2'), Board())

  assert game._next_up == player1

def test_change_turn_updates_next_up():
  player1 = Player('P1')
  player2 = Player('P2')
  game = Game(player1, player2, Board())

  game.change_turns()

  assert game._next_up == player2
