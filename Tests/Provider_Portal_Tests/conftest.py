import pytest
from selenium import webdriver

from Base.login import Login

@pytest.fixture(scope='class')
def setupDriver(request):
    print("setup Driver")
    driver = webdriver.Chrome()
    lp = Login(driver)

    lp.login_to_dashboard('https://biotheranostics--lisqa.sandbox.my.site.com/s/login/?ec=302&startURL=%2Fs%2F')

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    print("tear down")
    driver.quit()
