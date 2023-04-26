from selenium.webdriver.common.by import By


class LoginPageLocators:
    userName_field = (By.XPATH, "//input[@placeholder='Username']")
    passWord_field = (By.XPATH, "//input[@placeholder='Password']")
    login_button = (By.XPATH, "//button[@type='button']")