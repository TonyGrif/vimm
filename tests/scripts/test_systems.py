from scripts import get_available_systems

def test_available_systems():
    res = get_available_systems()
    assert len(res) == 30
    assert res[0] == "Atari2600"
