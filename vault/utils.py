"""This modules defines utility functions for the vault scraper"""

from typing import List

import httpx
from bs4 import BeautifulSoup

URL = 'https://vimm.net/vault'


def request_vault() -> None:
    """Make a request on the full vault

    Args:
        console: The console to scrape
    """
    return


def request_letter(console: str, character: str) -> List[str]:
    """Make a request on a specific letter for a console

    Args:
        console: The console to scrape
        character: The letter to scrape
    """
    res = httpx.get(f'{URL}/{console}/{character}')

    soup = BeautifulSoup(res.text, 'html.parser')

    titles = []
    for title in soup.find_all('td', {'style': 'width:auto'}):
        titles.append(title.find('a').text)

    return titles
