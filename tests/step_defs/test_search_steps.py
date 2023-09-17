"""
This module contains step definitions for search.feature
"""

import requests

from pytest_bdd import scenarios, parsers, given, then

SEARCH_API = 'http://api.duckduckgo.com/'

scenarios('../features/search.feature')

CONVERTERS = {
    'code': int,
    'phrase': str,
}


@given(
    parsers.parse('the Search API is queried with "{phrase}"'),
    target_fixture='search_response',
    converters=CONVERTERS
)
def search_response(phrase):
    params = {'q': phrase, 'format': 'json'}
    response = requests.get(SEARCH_API, params=params)
    return response


@then(
    parsers.parse('the response status code id "{code}"'),
    converters=CONVERTERS
)
def search_response_code(search_response, code):
    assert search_response.status_code == code


@then(
    parsers.parse('the response contains results for "{phrase}"'),
    converters=CONVERTERS
)
def search_response_content(search_response, phrase):
    assert phrase.lower() == search_response.json()['Heading'].lower()
