from selenium.webdriver.common.by import By


class LoginPageLocators():
    NAME_FIELD = (By.CSS_SELECTOR, "[name='UserName']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[name='Password']")
    ENTER_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-large:nth-child(1)")
    WRONG_DATA_TEXT = (By.XPATH, "//*[text()='Неверный логин или пароль']")
    Sign_Out_Class = (By.XPATH, "[class='sign-out']")
