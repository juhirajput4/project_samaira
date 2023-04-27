import logging
import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from Base.Selenium_driver import seleniumDriver
from Utilities.Custom_Logger import CustomLogger
from Locators.provider_portal_locators import ProviderPortalLocators

#constants
RequiredTestType = "CancerType ID"

class ProviderPortal(seleniumDriver):

    log = CustomLogger(loggerName="loginLogger", logLevel=logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def click_unsumbitted_request(self):
        self.elementClick(ProviderPortalLocators.unsubmitted_requests_button)

    def get_patients(self):
        if self.isElementPresent(ProviderPortalLocators.patient_name):
            print('is present')
        return self.getElementList(ProviderPortalLocators.patient_name)

    def get_next_page(self):
        self.elementClick(ProviderPortalLocators.next_button)

    def change_dropdown(self):
        dropdown_ele = self.getElement(ProviderPortalLocators.display_record_dropdown)
        sel = Select(dropdown_ele)
        sel.select_by_value("25")
        time.sleep(5)

    def find_CTID_in_Table(self):
        time.sleep(10)
        self.change_dropdown()
        rows = self.get_patients()
        for row in rows:
            test_type = row.find_element(By.XPATH,".//th[@data-label='Test Type']").text
            if test_type == RequiredTestType:
                patient = row.find_element(By.XPATH,".//th[@data-label='Patient Name']/a")
                time.sleep(2)
                print(patient.text)
                patient.click()
                break

    def edit_form(self):
        self.waitForElement(ProviderPortalLocators.edit_button)
        self.elementClick(ProviderPortalLocators.edit_button)

    def enter_dob(self, date="Apr 11, 1980"):
        self.waitForElement(ProviderPortalLocators.patient_DOB)
        self.clearFieldFunction(ProviderPortalLocators.patient_DOB)
        self.sendKeys(date, ProviderPortalLocators.patient_DOB)

    def enter_last_name(self, last_name="Trey"):
        self.waitForElement(ProviderPortalLocators.patient_lastname)
        self.clearFieldFunction(ProviderPortalLocators.patient_lastname)
        self.sendKeys(last_name, ProviderPortalLocators.patient_lastname)

    def enter_sex(self):
        dropdown_ele = self.getElement(ProviderPortalLocators.patient_sex)
        sel = Select(dropdown_ele)
        sel.select_by_value("Female")
        time.sleep(5)

    def enter_bill_to(self):
        dropdown_ele = self.getElement(ProviderPortalLocators.bill_to)
        sel = Select(dropdown_ele)
        sel.select_by_value("Private Insurance")
        time.sleep(5)

    def enter_hospital_status(self):
        dropdown_ele = self.getElement(ProviderPortalLocators.hospital_status)
        sel = Select(dropdown_ele)
        sel.select_by_value("Outpatient")
        time.sleep(5)

    def press_save(self):
        self.waitForElement(ProviderPortalLocators.save_button)
        self.elementClick(ProviderPortalLocators.save_button)

    def fomalities(self):
        time.sleep(2)
        self.waitForElement(ProviderPortalLocators.patient_face_sheet)
        self.elementClick(ProviderPortalLocators.patient_face_sheet)
        time.sleep(2)
        self.waitForElement(ProviderPortalLocators.patient_insurance_info)
        self.elementClick(ProviderPortalLocators.patient_insurance_info)
        time.sleep(2)
        self.waitForElement(ProviderPortalLocators.pythology_report)
        self.elementClick(ProviderPortalLocators.pythology_report)
        time.sleep(2)
        self.waitForElement(ProviderPortalLocators.terms_and_condition)
        self.elementClick(ProviderPortalLocators.terms_and_condition)
        time.sleep(2)
        self.waitForElement(ProviderPortalLocators.submit_testReport_button)
        # self.elementClick(ProviderPortalLocators.submit_testReport_button)



