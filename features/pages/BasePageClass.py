from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from features.pages.locators import BasePageLocators
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def load_page(self, url='', params=None):
        if params is None:
            self.driver.get(url)
        else:
            url_params = list(map(lambda x: "{}={}".format(x[0], x[1]), params.items()))
            self.driver.get(url + '&'.join(url_params))

    def get_element_by_css(self, locator, within_element=None):
        if within_element is None:
            context = self.driver
        else:
            context = within_element
        try:
            css_element = context.find_element(By.CSS_SELECTOR, locator)
        except NoSuchElementException:
            return None
        return css_element

    def get_element_by_id(self, id):
        try:
            element = self.driver.find_element_by_id(id)
        except NoSuchElementException:
            return None
        return element

    def get_element_list_by_css(self, locator, within_element=None):
        if within_element is None:
            context = self.driver
        else:
            context = within_element
        try:
            element_list = self.driver.find_elements_by_css_selector(locator)
        except NoSuchElementException:
            return []
        return element_list

    def wait_for_css_element(self, locator, timeout=60):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))

    def wait_for_element_clickable(self, locator, timeout=60):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))

    def is_login_popup_shown(self, timeout=60):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, BasePageLocators.LOGIN_POPUP)))
        except TimeoutException:
            return False
        else:
            return True

    def do_login(self, email, password):
        self.wait_for_css_element(BasePageLocators.LOGIN_POPUP)
        email_box = self.get_element_by_css(BasePageLocators.LOGIN_POPUP_EMAIL)
        password_box = self.get_element_by_css(BasePageLocators.LOGIN_POPUP_PASSWORD)
        login_button = self.get_element_by_css(BasePageLocators.LOGIN_POPUP_LOGIN_BUTTON)
        email_box.send_keys(email)
        password_box.send_keys(password)
        login_button.click()

    def get_profile_name(self):
        self.wait_for_css_element(BasePageLocators.PROFILE_AREA)
        return self.get_element_by_css(BasePageLocators.PROFILE_AREA).text

    def scroll_to(self, locator):
        self.wait_for_css_element(locator)
        web_element = self.get_element_by_css(locator)
        ActionChains(self.driver).move_to_element(web_element).perform()


