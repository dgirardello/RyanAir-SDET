from features.pages.TripPageClass import TripPage
from features.pages.locators import TripPageLocators as TPL
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class FlightSelection(TripPage):
    
    def __init__(self, driver):
        TripPage.__init__(self, driver)
        
    def get_flights(self):
        return self.get_element_list_by_css(TPL.FlightSelection.FLIGHT_LIST_ITEMS)

    def select_first_flight(self):
        self.wait_for_css_element(TPL.FlightSelection.FLIGHT_LIST_ITEMS)
        flight_cards = self.get_element_list_by_css(TPL.FlightSelection.FLIGHT_LIST_ITEMS)
        flight_cards[0].click()

    def get_fare_card(self, fare):
        if str(fare).upper() in ['REGULAR']:
            locator = TPL.FlightSelection.FARE_CARD_REGULAR
        elif str(fare).upper() in ['PLUS']:
            locator = TPL.FlightSelection.FARE_CARD_PLUS
        elif str(fare).upper() in ['FLEXI PLUS']:
            locator = TPL.FlightSelection.FARE_CARD_FLEXI
        else:
            locator = TPL.FlightSelection.FARE_CARD_STANDARD

        self.wait_for_css_element(locator)
        return self.get_element_by_css(locator)

    def select_flight_fare(self, fare):
        fare_card = self.get_fare_card(fare)
        fare_card_button = self.get_element_by_css('button', within_element=fare_card)
        fare_card_button.click()

    def is_login_section_shown(self, timeout=60):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, TPL.FlightSelection.LOGIN_BOX)))
        except TimeoutException:
            return False
        else:
            return True

    def click_login_element(self, button):
        self.scroll_to(TPL.FlightSelection.LOGIN_BOX)
        if 'LOGIN' in str(button).upper():
            locator = TPL.FlightSelection.LOGIN_BOX_LOGIN_BUTTON
        elif 'LOG IN LATER':
            locator = TPL.FlightSelection.LOGIN_BOX_LOGIN_LATER_LINK
        self.get_element_by_css(locator).click()
        
    def get_passenger_subsection(self, inner_div=False):
        self.scroll_to(TPL.FlightSelection.PASSENGERS_SECTION_CONTAINER)
        return_element = self.get_element_by_css(TPL.FlightSelection.PASSENGERS_SECTION_CONTAINER)
        if inner_div:
            return_element = self.get_element_by_css(TPL.FlightSelection.PASSENGERS_SECTION_CONTAINER_INNER_DIV,
                                                     within_element=return_element)
        return return_element

    def select_first_companion(self):
        self.wait_for_css_element(TPL.FlightSelection.PASSENGERS_SECTION_SAVED_COMPANION_BUTTON)
        passenger_section = self.get_element_by_css(TPL.FlightSelection.PASSENGERS_SECTION_CONTAINER)
        companion_button_list = self.get_element_list_by_css(TPL.FlightSelection.PASSENGERS_SECTION_SAVED_COMPANION_BUTTON,
                                                             within_element=passenger_section)
        companion_button_list[0].click()

    def get_passenger_field_text(self, field):
        use_text = False
        if 'TITLE' in str(field).upper():
            locator = TPL.FlightSelection.PASSENGERS_SECTION_TITLE_BOX
            use_text = True
        elif 'FIRST NAME' in str(field).upper():
            locator = TPL.FlightSelection.PASSENGERS_SECTION_FIRST_NAME_BOX
        elif 'LAST NAME' in str(field).upper():
            locator = TPL.FlightSelection.PASSENGERS_SECTION_LAST_NAME_BOX
        else:
            raise Exception("Unknown Passenger field {}".format(field))

        self.wait_for_css_element(locator)
        if use_text:
            return_text = self.get_element_by_css(locator).text
        else:
            return_text = self.get_element_by_css(locator).get_attribute('value')
        return return_text

    def continue_to_seat_selection(self):
        self.wait_for_css_element(TPL.FlightSelection.PASSENGERS_SECTION_CONTINUE_BUTTON)
        continue_button = self.get_element_by_css(TPL.FlightSelection.PASSENGERS_SECTION_CONTINUE_BUTTON)
        continue_button.click()





