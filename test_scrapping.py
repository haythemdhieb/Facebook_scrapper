import pytest
import sys
import os

sys.path.insert(0, os.getcwd())

from scrapper import Scrapper


def test_scrapping():
    """
    Function that will test if the data was scrapped successfully
    """
    scrapper = Scrapper()
    scrapped_data = scrapper.scrape_fb_page("nous.sommes.les.ingenieurs", 5)
    assert len(scrapped_data) > 0
    assert len(scrapped_data[0]["text"]) > 0
