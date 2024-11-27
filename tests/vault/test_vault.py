import pytest
from vault import Vault


class TestVault:
    def test_init(self, atari_2600):
        assert atari_2600.console == "Atari2600"

        assert Vault("PlayStation 3", validate=False).console == "PlayStation 3"

        with pytest.raises(ValueError) as _:
            Vault("Playstation 3")

        assert Vault("PS2", validate=True, auto_scrape=True).entries is not None 

    def test_scrape(self):
        ps2 = Vault("PS2", auto_scrape=True)
        assert ps2.entries is not None
        assert len(ps2.entries) == 1807

        assert "Hitman: Blood Money" in ps2.entries
        assert "Devil May Cry 3: Dante's Awakening" in ps2.entries
        assert "Sly 2: Band of Thieves" in ps2.entries
