from vault.utils import request_letter, request_vault

class TestUtils:
    def test_request_vault(self):
        pass

    def test_request_letter(self):
        res = request_letter("Atari2600", "A")
        assert len(res) == 23
        assert res[0] == "Activision Decathlon, The"

        res = request_letter("PS3", "D")
        assert len(res) == 134
        assert res[6] == "Dark Souls"
