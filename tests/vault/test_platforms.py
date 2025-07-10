import pytest

from vimm import AvailablePlatformScraper


@pytest.fixture
def scraper():
    return AvailablePlatformScraper()


class TestAvailablePlatformScraper:
    def test_platforms(self, scraper):
        platforms = scraper.platforms

        assert len(platforms) == 33
        assert platforms[0].name == "Atari 2600"
        assert platforms[-1].name == "Nintendo 3DS"

    def test_consoles(self, scraper):
        consoles = scraper.consoles

        assert len(consoles) == 24
        assert consoles[13].name == "PlayStation"
        assert consoles[13].year == 1994
        assert consoles[13].link is not None
        assert consoles[13].designation == "Console"

    def test_handhelds(self, scraper):
        handhelds = scraper.handhelds

        assert len(handhelds) == 9
        assert handhelds[4].name == "Game Boy Color"
        assert handhelds[4].year == 1998
        assert handhelds[4].link is not None
        assert handhelds[4].designation == "Handheld"
