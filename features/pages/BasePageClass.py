from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


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

    def get_elements_by_css(self, locator, within_element=None):
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

