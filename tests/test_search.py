"""
These tests cover DuckDuckGo searches.
"""

import pytest

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
def test_basic_duckduckgo_search(browser, phrase):
  search_page = DuckDuckGoSearchPage(browser)
  result_page = DuckDuckGoResultPage(browser)
  
  # Given the DuckDuckGo home page is displayed
  search_page.load()

  # When the user searches for the phrase
  search_page.search(phrase)

  # Then the search result query is the phrase
  assert phrase == result_page.search_input_value()
  
  # And the search result links pertain to the phrase
  for title in result_page.result_link_titles():
    assert phrase.lower() in title.lower()

  # And the search result title contains the phrase
  # (Putting this assertion last guarantees that the page title will be ready)
  assert phrase in result_page.title()
