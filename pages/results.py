"""
This module contains the DuckDuckGo search results page.
"""

from selenium.webdriver.common.by import By


class SearchResultsPage:

    RESULT = '[@data-testid="result"]'
    RESULT_LINKS = (By.CSS_SELECTOR, RESULT)
    SEARCH_INPUT = (By.NAME, 'q')

    def __init__(self, browser):
        self.browser = browser

    def title(self):
        return self.browser.title

    def result_link_titles(self, phrase):
        xpath = f"//*{self.RESULT}//*[contains(text(), '%s')]" % phrase
        links = self.browser.find_elements(By.XPATH, xpath)
        titles = [link.text for link in links]
        return titles

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        return search_input.get_attribute('value')
