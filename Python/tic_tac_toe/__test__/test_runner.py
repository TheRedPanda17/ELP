from utils import get_game
from runner import Runner

def test_runner_initializes_with_game():
  game = get_game()
  runner = Runner(game)

  assert runner._game == game

def test_runner_initializes_with_zero_games():
  game = get_game()
  runner = Runner(game)

  assert runner._games_played == 0

def test_play_again_returns_true_on_first_game():
  game = get_game()
  runner = Runner(game)

  assert runner._play_again() == True

def test_play_again_returns_true_y_input(monkeypatch):
  game = get_game()
  runner = Runner(game)
  runner._games_played = 1

  monkeypatch.setattr('builtins.input', lambda: 'Y')
  assert runner._play_again() == True

  monkeypatch.setattr('builtins.input', lambda: 'y')
  assert runner._play_again() == True

def test_play_again_returns_false_non_y_input(monkeypatch):
  game = get_game()
  runner = Runner(game)
  runner._games_played = 1

  monkeypatch.setattr('builtins.input', lambda: 'N')
  assert runner._play_again() == False

  monkeypatch.setattr('builtins.input', lambda: 'n')
  assert runner._play_again() == False

  monkeypatch.setattr('builtins.input', lambda: 'asdf')
  assert runner._play_again() == False