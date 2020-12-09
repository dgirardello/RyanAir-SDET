from features.pages.TripPageClass import TripPage
from features.pages.locators import TripPageLocators as TPL
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Extras(TripPage):

    def __init__(self, driver):
        TripPage.__init__(self, driver)

    def is_loaded(self):
        try:
            WebDriverWait(self.driver, 90).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, TPL.Extras.EXTRAS_LIST_CONTAINER)))
        except TimeoutException:
            return False
        else:
            return True

    def finish_booking(self):
        self.wait_for_css_element(TPL.Extras.BUTTON_CONTINUE)
        button_continue = self.get_element_by_css(TPL.Extras.BUTTON_CONTINUE)
        ActionChains(self.driver).move_to_element(button_continue).perform()
        button_continue.click()