import pytest
from vault import Vault


class TestVault:
    def test_init(self, atari_2600):
        assert atari_2600.console == "Atari2600"
        assert Vault("Atari2600", validate=True).console == "Atari2600"

        assert Vault("PlayStation 3").console == "PlayStation 3"

        with pytest.raises(ValueError) as _:
            Vault("Playstation 3", validate=True)
