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
        consoles = scraper.consoles

        assert len(consoles) == 24
        assert consoles[13].name == "PlayStation"
        assert consoles[13].year == 1994
        assert consoles[13].link is not None
        assert consoles[13].designation == "Console"

    def test_handhelds(self, scraper):
        pytest.skip()
