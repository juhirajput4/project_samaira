from selenium import webdriver
import time
import unittest
import pytest

from pages.Home_Page.provider_portal_home import ProviderPortal

@pytest.mark.usefixtures("setupDriver")
class Test_Provider_Portal(unittest.TestCase):

    @pytest.fixture(autouse = True)
    def classSetup(self, setupDriver):
        self.provider_portal = ProviderPortal(self.driver)

    @pytest.mark.run(order=1)
    def test_form_sumbit(self):
        self.provider_portal.click_unsumbitted_request()
        time.sleep(4)
        self.provider_portal.find_CTID_in_Table()
        time.sleep(2)
        self.provider_portal.edit_form()
        time.sleep(2)
        self.provider_portal.enter_sex()
        self.provider_portal.enter_dob()
        self.provider_portal.enter_bill_to()
        time.sleep(2)
        self.provider_portal.enter_hospital_status()
        time.sleep(2)
        self.provider_portal.press_save()
        time.sleep(15)
        self.provider_portal.fomalities()
        time.sleep(10)


