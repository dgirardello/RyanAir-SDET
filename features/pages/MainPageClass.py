from features.pages.BasePageClass import BasePage
from features.pages.locators import MainPageLocators
from selenium.common.exceptions import StaleElementReferenceException
import time


class MainPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def load_page(self):
        BasePage.load_page(self, 'https://www.ryanair.com/ie/en')

    def accept_all_cookies(self):
        if self.get_element_by_css(MainPageLocators.COOKIE_POPUP) is not None:
            btn_accept_cookies = self.get_element_by_css(MainPageLocators.ACCEPT_ALL_COOKIES)
            btn_accept_cookies.click()

    def select_trip_type(self, round_trip=True):
        if round_trip:
            btn_trip_type = self.get_element_by_css(MainPageLocators.RETURN_TRIP)
        else:
            btn_trip_type = self.get_element_by_css(MainPageLocators.SINGLE_TRIP)
        btn_trip_type.click()

    def get_location_selector(self, origin=True):
        if origin:
            locator = MainPageLocators.TEXTBOX_DEPARTURE_ID
        else:
            locator = MainPageLocators.TEXTBOX_DESTINATION_ID
        return locator

    def type_city(self, text, origin=True):
        text_box = self.get_location_selector(origin=origin)
        text_box.send_keys(str(text).capitalize())

    def show_destinations(self, origin=True):
        text_box_locator = self.get_location_selector(origin=origin)
        text_box = self.get_element_by_id(text_box_locator)
        text_box.click()

    def clear_destination_selection(self):
        clear_selection_button = self.get_element_by_css(MainPageLocators.BUTTON_CLEAR_DESTINATION)
        clear_selection_button.click()

    def select_country(self, country, origin=True):
        self.wait_for_css_element(MainPageLocators.FLIGHT_COUNTRIES_CONTAINER)
        selected_country = [x for x in self.get_element_list_by_css(MainPageLocators.FLIGHT_COUNTRIES)
                            if str(x.text).upper() in str(country).upper()][0]
        selected_country.click()

    def select_airport(self, airport, origin=True):
        self.wait_for_css_element(MainPageLocators.FLIGHT_AIRPORTS_CONTAINER)
        selected_airport = [x for x in self.get_element_list_by_css(MainPageLocators.FLIGHT_AIRPORTS)
                            if str(x.text).upper() in str(airport).upper()][0]
        selected_airport.click()

    def get_departure_selector(self, departure=True):
        if departure:
            locator = MainPageLocators.TEXTBOX_DEPARTURE_CALENDAR
        else:
            locator = MainPageLocators.TEXTBOX_DESTINATION_CALENDAR
        self.wait_for_css_element(locator)
        return self.get_element_by_css(locator)

    def open_calendar(self, departure=True):
        self.get_departure_selector(departure=departure).click()

    def set_date(self, date, departure=True):
        self.open_calendar(departure=departure)
        locator = MainPageLocators.DEPARTURE_CALENDAR_DATE.format(date)
        self.wait_for_element_clickable(locator)
        self.get_element_by_css(locator).click()

    def search_flight(self):
        self.get_element_by_css(MainPageLocators.SEARCH_BUTTON).click()
