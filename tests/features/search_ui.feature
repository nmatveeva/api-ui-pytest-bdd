Feature: Search Web Browsing
  As a web user,
  I want to find information.

  Background:
    Given the Search home page is displayed


  Scenario: Basic Web Search
    When the user searches for "Python"
    Then results are shown for "Python"


  Scenario: Phrase Web Search
    When the user searches for the long phrase:
      """
      Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.
      """
    Then one of the results contains "About Python™ | Python.org"
