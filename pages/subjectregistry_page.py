import allure
from conftest import browser
from pages.base_page import BasePage
from pages.locators import LoginPageLocators as LP
from pages.locators import SubjectRegistryLocators as SR
from constants import LOGIN_PAGE_URL
from constants import TEST_DATA_SUBJECT_REGISTRY_LOGIN
from constants import TEST_DATA_SUBJECT_REGISTRY_PASSWORD
from selenium.webdriver.common.by import By
import time
path = LOGIN_PAGE_URL


class SubjectRegistryPage(BasePage):
    

    def check_auth_with_good_data(self):
        self.click(*LP.NAME_FIELD)
        self.write_field(*LP.NAME_FIELD, TEST_DATA_SUBJECT_REGISTRY_LOGIN)
        self.click(*LP.PASSWORD_FIELD)
        self.write_field(*LP.PASSWORD_FIELD, TEST_DATA_SUBJECT_REGISTRY_PASSWORD) 
        self.is_element_present(*LP.ENTER_BUTTON)
        self.click(*LP.ENTER_BUTTON)
        self.is_element_present(*LP.Sign_Out_Class)

    
    def click_to_box_subjectregistry(self):
        self.is_element_present(*SR.BOX_SUBJECTREGISTRY)
        self.is_text_present(By.XPATH, "/html/body/div[2]/div/div/div[12]/a/span", "Реестр субъектов инвестиционной деятельности")
        self._browser.get(
                "https://dgp.investmoscow.upt24.ru/app/subject-registry"
            )


    def check_dropdown_selector(self):
        self.is_element_present(*SR.DROPDOWN_SELECTOR)
        self.is_text_present(By.CSS_SELECTOR, "[class='menu-dropdown__selected-value']>span", 'Реестр субъектов инвестиционной деятельности')

    
    def check_search_ooo(self):
        self.is_element_present(*SR.SEARCH_FIELD)
        self.is_element_present(*SR.SEARCH_BUTTON)
        self.click(*SR.SEARCH_FIELD)
        self.clear(*SR.SEARCH_FIELD)
        self.write_field(*SR.SEARCH_FIELD, 'СТАН-Р')
        self.click(*SR.SEARCH_BUTTON)
        card_count = self._browser.find_elements(By.CSS_SELECTOR, '[class="card"]')
        assert len(card_count) == 1, "Не совпадение по колличеству результатов"
        ooo_count = self._browser.find_elements(By.XPATH, "//*[contains(text(), 'СТАН-Р')]")
        assert len(ooo_count) == 1, "Не совпадение по колличеству результатов для ООО СТАН-Р "

    def check_search_ip(self):
        self.is_element_present(*SR.SEARCH_FIELD)
        self.is_element_present(*SR.SEARCH_BUTTON)
        self.click(*SR.SEARCH_FIELD)
        self.clear(*SR.SEARCH_FIELD)
        self.write_field(*SR.SEARCH_FIELD, 'МЕЗЕНЦЕВА ЕЛЕНА')
        self.click(*SR.TYPE_SUBJECT)
        self.click(*SR.SELECTOR_VALUE_IP)
        self.click(*SR.SEARCH_BUTTON)
        card_count_ip = self._browser.find_elements(By.CSS_SELECTOR, '[class="card"]')
        assert len(card_count_ip) == 1, "Не совпадение по колличеству результатов для ИП"
        ip_count = self._browser.find_elements(By.XPATH, "//*[contains(text(), 'МЕЗЕНЦЕВА ЕЛЕНА')]")
        assert len(ip_count) == 1, "Не совпадение по колличеству результатов для ИП"
 
    
    def sort_by_date_updated(self):
        self.is_element_present(*SR.SEARCH_FIELD)
        self.is_element_present(*SR.SEARCH_BUTTON)
        self.is_element_present(*SR.SELECTOR_SORT)
        self.click(*SR.SELECTOR_SORT_DATE)
        self.click(*SR.SELECTOR_SORT_DATE_VALUE_UPDATED)
        card_count_sort = self._browser.find_elements(By.CSS_SELECTOR, '[class="card"]')
        assert len(card_count_sort) == 10, "Не совпадение по колличеству результатов при сортировке"
        sort_date_count = self._browser.find_elements(By.XPATH, "//*[contains(text(), 'СТАН-Р')]")
        assert len(sort_date_count) == 1, "Не совпадение по колличеству результатов при сортировке"


    def sort_by_date_ogrn(self):
        self.is_element_present(*SR.SEARCH_FIELD)
        self.is_element_present(*SR.SEARCH_BUTTON)
        self.is_element_present(*SR.SELECTOR_SORT)
        self.click(*SR.SELECTOR_SORT_DATE)
        self.click(*SR.SELECTOR_SORT_DATE_VALUE_OGRN)
        card_ogrn_sort = self._browser.find_elements(By.CSS_SELECTOR, '[class="card"]')
        assert len(card_ogrn_sort) == 10, "Не совпадение по колличеству результатов"
        sort_ogrn_count = self._browser.find_elements(By.XPATH, "//*[contains(text(), 'ЛЮНЕТ')]")
        assert len(sort_ogrn_count) == 1, "Не совпадение по колличеству результатов"

