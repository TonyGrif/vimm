from vault.utils import request_letter, request_vault

class TestUtils:
    def test_request_vault(self):
        res = request_vault("Atari2600")
        assert len(res) == 478

        assert "Pitfall! Pitfall Harry's Jungle Adventure" in res
        assert "Missile Command" in res
        assert "Space Invaders" in res

    def test_request_letter(self):
        res = request_letter("Atari2600", "A")
        assert len(res) == 23
        assert res[0] == "Activision Decathlon, The"

        res = request_letter("PS3", "D")
        assert len(res) == 134
        assert res[6] == "Dark Souls"
