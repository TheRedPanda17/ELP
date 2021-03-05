from setup import get_player

def test_creates_a_new_player_from_input(monkeypatch):
  player_name = 'player name'
  monkeypatch.setattr('builtins.input', lambda _: player_name)

  player = get_player(1)
  
  assert player.name == player_name
