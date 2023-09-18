"""
This module contains steps definitions for search_ui.feature
"""

from pytest_bdd import scenarios, parsers, given, when, then

from pages.search import SearchPage
from pages.results import SearchResultsPage


scenarios('../features/search_ui.feature')


@when(parsers.parse('the user searches for "{phrase}"'))
@when(parsers.parse('the user searches for the long phrase:\n{phrase}'))
def search_phrase(browser, phrase):
    search_page = SearchPage(browser)
    search_page.search(phrase)


@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(browser, phrase):
    result_page = SearchResultsPage(browser)
    assert len(result_page.result_link_titles(phrase)) > 0
    assert result_page.search_input_value() == phrase


@then(parsers.parse('one of the results contains "{phrase}"'))
def results_have_one(browser, phrase):
    result_page = SearchResultsPage(browser)
    assert len(result_page.result_link_titles(phrase)) > 0
