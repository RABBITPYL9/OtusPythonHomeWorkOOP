import allure
from conftest import browser
from pages.base_page import BasePage
from pages.locators import LoginPageLocators as LP
from pages.locators import SubjectRegistryLocators as SR
from pages.locators import EgrnPageLocators as EP
from constants import LOGIN_PAGE_URL
from constants import TEST_DATA_SUBJECT_REGISTRY_LOGIN
from constants import TEST_DATA_SUBJECT_REGISTRY_PASSWORD
from constants import TEST_EGRN_LOGIN1
from constants import TEST_EGRN_PASS1
from constants import TEST_EGRN_LOGIN2
from constants import TEST_EGRN_PASS2
from constants import TEST_EGRN_LOGIN3
from constants import TEST_EGRN_PASS3
from constants import TEST_EGRN_LOGIN4
from constants import TEST_EGRN_PASS4
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
path = LOGIN_PAGE_URL
import time


class EgrnPage(BasePage):
    
    
    def check_auth_with_good_data_admin(self):
        self.click(*LP.NAME_FIELD)
        self.write_field(*LP.NAME_FIELD, TEST_DATA_SUBJECT_REGISTRY_LOGIN)
        self.click(*LP.PASSWORD_FIELD)
        self.write_field(*LP.PASSWORD_FIELD, TEST_DATA_SUBJECT_REGISTRY_PASSWORD) 
        self.is_element_present(*LP.ENTER_BUTTON)
        self.click(*LP.ENTER_BUTTON)
        self._browser.implicitly_wait(15)
        self.is_element_present(*LP.Sign_Out_Class)
        self._browser.implicitly_wait(15)

    
    def check_filter_objects(self):

        element_cancel = WebDriverWait(self._browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[2]/div[2]/button[2]")))
        element_cancel.click();
        
        element_search = WebDriverWait(self._browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='uid-btn uid-btn_main uid-btn_size_small uid-ml-32']")))
        element_search.click();

        element_field = WebDriverWait(self._browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Укажите кадастровый номер']")))
        element_field.click();


    def check_work_filter_with_type_zemelniy(self):
        self.click(*EP.FILTER_FAT)
        self.click(*EP.SELECTOR_FOR_TYPE_OBJECT_ON_FILTER_FAT)
        element_field = WebDriverWait(self._browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div/div[1]/form/div[1]/div[1]/div/div[2]/div[2]/div/div/span[2]")))
        element_field.click();
        self.click(*EP.SEARCH_BUTTON)
        ab = self.GetValueText("[class='registry-second-line uid-mt-16'] [class='uid-text-accent']")
        save_ab = int(ab)
        save_ab +=1
        self.click(*EP.GET_ZAPROS_BUTTON)
        self.click(*EP.FIELD_ENTER_KAD_NUMBER)
        self.write_field(*EP.FIELD_ENTER_KAD_NUMBER, "27:49:934842:323")
        self.click(*EP.SELECTOR_TYPE_OBJECT)
        self.click(*EP.OBJECT_ZEMELNIY_YCHASTOK)
        self.click(*EP.SEND_REQ_NUMBER)
        self.click(*EP.SELECTOR_FOR_TYPE_OBJECT_ON_FILTER_FAT)
        element_field = WebDriverWait(self._browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div/div[1]/form/div[1]/div[1]/div/div[2]/div[2]/div/div/span[2]")))
        element_field.click();
        self.click(*EP.SEARCH_BUTTON)
        abc = self.GetValueText("[class='registry-second-line uid-mt-16'] [class='uid-text-accent']")
        assert str(abc) == str(save_ab), "Колличество результатов в фильтре по типу Земельный участок не соответствует"


    def check_big_filter_objects(self):

        element_big_cancel = WebDriverWait(self._browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[2]/div[1]/span")))
        element_big_cancel.click()
        
        self.is_text_present(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/form/div[1]/div[1]/div/div[1]", "Тип объекта")
        self.is_text_present(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/form/div[1]/div[3]/div/div[1]", "Отправитель запроса")
        self.is_text_present(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div[1]", "Дата запроса")

        element_search1 = WebDriverWait(self._browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='uid-btn uid-btn_main uid-btn_size_small uid-ml-32']")))
        element_search1.click();

        element_cancel1 = WebDriverWait(self._browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='uid-btn uid-btn_secondary uid-btn_size_small']")))
        element_cancel1.click();

        element_svernyt_filter = WebDriverWait(self._browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div/div[1]/form/div[2]/div[1]/span")))
        element_svernyt_filter.click();

    
    def check_search_filter_with_kad_number(self):
        self.click(*EP.SEARCH_FIELD)
        self.write_field(*EP.SEARCH_FIELD, "13378123")
        self.click(*EP.SEARCH_BUTTON)
        self.is_text_present(By.CSS_SELECTOR, "[class='registry-second-line uid-mt-16'] [class='uid-text-accent']", "4")



    def check_columns_on_page(self):
        self.is_text_present(By.XPATH, "/html/body/div/div/div[2]/div/table/thead/tr/th[1]/div/span", "ДАТА И ВРЕМЯ ОТПРАВКИ ЗАПРОСА")
        self.is_text_present(By.XPATH, "/html/body/div/div/div[2]/div/table/thead/tr/th[2]/div/span", "КАДАСТРОВЫЙ НОМЕР")
        self.is_text_present(By.XPATH, "/html/body/div/div/div[2]/div/table/thead/tr/th[3]/div/span", "ФИО ОТПРАВИТЕЛЯ ЗАПРОСА")
        self.is_text_present(By.XPATH, "/html/body/div/div/div[2]/div/table/thead/tr/th[4]/div/span", "РЕЗУЛЬТАТ ЗАПРОСА")
        self.is_text_present(By.XPATH, "/html/body/div/div/div[2]/div/table/thead/tr/th[5]/div/span", "ДАТА ФОРМИРОВАНИЯ ВЫПИСКИ")
        self.is_text_present(By.XPATH, "/html/body/div/div/div[2]/div/table/thead/tr/th[6]/div/span", "ДАТА И ВРЕМЯ ПОЛУЧЕНИЯ РЕЗУЛЬТАТА")


    def check_auth_with_shubin_egrn1(self):
        self.click(*EP.NAME_FIELD)
        self.write_field(*EP.NAME_FIELD, TEST_EGRN_LOGIN1)
        self.click(*EP.PASSWORD_FIELD)
        self.write_field(*EP.PASSWORD_FIELD, TEST_EGRN_PASS1) 
        self.is_element_present(*LP.ENTER_BUTTON)
        self.click(*LP.ENTER_BUTTON)
        self._browser.implicitly_wait(15)
        self.is_element_present(*LP.Sign_Out_Class)
        self._browser.implicitly_wait(15)


    def check_auth_with_shubin_egrn2(self):
        self.click(*EP.NAME_FIELD)
        self.write_field(*EP.NAME_FIELD, TEST_EGRN_LOGIN2)
        self.click(*EP.PASSWORD_FIELD)
        self.write_field(*EP.PASSWORD_FIELD, TEST_EGRN_PASS2) 
        self.is_element_present(*LP.ENTER_BUTTON)
        self.click(*LP.ENTER_BUTTON)
        self._browser.implicitly_wait(15)
        self.is_element_present(*LP.Sign_Out_Class)
        self._browser.implicitly_wait(15)


    def check_auth_with_shubin_egrn3(self):
        self.click(*EP.NAME_FIELD)
        self.write_field(*EP.NAME_FIELD, TEST_EGRN_LOGIN3)
        self.click(*EP.PASSWORD_FIELD)
        self.write_field(*EP.PASSWORD_FIELD, TEST_EGRN_PASS3) 
        self.is_element_present(*LP.ENTER_BUTTON)
        self.click(*LP.ENTER_BUTTON)
        self._browser.implicitly_wait(15)
        self.is_element_present(*LP.Sign_Out_Class)
        self._browser.implicitly_wait(15)

    
    def check_auth_with_shubin_egrn4(self):
        self.click(*EP.NAME_FIELD)
        self.write_field(*EP.NAME_FIELD, TEST_EGRN_LOGIN4)
        self.click(*EP.PASSWORD_FIELD)
        self.write_field(*EP.PASSWORD_FIELD, TEST_EGRN_PASS4) 
        self.is_element_present(*LP.ENTER_BUTTON)
        self.click(*LP.ENTER_BUTTON)
        self._browser.implicitly_wait(15)
        self.is_element_present(*LP.Sign_Out_Class)
        self._browser.implicitly_wait(15)


    def check_not_present_element_on_dgp(self):
        self.isElementNotPresent("(//text()[. = 'Реестр запросов выписок из ЕГРН'])[1]")


    def check_redirect_after_move(self):
        time.sleep(2)
        self._browser.get("https://dgp.investmoscow.upt24.ru/app/egrn-statement-registry")
        time.sleep(3)
        current_url = self._browser.current_url
        assert current_url == "https://dgp.investmoscow.upt24.ru/Doutree2/home/Dashboard.aspx"


    def check_request_button_not_present_shubin_egrn1(self):
        self.isElementNotPresent("/html/body/div/div/div[2]/div/div[2]/div[2]/button/div")


    def check_request_button_is_present(self):
        self.is_text_present(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div[2]/button/div", 'Запросить выписку')
        self._browser.find_element_by_xpath("//*[text()='Запросить выписку']")

    
    def click_to_box_requests_from_egrn_and_open_page_shubin_egrn1(self):
        self.is_element_present(*EP.SHUBIN_EGRN1_TEXT_REQUESTS_FROM_EGRN)
        self.click(*EP.SHUBIN_EGRN1_BOX_REQUESTS_FROM_EGRN)
        s = self._browser.window_handles
        click_on_new_window = s[1]
        self._browser.switch_to.window(f"{click_on_new_window}")
        current_url = self._browser.current_url
        assert current_url == "https://dgp.investmoscow.upt24.ru/app/egrn-statement-registry"
        self._browser.implicitly_wait(15)


    def click_to_box_requests_from_egrn_and_open_page_shubin_egrn2(self):
        self.is_element_present(*EP.SHUBIN_EGRN1_TEXT_REQUESTS_FROM_EGRN)
        self.click(*EP.SHUBIN_EGRN1_BOX_REQUESTS_FROM_EGRN)
        s = self._browser.window_handles
        click_on_new_window = s[1]
        self._browser.switch_to.window(f"{click_on_new_window}")
        current_url = self._browser.current_url
        assert current_url == "https://dgp.investmoscow.upt24.ru/app/egrn-statement-registry"
        self._browser.implicitly_wait(15)


    def click_to_box_requests_from_egrn_and_open_page(self):
        self.is_element_present(*EP.BOX_REQUESTS_FROM_EGRN)
        self.click(*EP.BOX_REQUESTS_FROM_EGRN)
        s = self._browser.window_handles
        click_on_new_window = s[1]
        self._browser.switch_to.window(f"{click_on_new_window}")
        current_url = self._browser.current_url
        assert current_url == "https://dgp.investmoscow.upt24.ru/app/egrn-statement-registry"
        self._browser.implicitly_wait(15)
        

    def open_module_window_for_send_request(self):
        self.is_element_present(*EP.MODULE_WINDOW_ENTER_KADASTR_NUMBER)
        self.click(*EP.GET_ZAPROS_BUTTON)
        self.click(*EP.FIELD_ENTER_KAD_NUMBER)


    def check_send_request_of_zemelniy_ychastok(self):
        self.click(*EP.FIELD_ENTER_KAD_NUMBER)
        self.write_field(*EP.FIELD_ENTER_KAD_NUMBER, "27:49:934842:323")
        self.click(*EP.SELECTOR_TYPE_OBJECT)
        self.click(*EP.OBJECT_ZEMELNIY_YCHASTOK)
        self.click(*EP.SEND_REQ_NUMBER)


    def check_send_request_of_oks(self):
        self.click(*EP.FIELD_ENTER_KAD_NUMBER)
        self.write_field(*EP.FIELD_ENTER_KAD_NUMBER, "27:49:934842:323")
        self.click(*EP.SELECTOR_TYPE_OBJECT)
        self.click(*EP.OBJECT_OKS)
        self.click(*EP.SEND_REQ_NUMBER)


    def check_send_request_of_pomeshenie(self):
        self.click(*EP.FIELD_ENTER_KAD_NUMBER)
        self.write_field(*EP.FIELD_ENTER_KAD_NUMBER, "27:49:934842:323")
        self.click(*EP.SELECTOR_TYPE_OBJECT)
        self.click(*EP.OBJECT_POMESHENIE)
        self.click(*EP.SEND_REQ_NUMBER)


    def click_add_more_and_cancel_button(self):
        self.click(*EP.ADD_MORE_BTN)
        self.click(*EP.CANCEL_BUTTON_IN_MODULE_WINDOW)


    def check_sorted_by_first_column(self):
        self.isElementPresent("[class='uid-arrow uid-arrow-up']")


    def check_can_move_to_second_page_and_return_to_first(self):
        self.click(*EP.SECOND_PAGE)
        self.click(*EP.FIRST_PAGE)