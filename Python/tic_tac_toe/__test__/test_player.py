from player import Player
import pytest

@pytest.fixture(autouse=True)
def run_around_tests():
  Player.player_count = 0
  yield

def test_player_created_has_name():
  player_name = 'player'
  player = Player(player_name, 'X')

  assert player.name == player_name

def test_player_starts_with_zero_wins():
  player_name = 'player'
  player = Player(player_name, 'X')

  assert player.wins == 0

def test_add_win():
  player = Player('Player', 'X')
  player.add_win()

  assert player.wins == 1

def test_switch_symbol():
  player = Player('Player', 'X')

  assert player.symbol == 'X'

  player.switch_symbol()

  assert player.symbol == 'O'