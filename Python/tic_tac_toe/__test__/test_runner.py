from player import Player
from utils import get_game
from runner import Runner
from checker import Game_Results
import pytest

@pytest.fixture(autouse=True)
def run_around_tests():
  Player.player_count = 0
  yield

def test_runner_initializes_with_players():
  player1 = Player('1', 'X')
  player2 = Player('2', 'O')
  runner = Runner(player1, player2)

  assert runner._player1 == player1
  assert runner._player2 == player2

def test_runner_initializes_with_zero_games():
  runner = Runner(Player('1', 'X'), Player('2', 'O'))

  assert runner._games_played == 0

def test_play_again_returns_true_on_first_game():
  runner = Runner(Player('1', 'X'), Player('2', 'O'))

  assert runner._play_again() == True

def test_runner_has_game():
  runner = Runner(Player('1', 'X'), Player('2', 'O'))

  assert runner._game != None

def test_play_again_returns_true_y_input(monkeypatch):
  runner = Runner(Player('1', 'X'), Player('2', 'O'))
  runner._games_played = 1

  monkeypatch.setattr('builtins.input', lambda _: 'Y')
  assert runner._play_again() == True

  monkeypatch.setattr('builtins.input', lambda _: 'y')
  assert runner._play_again() == True

def test_play_again_returns_false_non_y_input(monkeypatch):
  runner = Runner(Player('1', 'X'), Player('2', 'O'))
  runner._games_played = 1

  monkeypatch.setattr('builtins.input', lambda _: 'N')
  assert runner._play_again() == False

  monkeypatch.setattr('builtins.input', lambda _: 'n')
  assert runner._play_again() == False

  monkeypatch.setattr('builtins.input', lambda _: 'asdf')
  assert runner._play_again() == False

def test_add_score_to_winner_p1():
  runner = Runner(Player('1', 'X'), Player('2', 'O'))

  runner._end_game(Game_Results.player_x)

  assert runner._player1.wins == 1

def test_add_score_to_winner_p2():
  runner = Runner(Player('1', 'X'), Player('2', 'O'))

  runner._end_game(Game_Results.player_o)

  assert runner._player2.wins == 1

def test_add_score_to_winner_none():
  runner = Runner(Player('1', 'X'), Player('2', 'O'))

  runner._end_game(Game_Results.cats_game)

  assert runner._player1.wins == 0
  assert runner._player2.wins == 0
