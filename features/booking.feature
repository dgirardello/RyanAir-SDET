@booking
Feature: Execute a booking

  @flight_search @test
  Scenario: Search for a fight
    Given I'm on the RyanAir homepage
    And   I accept all the cookies if the Cookies Popup is shown
    And   I check "Single Trip"
    And   I the flight's destination using
          | KEY     | VALUE     |
          | Country | Spain     |
          | Airport | Barcelona |
    And   I select a departure date 30 days from now