import pytest
from conftest import browser
from pages.login_page import LoginPage, path
from pages.subjectregistry_page import SubjectRegistryPage as SR
from pages.egrn_page import EgrnPage as EP
from constants import BASE_URL
from pages.base_page import BasePage
from pages.locators import LoginPageLocators as LP
from constants import LOGIN_PAGE_URL
from constants import TEST_EGRN_LOGIN1
from constants import TEST_EGRN_PASS1
from constants import TEST_EGRN_LOGIN2
from constants import TEST_EGRN_PASS2
from constants import TEST_EGRN_LOGIN3
from constants import TEST_EGRN_PASS3
from constants import TEST_EGRN_LOGIN4
from constants import TEST_EGRN_PASS4
from selenium.webdriver.common.by import By
path = LOGIN_PAGE_URL
import time


#test with admin data(авторизация под админом) и проверка наличия колонок на странице
@pytest.mark.need_review
def test_check_content_data_on_egrn_page(browser):
    page = EP(browser, BASE_URL+path)
    page.open()
    page.check_auth_with_good_data_admin()
    page.click_to_box_requests_from_egrn_and_open_page()
    page.check_columns_on_page()


#test with admin data(авторизация под админом) и проверка сортировки по умолчанию по колонке "Дата и время отправки запроса"
@pytest.mark.need_review
def test_check_content_data_on_egrn_page(browser):
    page = EP(browser, BASE_URL+path)
    page.open()
    page.check_auth_with_good_data_admin()
    page.click_to_box_requests_from_egrn_and_open_page()
    page.check_columns_on_page()
    page.check_sorted_by_first_column()


#Авторизация под админом и проверка доступности кнопки "запросить выписку"
@pytest.mark.need_review
def test_check_filter_data_and_request_button(browser):
    page = EP(browser, BASE_URL+path)
    page.open()
    page.check_auth_with_good_data_admin()
    page.click_to_box_requests_from_egrn_and_open_page()
    page.check_request_button_is_present()
    page.check_filter_objects()


#Авторизация под shubin_egrn и проверка контента на странице
@pytest.mark.need_review
def test_check_auth_with_shubin_egrn1_and_check_content(browser):
    page = EP(browser, BASE_URL+path)
    page.open()
    page.check_auth_with_shubin_egrn1()
    page.click_to_box_requests_from_egrn_and_open_page_shubin_egrn1()
    page.check_filter_objects()
    page.check_columns_on_page()



#проверка что пользователь shubin_egrn_1 не видит кнопку "запросить выписку"
@pytest.mark.need_review
def test_check_cant_get_requests_from_egrn(browser):
    page = EP(browser, BASE_URL+path)
    page.open()
    page.check_auth_with_shubin_egrn1()
    page.click_to_box_requests_from_egrn_and_open_page_shubin_egrn1()
    page.check_filter_objects()
    page.check_request_button_not_present_shubin_egrn1()


#Авторизация под пользователем shubin_egrn2 и проверка доступности кнопки "Запросить выписку"
@pytest.mark.need_review
def test_check_auth_shubinegrn2_and_get_request_button(browser):
    page = EP(browser, BASE_URL+path)
    page.open()
    page.check_auth_with_shubin_egrn2()
    page.click_to_box_requests_from_egrn_and_open_page_shubin_egrn2()
    page.check_request_button_is_present()
    page.check_filter_objects()


#Авторизация под пользователем shubin_egrn2 и открытие модульного окна запроса выписки
@pytest.mark.need_review
def test_check_auth_shubinegrn2_and_get_request_button(browser):
    page = EP(browser, BASE_URL+path)
    page.open()
    page.check_auth_with_shubin_egrn2()
    page.click_to_box_requests_from_egrn_and_open_page_shubin_egrn2()
    page.check_request_button_is_present()
    page.check_filter_objects()
    page.open_module_window_for_send_request()


#Авторизация под пользователем shubin_egrn2 и открытие окна запроса выписки
@pytest.mark.need_review
def test_check_send_request(browser):
    page = EP(browser, BASE_URL+path)
    page.open()
    page.check_auth_with_shubin_egrn2()
    page.click_to_box_requests_from_egrn_and_open_page_shubin_egrn2()
    page.check_request_button_is_present()
    page.check_filter_objects()
    page.open_module_window_for_send_request()


#Авторизация под пользователем shubin_egrn2 и отправка запроса с типом земельный участок
@pytest.mark.need_review
def test_check_send_request_zemelniy(browser):
    page = EP(browser, BASE_URL+path)
    page.open()
    page.check_auth_with_shubin_egrn2()
    page.click_to_box_requests_from_egrn_and_open_page_shubin_egrn2()
    page.check_request_button_is_present()
    page.check_filter_objects()
    page.open_module_window_for_send_request()
    page.check_send_request_of_zemelniy_ychastok()


