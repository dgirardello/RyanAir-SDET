from features.pages.BasePageClass import BasePage
from features.pages.locators import PaymentPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


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

