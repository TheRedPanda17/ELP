from player import Player

def test_player_created_has_name():
  player_name = 'player'
  player = Player(player_name)

  assert player.name == player_name