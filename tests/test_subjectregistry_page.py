import pytest
from conftest import browser
from pages.login_page import LoginPage, path
from pages.subjectregistry_page import SubjectRegistryPage as SR
from constants import BASE_URL
from pages.base_page import BasePage
from pages.locators import LoginPageLocators as LP
from constants import LOGIN_PAGE_URL
from selenium.webdriver.common.by import By
path = LOGIN_PAGE_URL


#IP-153
@pytest.mark.need_review
def test_open_and_login_subjectregistry_page(browser):
    page = SR(browser, BASE_URL+path)
    page.open()
    page.check_auth_with_good_data()
    page.click_to_box_subjectregistry()
    page.check_dropdown_selector()


#IP-154
@pytest.mark.need_review
def test_check_search_ooo(browser):
    page = SR(browser, BASE_URL+path)
    page.open()
    page.check_auth_with_good_data()
    page.click_to_box_subjectregistry()
    page.check_search_ooo()


#IP-155
@pytest.mark.need_review
def test_check_search_ip(browser):
    page = SR(browser, BASE_URL+path)
    page.open()
    page.check_auth_with_good_data()
    page.click_to_box_subjectregistry()
    page.check_search_ip()


#IP-156
@pytest.mark.need_review
def test_sort_by_date_updated(browser):
    page = SR(browser, BASE_URL+path)
    page.open()
    page.check_auth_with_good_data()
    page.click_to_box_subjectregistry()
    page.sort_by_date_updated()


#IP-157
@pytest.mark.need_review
def test_sort_by_date_ogrn(browser):
    page = SR(browser, BASE_URL+path)
    page.open()
    page.check_auth_with_good_data()
    page.click_to_box_subjectregistry()
    page.sort_by_date_ogrn()