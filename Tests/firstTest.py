from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from Base.login import Login

driver = webdriver.Chrome()
lp = Login(driver)
# driver.get('https://biotheranostics--lisqa.sandbox.lightning.force.com/lightning/n/BTX_Home')

lp.login_to_dashboard('https://biotheranostics--lisqa.sandbox.my.site.com/s/login/?ec=302&startURL=%2Fs%2F')

time.sleep(40000)
driver.close()

