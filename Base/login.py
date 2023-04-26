import logging
import time

from Base.Selenium_driver import seleniumDriver
from Utilities.Custom_Logger import CustomLogger
from Locators.login_locators import LoginPageLocators

class Login(seleniumDriver):

    def __init__(self, driver):
        self.driver = driver

    log = CustomLogger(loggerName="loginLogger", logLevel=logging.DEBUG)

    def verify_dashboard_login(self):
        title = self.getTitle()
        print(title)
        return title == 'Home'
    
    def login_to_dashboard(self, url=""):
        self.log.info("Login into Dashboard")
        self.navigate_to_url(url)

        #enter email
        self.waitForElement(LoginPageLocators.userName_field)
        self.sendKeys("pavani.uppala@technossus.com.lis",LoginPageLocators.userName_field)
        # self.clearSendKeys(email, DashboardHomeLocators.userName_field)

        #enter password
        self.waitForElement(LoginPageLocators.passWord_field)
        self.sendKeys("Spivulet@123456",LoginPageLocators.passWord_field)

        #click login
        self.elementClick(LoginPageLocators.login_button,timeout=10)
        time.sleep(10)
        dashboard_login= self.verify_dashboard_login()
        self.takeScreenshot()
        print(dashboard_login)
        assert dashboard_login == True, "Login to Dashboard, Check FAILED"