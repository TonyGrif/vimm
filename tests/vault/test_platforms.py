import pytest

from vimm import AvailablePlatformScraper


@pytest.fixture
def scraper():
    return AvailablePlatformScraper()


class TestAvailablePlatformScraper:
    def test_platforms(self, scraper):
        platforms = scraper.platforms

        assert len(platforms) == 32
        assert platforms[0].name == "Atari 2600"
        assert platforms[-1].name == "PlayStation Portable"

    def test_consoles(self, scraper):
        pytest.skip()

    def test_handhelds(self, scraper):
        pytest.skip()
