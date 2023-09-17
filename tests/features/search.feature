Feature: Search Instant Answer API
  As an application developer,
  I want to get instant answer for search phrase via REST API,
  So that my app can get answers.


  Scenario Outline: Basic Search API Query
    Given the Search API is queried with "<phrase>"
    Then the response status code id "200"
    Then the response contains results for "<phrase>"

    Examples: Principles of OOP
    | phrase        |
    | Abstraction   |
    | Inheritance   |
    | Polymorphism  |
    | Encapsulation |
