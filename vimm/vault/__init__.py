"""This module contains scrapers pertaining to Vimm's vault"""

from .platform import PlatformScraper
from .platforms import AvailablePlatformScraper

__all__ = ["AvailablePlatformScraper", "PlatformScraper"]
