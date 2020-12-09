from features.pages.TripPageClass import TripPage
from features.pages.locators import TripPageLocators as TPL
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class OverviewSection(TripPage):

    def __init__(self, driver):
        TripPage.__init__(self, driver)

    def is_loaded(self):
        try:
            WebDriverWait(self.driver, 90).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, TPL.OverviewSection.PILLARS_CONTAINER)))
        except TimeoutException:
            return False
        else:
            return True


