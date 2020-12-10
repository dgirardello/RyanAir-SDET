from features.pages.BasePageClass import BasePage
from features.pages.locators import PaymentPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import re

class PaymentPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def is_loaded(self):
        try:
            WebDriverWait(self.driver, 90).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, PaymentPageLocators.PAYMENT_CONTAINER)))
        except TimeoutException:
            return False
        else:
            return True

    def select_insurance(self, insurance=''):
        self.wait_for_css_element(PaymentPageLocators.INSURANCE_CONTAINER)
        if 'PLUS' in str(insurance).upper():
            locator = PaymentPageLocators.INSURANCE_PLUS_CHECK
        else:
            locator = PaymentPageLocators.INSURANCE_NO_CHECK
        self.get_element_by_css(locator).click()

    def go_to(self, section):
        if 'PAYMENT' in str(section):
            locator = PaymentPageLocators.PAYMENT_CONTAINER
        else:
            locator = PaymentPageLocators.CONTACT_DETAILS_CONTAINER
        self.scroll_to(locator)

    def type_in_textbox(self, textbox_container, text):
        self.wait_for_css_element(textbox_container)
        container_element = self.get_element_by_css(textbox_container)
        textbox_element = self.get_element_by_css(PaymentPageLocators.PAYMENT_INPUT,
                                                  within_element=container_element)
        textbox_element.send_keys(str(text))

    def payment_type_and_select_country(self, country):
        self.wait_for_css_element(PaymentPageLocators.PAYMENT_CARD_ADDRESS_COUNTRY_CONTAINER)
        container_element = self.get_element_by_css(PaymentPageLocators.PAYMENT_CARD_ADDRESS_COUNTRY_CONTAINER)
        textbox_element = self.get_element_by_css(PaymentPageLocators.PAYMENT_INPUT,
                                                  within_element=container_element)
        textbox_element.click()
        for key in country:
            textbox_element.send_keys(key)
            sleep(1)
        textbox_element.send_keys(Keys.ENTER)


    def type_in_field(self, field, text):
        if re.search(r'Card Number', field, re.IGNORECASE):
            self.type_in_textbox(PaymentPageLocators.PAYMENT_CARD_NUMBER_CONTAINER,
                                 text)
        elif re.search(r'Cardholder Name', field, re.IGNORECASE):
            self.type_in_textbox(PaymentPageLocators.PAYMENT_CARD_NAME_CONTAINER,
                                 text)
        elif re.search(r'CVV', field, re.IGNORECASE):
            self.type_in_textbox(PaymentPageLocators.PAYMENT_CARD_CVV_CONTAINER,
                                 text)
        elif re.search(r'Address Line 1', field, re.IGNORECASE):
            self.type_in_textbox(PaymentPageLocators.PAYMENT_CARD_ADDRESS_LINE1_CONTAINER,
                                 text)
        elif re.search(r'City', field, re.IGNORECASE):
            self.type_in_textbox(PaymentPageLocators.PAYMENT_CARD_ADDRESS_CITY_CONTAINER,
                                 text)
        elif re.search(r'Country', field, re.IGNORECASE):
            self.payment_type_and_select_country(str(text))
        elif re.search(r'Postcode', field, re.IGNORECASE):
            self.type_in_textbox(PaymentPageLocators.PAYMENT_CARD_ADDRESS_POSTCODE_CONTAINER,
                                 text)
        else:
            raise Exception('Unknown field {} in Paymnet Page'.format(field))

    def select_dropdown_item(self, dropdown_container, text):
        self.get_element_by_css(PaymentPageLocators.DROPDOWN_BUTTON,
                                within_element=dropdown_container).click()
        options_list = self.get_element_list_by_css(PaymentPageLocators.DROPDOWN_ITEMS,
                                                    within_element=dropdown_container)
        for option in options_list:
            if re.search(option.text, text, re.IGNORECASE):
                option.click()
                break

    def set_dropdown_date(self, month=None, year=None):
        self.wait_for_css_element(PaymentPageLocators.PAYMENT_CARD_EXPIRE_CONTAINER)
        expiry_date_container = self.get_element_by_css(PaymentPageLocators.PAYMENT_CARD_EXPIRE_CONTAINER)
        dropdown_month, dropdown_year = self.get_element_list_by_css(PaymentPageLocators.DROPDOWN_CONTAINER,
                                                                     within_element=expiry_date_container)
        if month is not None:
            self.select_dropdown_item(dropdown_month, month)

        if year is not None:
            self.select_dropdown_item(dropdown_year, year)

    def accept_terms(self):
        self.get_element_by_css(PaymentPageLocators.PAYMENT_ACCEPT_CONDITIONS).click()

    def pay_now(self):
        self.wait_for_css_element(PaymentPageLocators.PAYMENT_PAY_NOW_BUTTON)
        self.get_element_by_css(PaymentPageLocators.PAYMENT_PAY_NOW_BUTTON).click()

    def is_error_present(self):
        try:
            WebDriverWait(self.driver, 90).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, PaymentPageLocators.PAYMENT_ERROR_CONTAINER)))
        except TimeoutException:
            return False
        else:
            return True

    def get_error_message(self):
        self.wait_for_css_element(PaymentPageLocators.PAYMENT_ERROR_CONTAINER)
        return self.get_element_by_css(PaymentPageLocators.PAYMENT_ERROR_CONTAINER).text
