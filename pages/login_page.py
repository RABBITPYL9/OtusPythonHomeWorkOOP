import allure
from conftest import browser
from pages.base_page import BasePage
from pages.locators import LoginPageLocators as LP
from constants import LOGIN_PAGE_URL
import random
from selenium.webdriver.common.by import By
import time
path = LOGIN_PAGE_URL


class LoginPage(BasePage):
    
    
    def check_auth_with_good_data_and_exit(self):
        self.click(*LP.NAME_FIELD)
        self.write_field(*LP.NAME_FIELD, "dgp")
        self.click(*LP.PASSWORD_FIELD)
        self.write_field(*LP.PASSWORD_FIELD, "111") 
        self.is_element_present(*LP.ENTER_BUTTON)
        self.click(*LP.ENTER_BUTTON)
        self.is_element_present(*LP.Sign_Out_Class)
        self._browser.implicitly_wait(15)
        self._browser.get(
                "https://dgp.investmoscow.upt24.ru/Doutree2/Account/LogOff.aspx"
            )
        self.is_not_element_present(*LP.Sign_Out_Class)

    def check_auth_with_good_data(self):
        self.click(*LP.NAME_FIELD)
        self.write_field(*LP.NAME_FIELD, "dgp")
        self.click(*LP.PASSWORD_FIELD)
        self.write_field(*LP.PASSWORD_FIELD, "111") 
        self.is_element_present(*LP.ENTER_BUTTON)
        self.click(*LP.ENTER_BUTTON)
        self.is_element_present(*LP.Sign_Out_Class)

    
    def check_url_after_login(self):
        time.sleep(3)
        current_url = self._browser.current_url
        assert current_url == "https://dgp.investmoscow.upt24.ru/Doutree2/home/Dashboard.aspx"
        self._browser.implicitly_wait(15)

    def check_auth_with_bad_pass(self):
        self.click(*LP.NAME_FIELD)
        self.write_field(*LP.NAME_FIELD, "dgp")
        self.click(*LP.PASSWORD_FIELD)
        self.write_field(*LP.PASSWORD_FIELD, "11123") 
        self.is_element_present(*LP.ENTER_BUTTON)
        self.click(*LP.ENTER_BUTTON)
        self.is_element_present(*LP.WRONG_DATA_TEXT)


    def assert_title(self):
        assert "Авторизация - ЕИИП" == browser.title

