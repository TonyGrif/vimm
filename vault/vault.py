"""This module defines the vault class for scraping vimm.net/vault data."""

from typing import List

from .systems import SYSTEMS
from .utils import request_vault


class Vault:
    """This class defines the scraper for vaults on vimm.net

    Attributes:
        console: The game console for this vault
    """

    def __init__(
        self, console: str, validate: bool = True, auto_scrape: bool = False
    ) -> None:
        """Constructor for the Vault object

        Args:
            console: The game console to be scraped for
            validate: Whether or not to validate console on init
            auto_scrape: Whether of not to automatically request vault data
        """
        if validate and self._validate_console(console) is False:
            raise ValueError('Invalid console passed; check SYSTEMS for availability')

        self.console = console
        self.entries: List[str] = []

        if auto_scrape:
            self.request()

    def _validate_console(self, console: str) -> bool:
        """Validate if the console is included in vimm.net vault

        Args:
            console: The game console to validate
        """
        if console not in SYSTEMS:
            return False
        return True

    def request(self) -> None:
        """Make HTTP request on this objects' console vault"""
        self.entries = request_vault(self.console)

    def get_result_by_letter(self) -> None:
        """TBW"""
        return
