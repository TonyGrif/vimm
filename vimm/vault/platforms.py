"""Contains scraper pertaining to the available platforms on Vimm"""

from dataclasses import dataclass
from typing import List, Optional, no_type_check

import httpx
from bs4 import BeautifulSoup


@dataclass
class Platform:
    """Information pertaining to the platform on Vimm"""

    name: str
    link: str
    year: int
    designation: str


class AvailablePlatformScraper:
    """Scrapes available platforms from Vimm's vault

    Attributes:
        platforms: all available platforms
        consoles: the available home consoles
        handhelds: the available handheld consoles
    """

    def __init__(self) -> None:
        """Constructor for the AvailablePlatformScraper

        Args:
            TBW
        """
        self._platforms: Optional[List[Platform]] = None
        self._consoles: List[Platform] = []
        self._handhelds: List[Platform] = []

    @property
    def platforms(self) -> List[Platform]:
        """Return all the available platform's on Vimm"""
        if self._platforms is not None:
            return self._platforms

        res = self._make_request(verify=False)
        self._platforms = self._parse_request(res)
        return self._platforms

    @property
    def consoles(self) -> List[Platform]:
        """Return all the home consoles available on Vimm"""
        return [value for value in self.platforms if value.designation == "Console"]

    @property
    def handhelds(self) -> List[Platform]:
        """Return all the handheld platforms on Vimm"""
        return [value for value in self.platforms if value.designation == "Handheld"]

    def _make_request(self, verify: bool = False) -> str:
        res = httpx.get("https://vimm.net/vault", verify=verify)
        res.raise_for_status()
        return res.text

    @no_type_check
    def _parse_request(self, res: str) -> List[Platform]:
        soup = BeautifulSoup(res, "html.parser")
        tables = soup.find_all("table")
        data = []

        for table in tables:
            entries = table.find_all("tr")
            for entry in entries:
                values = entry.find_all("td")
                data.append(
                    Platform(
                        name=values[0].find("a").text,
                        link=f"https://vimm.net{values[0].find('a')['href']}",
                        year=int(values[1].text),
                        designation=table.find("caption").text[:-1],
                    )
                )

        return data
