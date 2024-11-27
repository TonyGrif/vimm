#!/usr/bin/python3

"""This script gathers the available systems from vimm.net/vault in a python
list format for use in the main library.

Usage:
    python scripts/system.py
"""

from typing import List

import httpx
from bs4 import BeautifulSoup

VAULT_URL = 'https://vimm.net/vault'


def get_available_systems() -> List[str]:
    """Scrape the vault home page for systems"""
    response = httpx.get(VAULT_URL)
    return _parse(response.text)


def _parse(res: str) -> List[str]:
    """Find systems in HTTP response"""
    systems = []
    soup = BeautifulSoup(res, 'html.parser')

    for elem in soup.find_all('td'):
        if anchor := elem.find('a'):
            idx = anchor['href'].rfind('/')
            systems.append(anchor['href'][idx + 1 :])

    return systems


if __name__ == '__main__':
    print(get_available_systems())
