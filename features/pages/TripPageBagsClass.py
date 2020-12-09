from features.pages.TripPageClass import TripPage
from features.pages.locators import TripPageLocators as TPL
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Bags(TripPage):

    def __init__(self, driver):
        TripPage.__init__(self, driver)

    def is_loaded(self):
        try:
            WebDriverWait(self.driver, 90).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, TPL.BagsSelection.BAGS_CARD_CONTAINER)))
        except TimeoutException:
            return False
        else:
            return True

    def continue_to_extras(self):
        self.scroll_to(TPL.BagsSelection.BUTTON_CONTINUE)
        self.wait_for_css_element(TPL.BagsSelection.BUTTON_CONTINUE)
        button_continue = self.get_element_by_css(TPL.BagsSelection.BUTTON_CONTINUE)
        button_continue.click()