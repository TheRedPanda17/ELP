from player import Player
import pytest

@pytest.fixture(autouse=True)
def run_around_tests():
  Player.player_count = 0
  yield

def test_player_created_has_name():
  player_name = 'player'
  player = Player(player_name)

  assert player.name == player_name

def test_player_starts_with_zero_wins():
  player_name = 'player'
  player = Player(player_name)

  assert player.wins == 0

def test_first_player_has_symbol_x():
  player1 = Player('p1')

  assert player1.symbol == 'X'

def test_second_player_has_symbol_o():
  player1 = Player('p1')
  player2 = Player('p2')

  assert player2.symbol == 'O'