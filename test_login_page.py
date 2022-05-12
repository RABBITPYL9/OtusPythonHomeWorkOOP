import pytest
from conftest import browser
from pages.login_page import LoginPage, path
from constants import BASE_URL
from pages.base_page import BasePage
from pages.locators import LoginPageLocators as LP
from constants import LOGIN_PAGE_URL
from selenium.webdriver.common.by import By
path = LOGIN_PAGE_URL


@pytest.mark.need_review
def test_open_login_page_with_good_auth(browser):
    page = LoginPage(browser, BASE_URL+path)
    page.open()
    page.check_auth_with_good_data()