import pytest
from pytest_bdd import given
from selenium import webdriver

from pages.search import SearchPage


# Hooks

def pytest_bdd_step_error(step):
    print(f'Step failed: {step}')


# Fixtures

@pytest.fixture
def browser():
    b = webdriver.Firefox()
    b.implicitly_wait(10)
    yield b
    b.quit()


@given('the Search home page is displayed')
def search_home(browser):
    search_page = SearchPage(browser)
    search_page.load()