#Авторизация под пользователем shubin_egrn2 и отправка запроса с типом ОКС (здание)
@pytest.mark.need_review
def test_check_send_request_oks(browser):
    page = EP(browser, BASE_URL+path)
    page.open()
    page.check_auth_with_shubin_egrn2()
    page.click_to_box_requests_from_egrn_and_open_page_shubin_egrn2()
    page.check_request_button_is_present()
    page.check_filter_objects()
    page.open_module_window_for_send_request()
    page.check_send_request_of_oks()


#Авторизация под пользователем shubin_egrn2 и отправка запроса с типом помещение
@pytest.mark.need_review
def test_check_send_request_pomeshenie(browser):
    page = EP(browser, BASE_URL+path)
    page.open()
    page.check_auth_with_shubin_egrn2()
    page.click_to_box_requests_from_egrn_and_open_page_shubin_egrn2()
    page.check_request_button_is_present()
    page.check_filter_objects()
    page.open_module_window_for_send_request()
    page.check_send_request_of_pomeshenie()


#Авторизация под пользователем shubin_egrn2 и нажатие кнопки "Добавить еще", "Отмена" в модульном окне отправки запроса
@pytest.mark.need_review
def test_check_click_on_window(browser):
    page = EP(browser, BASE_URL+path)
    page.open()
    page.check_auth_with_shubin_egrn2()
    page.click_to_box_requests_from_egrn_and_open_page_shubin_egrn2()
    page.check_request_button_is_present()
    page.check_filter_objects()
    page.open_module_window_for_send_request()
    page.click_add_more_and_cancel_button()


#Авторизация под пользователем shubin_egrn2 и проверка пагинации, переход с первой на вторую страницу выписок и обратно на первую
@pytest.mark.need_review
def test_check_move_to_pages(browser):
    page = EP(browser, BASE_URL+path)
    page.open()
    page.check_auth_with_shubin_egrn2()
    page.click_to_box_requests_from_egrn_and_open_page_shubin_egrn2()
    page.check_request_button_is_present()
    page.check_filter_objects()
    page.check_can_move_to_second_page_and_return_to_first()


#Авторизация под пользователем shubin_egrn2 и проверка наличия элементов расширенного фильтра
@pytest.mark.need_review
def test_check_big_filter_objects(browser):
    page = EP(browser, BASE_URL+path)
    page.open()
    page.check_auth_with_shubin_egrn2()
    page.click_to_box_requests_from_egrn_and_open_page_shubin_egrn2()
    page.check_request_button_is_present()
    page.check_filter_objects()
    page.check_big_filter_objects()


#Авторизация под пользователем shubin_egrn2 и проверка работы фильтра по кадастровому номеру
@pytest.mark.need_review
def test_check_work_filter_with_kad_number(browser):
    page = EP(browser, BASE_URL+path)
    page.open()
    page.check_auth_with_shubin_egrn2()
    page.click_to_box_requests_from_egrn_and_open_page_shubin_egrn2()
    page.check_request_button_is_present()
    page.check_search_filter_with_kad_number()


#Авторизация под пользователем shubin_egrn2 и проверка работы фильтра по типу поиска с типом объекта земельный участок
@pytest.mark.need_review
def test_check_work_filter_with_type_zemelniy(browser):
    page = EP(browser, BASE_URL+path)
    page.open()
    page.check_auth_with_shubin_egrn2()
    page.click_to_box_requests_from_egrn_and_open_page_shubin_egrn2()
    page.check_request_button_is_present()
    page.check_work_filter_with_type_zemelniy()


#Авторизация под пользователем shubin_egrn3 (с правами отправка запросом, скачивание выписки)
@pytest.mark.need_review
def test_auth_with_shubin_egrn3(browser):
    page = EP(browser, BASE_URL+path)
    page.open()
    page.check_auth_with_shubin_egrn3()
    page.click_to_box_requests_from_egrn_and_open_page_shubin_egrn2()
    page.check_request_button_is_present()
    page.check_filter_objects()
    page.open_module_window_for_send_request()
    page.check_send_request_of_zemelniy_ychastok()


#Авторизация под пользователем shubin_egrn4 (права отсутствуют)
@pytest.mark.need_review
def test_auth_with_shubin_egrn4(browser):
    page = EP(browser, BASE_URL+path)
    page.open()
    page.check_auth_with_shubin_egrn4()


#Авторизация под пользователем shubin_egrn4 (права отсутствуют) и проверка отсутствие карточки "Реестр запроса выписок из ЕГРН" в дгп
@pytest.mark.need_review
def test_check_not_present_box(browser):
    page = EP(browser, BASE_URL+path)
    page.open()
    page.check_auth_with_shubin_egrn4()
    page.check_not_present_element_on_dgp()


#Авторизация под пользователем shubin_egrn4 (права отсутствуют) и проверка перемещения пользователя при переходе по прямой ссылке
@pytest.mark.need_review
def test_check_redirect(browser):
    page = EP(browser, BASE_URL+path)
    page.open()
    page.check_auth_with_shubin_egrn4()
    page.check_redirect_after_move()


