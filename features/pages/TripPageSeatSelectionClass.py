from features.pages.TripPageClass import TripPage
from features.pages.locators import TripPageLocators as TPL
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class SeatSelection(TripPage):

    def __init__(self, driver):
        TripPage.__init__(self, driver)

    def is_loaded(self):
        try:
            WebDriverWait(self.driver, 90).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, TPL.SeatSelection.SEAT_MAP_CONTAINER)))
        except TimeoutException:
            return False
        else:
            return True

    def select_first_available_seat(self, priority=False):
        if priority:
            locator = TPL.SeatSelection.LIST_BUTTON_SEAT_PRIORITY
        else:
            locator = TPL.SeatSelection.LIST_BUTTON_SEAT_STANDARD

        self.wait_for_css_element(locator)
        seat_button_list = self.get_element_list_by_css(locator)
        seat_button_list[0].click()

    def hover_over_seat(self, seat_element):
        ActionChains(self.driver).move_to_element(seat_element).perform()
        self.wait_for_css_element(TPL.SeatSelection.SEAT_TOOLTIP_DESIGNATOR)

    def get_selected_seat_location(self):
        self.wait_for_css_element(TPL.SeatSelection.BUTTON_SEAT_SELECTED)
        selected_seat_button = self.get_element_by_css(TPL.SeatSelection.BUTTON_SEAT_SELECTED)
        self.hover_over_seat(selected_seat_button)
        return self.get_element_by_css(TPL.SeatSelection.SEAT_TOOLTIP_DESIGNATOR).text

    def is_seat_selected(self):
        plane_seat = self.get_element_by_css(TPL.SeatSelection.BUTTON_SEAT_SELECTED)
        panel_seat = self.get_element_by_css(TPL.SeatSelection.RIGHT_PANEL_SEAT_SELECTED)
        return plane_seat is not None and panel_seat is not None

    def get_panel_seat_text(self):
        return self.get_element_by_css(TPL.SeatSelection.RIGHT_PANEL_SEAT_SELECTED).text

    def continue_to_bags(self):
        self.wait_for_css_element(TPL.SeatSelection.BUTTON_CONTINUE)
        self.get_element_by_css(TPL.SeatSelection.BUTTON_CONTINUE).click()