from features.pages.BasePageClass import BasePage
from features.pages.locators import TripPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


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

    def accept_all_cookies(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, TripPageLocators.COOKIE_POPUP)))

            btn_accept_cookies = self.get_element_by_css(TripPageLocators.ACCEPT_ALL_COOKIES)
            btn_accept_cookies.click()
        except:
            pass

    def get_shopping_amount(self):
        self.wait_for_css_element(TripPageLocators.SHOPPING_CART_AMOUNT_INT)
        int_part = self.get_element_by_css(TripPageLocators.SHOPPING_CART_AMOUNT_INT).text
        dec_part = self.get_element_by_css(TripPageLocators.SHOPPING_CART_AMOUNT_DEC).text
        return float(".".join(map(str, [int_part, dec_part])))

    def show_cart_details(self):
        self.wait_for_css_element(TripPageLocators.SHOPPING_CART_BUTTON)
        self.get_element_by_css(TripPageLocators.SHOPPING_CART_BUTTON).click()

    def do_checkout(self):
        self.wait_for_css_element(TripPageLocators.SHOPPING_CART_DETAILS_CONTAINER)
        self.wait_for_css_element(TripPageLocators.SHOPPING_CART_DETAILS_CHECKOUT_BUTTON)
        self.get_element_by_css(TripPageLocators.SHOPPING_CART_DETAILS_CHECKOUT_BUTTON).click()









