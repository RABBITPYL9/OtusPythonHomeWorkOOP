from selenium.webdriver.common.by import By


class LoginPageLocators():
    
    NAME_FIELD = (By.CSS_SELECTOR, "[name='UserName']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[name='Password']")
    ENTER_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-large:nth-child(1)")
    WRONG_DATA_TEXT = (By.XPATH, "//*[text()='Неверный логин или пароль']")
    Sign_Out_Class = (By.XPATH, "[class='sign-out']")


class SubjectRegistryLocators():
    
    DROPDOWN_SELECTOR = (By.CSS_SELECTOR, "[class='menu-dropdown__selected-value']>span")
    BOX_SUBJECTREGISTRY = (By.XPATH, "(//text()[. = 'Реестр субъектов инвестиционной деятельности'])[1]")
    SEARCH_FIELD = (By.CSS_SELECTOR, "[placeholder='Укажите ИНН или ОГРН (ОГРНИП) или наименование ЮЛ, ФИО ИП']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "[class='uid-btn uid-btn_main uid-btn_size_small uid-ml-32']")
    SELECTOR_OOO_IP = (By.CSS_SELECTOR, "[class='uid-select-label']")
    TYPE_SUBJECT = (By.CSS_SELECTOR, "[class='uid-select__selected']")
    SELECTOR_VALUE_IP = (By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div/div/span[2]")
    SELECTOR_SORT = (By.XPATH, "[class='inline-block select-popper']")
    SELECTOR_SORT_DATE = (By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div/span")
    SELECTOR_SORT_DATE_VALUE_UPDATED = (By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div/span[1]")
    SELECTOR_SORT_DATE_VALUE_OGRN = (By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div/span[2]")


class EgrnPageLocators():

    NAME_FIELD = (By.CSS_SELECTOR, "[name='UserName']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[name='Password']")
    ENTER_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-large:nth-child(1)")
    WRONG_DATA_TEXT = (By.XPATH, "//*[text()='Неверный логин или пароль']")
    Sign_Out_Class = (By.XPATH, "[class='sign-out']")
    SEARCH_FIELD = (By.CSS_SELECTOR, "[placeholder='Укажите кадастровый номер']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "[class='uid-btn uid-btn_main uid-btn_size_small uid-ml-32']")
    CANCEL_BUTTON = (By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[2]/div[2]/button[1]")
    GET_ZAPROS_BUTTON = (By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div[2]/button/div")
    MODULE_WINDOW_ENTER_KADASTR_NUMBER = (By.CSS_SELECTOR, "[class='requests-header row']")
    ENTER_KAD_NUMBER_TEXT = (By.CSS_SELECTOR, "//text()[. = 'Введите кадастровый номер']")
    SELECT_TYPE_OBJECT = (By.CSS_SELECTOR, "//text()[. = 'Тип объекта1']")
    CLOSE_WINDOW_ICON = (By.CSS_SELECTOR, "[class='uid-portal-btn-close1']")
    ADD_MORE_TEXT = (By.CSS_SELECTOR, "//text()[. = 'Добавить еще1']")
    ADD_MORE_BTN = (By.XPATH, "/html/body/div/div/div[3]/div/div/section/div/div[2]/button/span")
    FIELD_ENTER_KAD_NUMBER = (By.CSS_SELECTOR, "[placeholder='00:00:000000:000']")
    #SELECTOR_TYPE_OBJECT = (By.CSS_SELECTOR, "[class='uid-select__selected']")
    SELECTOR_TYPE_OBJECT = (By.XPATH, "/html/body/div/div/div[3]/div/div/section/div/div[1]/div[2]/div/div/div[1]/div/div/div/span")
    OBJECT_ZEMELNIY_YCHASTOK = (By.XPATH, "/html/body/div/div/div[3]/div/div/section/div/div[1]/div[2]/div/div/div[2]/div/div/span[2]")
    OBJECT_POMESHENIE = (By.XPATH, "/html/body/div/div/div[3]/div/div/section/div/div[1]/div[2]/div/div/div[2]/div/div/span[4]")
    OBJECT_OKS = (By.XPATH, "/html/body/div/div/div[3]/div/div/section/div/div[1]/div[2]/div/div/div[2]/div/div/span[3]")
    SEND_REQ_NUMBER = (By.CSS_SELECTOR, "[class='uid-btn uid-btn_main uid-btn_size_small uid-ml-24']")
    CANCEL_BUTTON_IN_MODULE_WINDOW = (By.CSS_SELECTOR, "footer>[class='uid-btn uid-btn_secondary uid-btn_size_small']")
    TABLE_WITH_RESULT = (By.CSS_SELECTOR, "[class='uid-table-tbody']")
    RESULT_ON_13_PAGE_KAD_NUMBER = (By.XPATH, "//text()[. = '3d2322']")
    RESULT_ON_13_PAGE_LOGIN_SENDER = (By.CSS_SELECTOR, "(//text()[. = 'Администратор  .  .'])[1]")
    RESULT_ON_13_PAGE_DATE_SENDER = (By.CSS_SELECTOR, "(//text()[. = '05.05.2022 в 14:00'])[1]")
    BOX_REQUESTS_FROM_EGRN = (By.XPATH, "/html/body/div[2]/div/div/div[14]/a")
    SHUBIN_EGRN1_BOX_REQUESTS_FROM_EGRN = (By.XPATH, "/html/body/div[2]/div/div/div[3]/a")
    SHUBIN_EGRN1_TEXT_REQUESTS_FROM_EGRN = (By.XPATH, "(//text()[. = 'Реестр запросов выписок из ЕГРН'])[1]")
    SORTED_FIRST_COLUMN = (By.CSS_SELECTOR, "[class='uid-arrow uid-arrow-up']")
    FIRST_PAGE = (By.CSS_SELECTOR, "[class='page-wrapper uid-mt-24 uid-mb-32'] li:nth-child(1) > button")
    SECOND_PAGE = (By.CSS_SELECTOR, "[class='page-wrapper uid-mt-24 uid-mb-32'] li:nth-child(2) > button")
    BIG_DATA_FILTER = (By.CSS_SELECTOR, "[class='uid-select-label']")
    FILTER_FAT = (By.CSS_SELECTOR, "[class='link-button']")
    SELECTOR_FOR_TYPE_OBJECT_ON_FILTER_FAT = (By.CSS_SELECTOR, "[class='uid-select__selected']")