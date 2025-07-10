import pytest

from vimm import PlatformScraper


@pytest.fixture
def scraper():
    return PlatformScraper("PS1")


class TestPlatformScraperHomePage:
    def test_home_stats(self, scraper):
        home = scraper.home_page

        assert home.status.contained_media == 10862
        assert home.status.total_media == 10862
        assert home.status.redump_date == "2025-07-10"
