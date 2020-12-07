@booking
Feature: Execute a booking

  @flight_search @wip
  Scenario: Search for a fight
    Given I'm on the RyanAir homepage
    And   I accept all the cookies if the Cookies Popup is shown
    And   I check "Single Trip"
    And   I the flight's destination using
          | KEY     | VALUE     |
          | Country | Spain     |
          | Airport | Barcelona |
    And   I select a departure date for a Sunday 4 weeks from now
    When  I click on the Search button
    And   I wait until the Trip page is loaded
    Then  The page tile is "Ryanair"
    And   The Trip page show at least 1 flight listed

  @flight_select @test
  Scenario: Select a flight and check that is added to the shop cart
    Given I'm in the Tip page Flight section with a flight search with
          | PARAMETER   | VALUE             |
          | ORIGIN      | DUB               |
          | DESTINATION | BCN               |
          | ADULTS      | 1                 |
          | DATE        | 4 Weeks from now  |
          | WEEKDAY     | Sunday            |
    And   I accept all the cookies if the Cookies Popup is shown
    When  I select the first flight available
    And   I select the "Flexi Plus" fare
    Then  The total amount beside the shopping cart is greater than 0
    And   The Login sub-section is shown
