import pytest

from vault import Vault

@pytest.fixture(scope="session")
def atari_2600():
    return Vault("Atari2600")
