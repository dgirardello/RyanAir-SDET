@booking
Feature: Execute a flight booking booking, with an invalid payment at the end

  @flight_search @Page.MAIN
  Scenario: Search for a fight
    Given I'm on the RyanAir homepage
    And   I accept all the cookies if the Cookies Popup is shown in the Main page
    And   I check "Single Trip"
    And   I the flight's destination using
          | KEY     | VALUE     |
          | Country | Spain     |
          | Airport | Barcelona |
    And   I select a departure date for a Sunday 4 weeks from now
    When  I click on the Search button
    Then  The Trip page is shown
    And   The Trip page show at least 1 flight listed

  @flight_select @Page.TRIP @Section.FLIGHTS 
  Scenario: Select a flight and check that is added to the shop cart
    Given The Trip page is shown
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

  @flight_select_extras  @Page.TRIP @Section.EXTRAS
  Scenario: Finish booking a flight
    Given The Extras page is shown
    When  I click on the Extras "Continue" button
    Then  The Overview page is shown

  @flight_select_overview  @Page.TRIP @Section.OVERVIEW
  Scenario: Start Flight checkout
    Given The Overview page is shown
    When  I click on the Shopping cart icon
    And   I Click on the Checkout button
    Then  The Contact Details and Payment page is shown

  @flight_select_payment @error @invalid_card  @Page.PAYMENT
  Scenario: Set Insurance and payment options with an invalid credit card
    Given The Contact Details and Payment page is shown
    And   In the Insurance form I select "Insurance Plus"
    And   In the Payment page I scroll to Payment options
    And   In the payment form I type "1234 56789 012345" in the Card Number field
    And   In the payment form I select "July" in the Expiry Month dropdown
    And   In the payment form I select "2025" in the Expiry Year dropdown
    And   In the payment form I type "JOHN DOE" in the Cardholder Name field
    And   In the payment form I type "297" in the CVV field
    And   In the payment form I type "77 King Street N" in the Address Line 1 field
    And   In the payment form I type "Dublin" in the City field
    And   In the payment form I type "Ireland" in the Country field
    And   In the payment form I type "D01 TP22" in the Postcode field
    When  I accept the payment conditions
    And   I click on the Payment "Pay Now" button
    Then  In the Payment form an error is sown
    And   In the payment form the error message reads "Oops, something went wrong. Please check your payment details and try again"

