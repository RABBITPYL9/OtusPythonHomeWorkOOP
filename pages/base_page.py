import allure
from urllib.parse import urljoin
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import LoginPageLocators
from constants import IMPLICIT_WAIT, EXPLICIT_WAIT, BASE_URL
from selenium.webdriver.common.by import By


class BasePage():
    _base_url = BASE_URL
    _base_path = None

    def __init__(self, i_browser, i_url: str, i_timeout=IMPLICIT_WAIT):
        self._browser = i_browser
        self.url = i_url
        self._browser.implicitly_wait(i_timeout)

    def is_element_present(self, i_how: str, i_what: str) -> bool:
        with allure.step(f'Element with locator: "{i_how} {i_what}" is present'):
            try:
                self._browser.find_element(i_how, i_what)
            except NoSuchElementException:
                return False
            return True

    def click(self, i_how: str, i_what: str) -> bool:
        with allure.step(f'Click on element with locator: "{i_how} {i_what}"'):
            try:
                self._browser.find_element(i_how, i_what).click()
            except ElementNotInteractableException:
                return False
            return True
    
    def clear(self, i_how: str, i_what: str) -> bool:
        with allure.step(f'Clear on element with locator: "{i_how} {i_what}"'):
            try:
                self._browser.find_element(i_how, i_what).clear()
            except ElementNotInteractableException:
                return False
            return True

    def write_field(self, i_how: str, i_what: str, i_keys: str) -> bool:
        with allure.step(f'Write "{i_keys}" in field with locator: "{i_how} {i_what}"'):
            try:
                self._browser.find_element(i_how, i_what).send_keys(i_keys)
            except ElementNotInteractableException:
                return False
            return True

    def open(self):
        url = urljoin(self._base_url, self._base_path)
        with allure.step(f'open{url}'):
            self._browser.get(self.url)


    def is_not_element_present(self, i_how: str, i_what: str, i_timeout=EXPLICIT_WAIT) -> bool:
        with allure.step(f'Element with locator: "{i_how} {i_what}"is not presented'):
            try:
                WebDriverWait(self._browser, i_timeout).until(EC.presence_of_element_located((i_how, i_what)))
            except TimeoutException:
                return True

    def is_disappeared(self, i_how: str, i_what: str, i_timeout=EXPLICIT_WAIT) -> bool:
        try:
            WebDriverWait(self._browser, i_timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((i_how, i_what)))
        except TimeoutException:
            raise AssertionError(f'Element with locator: {i_how} {i_what} is visible!')
        return True

    def find_element_presence(self, locator,time=10):
        return WebDriverWait(self._browser,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_element(self, i_how: str, i_what: str) -> WebElement:
        try:
            element = self._browser.find_element(i_how, i_what)
            return element
        except NoSuchElementException:
            raise AssertionError(f'Element with locator: {i_how} {i_what} is not found!')

     
    def find_text(self, i_how: str, i_what: str) -> WebElement:
        try:
            element = self._browser.find_element(i_how, i_what)
            return element
        except NoSuchElementException:
            raise AssertionError(f'Text with locator: {i_how} {i_what} is not found!')

    
    def is_text_present(self, i_how: str, i_what: str, i_expected: str) -> WebElement:
        try:
            element = self._browser.find_element(i_how, i_what).text
            assert element == i_expected
            return element
        except NoSuchElementException:
            raise AssertionError(f'Element with locator: {i_how} {i_what} is not found!')


    #def isElementNotPresent(self, locator):
        #return bool(self._browser.find_element_by_xpath(locator))

    
    def isElementNotPresent(self, locator):
        try:
            a = self._browser.find_element_by_xpath(locator)
            raise AssertionError(f'Element with locator {locator}: is found!')
        except NoSuchElementException:
            return True


    def isElementPresent(self, locator):
        try:
            a = self._browser.find_element_by_css_selector(locator)
            return True
        except NoSuchElementException:
            raise AssertionError(f'Element with locator {locator}: is not found!')
            return False


    def GetValueText(self, locator):
        try:
            value_text = self._browser.find_element_by_css_selector(locator).text
            return value_text
        except NoSuchElementException:
            raise AssertionError(f"locator not found")
            return False
