from checker import Game_Results
from setup import get_player
from utils import get_empty_board, get_game
from player import Player
from board import Board
from game import Game
import pytest

@pytest.fixture(autouse=True)
def run_around_tests():
  Player.player_count = 0
  yield

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

def test_player_2_is_next_up():
  player2 = Player('P2')
  game = Game(Player('P1'), player2, Board())

  assert game._next_up == player2

def test_change_turn_updates_next_up():
  player1 = Player('P1')
  player2 = Player('P2')
  game = Game(player1, player2, Board())

  game.change_turns()

  assert game._next_up == player2

def test_run_turn_gets_turn_and_updates_board(monkeypatch):
  game = get_game()
  monkeypatch.setattr('builtins.input', lambda: '1')
  game.run_turn()
  expected_board = get_empty_board()
  expected_board[0][0] = 'X'

  assert expected_board == game.board._slots

  monkeypatch.setattr('builtins.input', lambda: "3")
  game.run_turn()
  expected_board[0][2] = 'O'

  assert expected_board == game.board._slots

def test_run_turn_on_taken_slot_does_not_update(monkeypatch):
  game = get_game()
  expected_board = get_empty_board()
  expected_board[0][0] = 'X'

  monkeypatch.setattr('builtins.input', lambda: '1')
  game.run_turn()
  game.run_turn() # Second turn in same slot

  assert expected_board == game.board._slots

def test_turn_on_taken_slot_does_not_change_turn(monkeypatch):
  player1 = Player('P1')
  player2 = Player('P2')
  game = Game(player1, player2, Board())

  monkeypatch.setattr('builtins.input', lambda: '1')
  game.run_turn()
  game.run_turn()

  assert game._next_up == player2

def test_get_score_returns_names_and_scores():
  player1 = Player('Tam')
  player1.wins = 1
  player2 = Player('Mat')
  player2.wins = 3
  expected_message = "Tam has 1 wins. Mat has 3 wins."

  game = Game(player1, player2, Board())

  assert game.get_score() == expected_message