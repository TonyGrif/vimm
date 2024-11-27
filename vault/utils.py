"""This modules defines utility functions for the vault scraper"""

from string import ascii_uppercase as letters
from typing import List

import httpx
from bs4 import BeautifulSoup

URL = 'https://vimm.net/vault'


def request_vault(console) -> List[str]:
    """Make a request on the full vault

    Args:
        console: The console to scrape
    """
    result = []

    result.extend(request_number(console))
    for letter in letters:
        result.extend(request_letter(console, letter))

    return result


def request_letter(console: str, character: str) -> List[str]:
    """Make a request on a specific letter for a console

    Args:
        console: The console to scrape
        character: The letter to scrape
    """
    res = httpx.get(f'{URL}/{console}/{character}')
    soup = BeautifulSoup(res.text, 'html.parser')
    return _parse_table(soup)


def request_number(console: str) -> List[str]:
    """Make a request on the # vault page; requires different URL than letters

    Args:
        console: The console to scrape
    """
    res = httpx.get(f'{URL}/?p=list&system={console}&section=number')
    soup = BeautifulSoup(res.text, 'html.parser')
    return _parse_table(soup)


def _parse_table(soup: BeautifulSoup) -> List[str]:
    """Parse the soup for games"""
    titles = []
    for title in soup.find_all('td', {'style': 'width:auto'}):
        titles.append(title.find('a').text)
    return titles
