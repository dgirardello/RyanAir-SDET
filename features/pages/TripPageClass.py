from features.pages.BasePageClass import BasePage
from features.pages.locators import TripPageLocators

class TripPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def load_page(self, date_out='', date_in='', origin='', destination='', adults=0, teens=0, children=0 ):
        params = {
            'adults': int(adults),
            'teens': int(teens),
            'children': int(children),
            'infants': 0,
            'dateOut': str(date_out),
            'dateIn': str(date_in),
            'isConnectedFlight': 'false',
            'isReturn': 'false',
            'discount': 0,
            'promoCode': '',
            'originIata': str(origin),
            'destinationIata': str(destination),
            'tpAdults': int(adults),
            'tpTeens': int(teens),
            'tpChildren': int(children),
            'tpInfants': 0,
            'tpStartDate': str(date_out),
            'tpEndDate': str(date_in),
            'tpDiscount': 0,
            'tpPromoCode': '',
            'tpOriginIata': str(origin),
            'tpDestinationIata': str(destination)
        }
        BasePage.load_page(self, url='https://www.ryanair.com/ie/en/trip/flights/select?', params=params)

    def wait_for_page_load(self, timeout=300):
        self.wait_for_css_element(TripPageLocators.DATE_CAROUSEL_CONTAINER, timeout=timeout)
        self.wait_for_css_element(TripPageLocators.FLIGHT_LIST_CONTAINER, timeout=timeout)

    def get_flights(self):
        return self.get_elements_by_css(TripPageLocators.FLIGHT_LIST_ITEMS)

    def select_first_flight(self):
        flight_cards = self.get_elements_by_css(TripPageLocators.FLIGHT_LIST_ITEMS)
        flight_cards[0].click()

    def get_fare_card(self, fare):
        if str(fare).upper() in ['REGULAR']:
            locator = TripPageLocators.FARE_CARD_REGULAR
        elif str(fare).upper() in ['PLUS']:
            locator = TripPageLocators.FARE_CARD_PLUS
        elif str(fare).upper() in ['FLEXI PLUS']:
            locator = TripPageLocators.FARE_CARD_FLEXI
        else:
            locator = TripPageLocators.FARE_CARD_STANDARD

        self.wait_for_css_element(locator)
        return self.get_elements_by_css(locator)

    def select_flight_fare(self, fare):
        fare_card = self.get_fare_card(fare)
        fare_card_button = self.get_element_by_css('button', within_element=fare_card)
        fare_card_button.click()
        pass