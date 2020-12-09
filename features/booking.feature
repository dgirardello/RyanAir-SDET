@booking
Feature: Execute a booking

#  @flight_search @Page.MAIN @wip
#  Scenario: Search for a fight
#    Given I'm on the RyanAir homepage
#    And   I accept all the cookies if the Cookies Popup is shown
#    And   I check "Single Trip"
#    And   I the flight's destination using
#          | KEY     | VALUE     |
#          | Country | Spain     |
#          | Airport | Barcelona |
#    And   I select a departure date for a Sunday 4 weeks from now
#    When  I click on the Search button
#    And   I wait until the Trip page is loaded
#    Then  The page tile is "Ryanair"
#    And   The Trip page show at least 1 flight listed

  @flight_select @Page.TRIP @Section.FLIGHTS 
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

  @flight_select_login  @Page.TRIP @Section.FLIGHTS 
  Scenario: Login to continue with the booking
    Given The Login sub-section is shown
    And   I click on the "Login" button within the "Login" sub-section
    And   The login popup is shown
    When  I input a valid credentials and click on Login
    Then  The Profile Name is shown in the top bar with the name "John"
    And   The Passengers sub-section is enabled

  @flight_select_passenger  @Page.TRIP @Section.FLIGHTS 
  Scenario: Add a passenger information
    Given The Passengers sub-section is enabled
    When  I click on the first Saved Companion
    And   The passenger fields are populated with
          | FIELD      | VALUE |
          | Title      | Mr    |
          | First Name | John  |
          | Last Name  | Doe   |
    And   I click on the "Continue" button within the "Passengers" sub-section
    Then  The Seat Selection page is shown
    
  @flight_select_seat  @Page.TRIP @Section.SEATS
  Scenario: Select a priority seat
    Given The Seat Selection page is shown
    When  I click on the first sear available in the "Priority" section
    Then  The seat is selected
    And   The selected seat location matches the seat shown in the right panel

  @flight_select_seat  @Page.TRIP @Section.SEATS
  Scenario: Continue to Bags
    Given The seat is selected
    When  I click on the Seat Selection "Continue" button
    Then  The Bags page is shown

  @flight_select_bags  @Page.TRIP @Section.BAGS
  Scenario: Continue to Extras
    Given The Bags page is shown
    When  I click on the Bags "Continue" button
    Then  The Extras page is shown

  @flight_select_bags  @Page.TRIP @Section.EXTRAS
  Scenario: Finish booking a flight
    Given The Extras page is shown
    When  I click on the Extras "Continue" button
    Then  The Overview page is shown

  @flight_select_bags  @Page.TRIP @Section.OVERVIEW
  Scenario: Start Flight checkout
    Given The Overview page is shown
    When  I click on the Shopping cart icon
    And   I Click on the Checkout button
    Then  The Contact Details and Payment page is shown
