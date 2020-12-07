from features.pages.TripPageClass import TripPage
from features.pages.locators import TripPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class SectionFlights(TripPage):
    
    def __init__(self, driver):
        TripPage.__init__(self, driver)
        
    def get_flights(self):
        return self.get_elements_by_css(TripPageLocators.SectionFlights.FLIGHT_LIST_ITEMS)

    def select_first_flight(self):
        self.wait_for_css_element(TripPageLocators.SectionFlights.FLIGHT_LIST_ITEMS)
        flight_cards = self.get_elements_by_css(TripPageLocators.SectionFlights.FLIGHT_LIST_ITEMS)
        flight_cards[0].click()

    def get_fare_card(self, fare):
        if str(fare).upper() in ['REGULAR']:
            locator = TripPageLocators.SectionFlights.FARE_CARD_REGULAR
        elif str(fare).upper() in ['PLUS']:
            locator = TripPageLocators.SectionFlights.FARE_CARD_PLUS
        elif str(fare).upper() in ['FLEXI PLUS']:
            locator = TripPageLocators.SectionFlights.FARE_CARD_FLEXI
        else:
            locator = TripPageLocators.SectionFlights.FARE_CARD_STANDARD

        self.wait_for_css_element(locator)
        return self.get_element_by_css(locator)

    def select_flight_fare(self, fare):
        fare_card = self.get_fare_card(fare)
        fare_card_button = self.get_element_by_css('button', within_element=fare_card)
        fare_card_button.click()

    def is_login_shown(self, timeout=60):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, TripPageLocators.SectionFlights.LOGIN_BOX)))
        except TimeoutException:
            return False
        else:
            return True