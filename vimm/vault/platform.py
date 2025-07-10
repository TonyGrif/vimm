"""Contains scraper pertaining to a single platform on Vimm"""

from dataclasses import dataclass
from typing import Optional, no_type_check

import httpx
from bs4 import BeautifulSoup


@dataclass
class StatusInfo:
    """Stores the status info of this platform"""

    contained_media: int
    total_media: int
    redump_date: str  # TODO: convert to datetime


@dataclass
class HomePage:
    """Stores information found on a platform's home page"""

    status: StatusInfo


class PlatformScraper:
    """Scrapes an available platform from Vimm's vault

    Attributes:
        home_page: the first page for each platform
    """

    def __init__(self, console: str) -> None:
        """Constructor for the PlatformScraper

        Args:
            console: identification of the console for the URL
        """
        self._console = console
        self._home_page: Optional[HomePage] = None

    @property
    def home_page(self) -> HomePage:
        """Return the home page information of this platform"""
        if self._home_page is not None:
            return self._home_page

        res = self._make_request(verify=False)
        self._home_page = self._parse_home_page(res)
        return self._home_page

    def _make_request(self, verify: bool = False) -> str:
        res = httpx.get(f"https://vimm.net/vault/{self._console}", verify=verify)
        res.raise_for_status()
        return res.text

    @no_type_check
    def _parse_home_page(self, res: str) -> HomePage:
        soup = BeautifulSoup(res, "html.parser")

        tables = soup.find_all("table")
        return HomePage(status=self._parse_status(tables[0]))

    @no_type_check
    def _parse_status(self, table) -> StatusInfo:
        rows = table.find_all("tr")
        status_numbers = [int(num) for num in rows[0].text.split() if num.isdigit()]
        redump = rows[1].text.partition(":")[2].strip()

        return StatusInfo(
            contained_media=status_numbers[0],
            total_media=status_numbers[1],
            redump_date=redump,
        )
