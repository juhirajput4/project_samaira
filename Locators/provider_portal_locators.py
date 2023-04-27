from selenium import webdriver
from selenium.webdriver.common.by import By

class ProviderPortalLocators:
    unsubmitted_requests_button = (By.XPATH,"(//a[@class='list-item-a customTablwc'])[2]")
    patient_name= (By.XPATH, "//tbody/tr")
    next_button= (By.XPATH,"//button[@class='slds-button slds-button_brand'][2]")
    display_record_dropdown = (By.XPATH, "//select[@class='slds-select']")

    # edit button
    edit_button = (By.XPATH, "(//lightning-icon[@icon-name='utility:edit']/span/lightning-primitive-icon)[1]")

    #patient
    patient_DOB = (By.XPATH, "(//lightning-input[@class='slds-form-element']/lightning-datepicker/div/div/input)[1]")
    patient_sex = (By.XPATH, "//select[@name='sex']")
    patient_lastname = (By.XPATH, "(//div[@id='PatientInformationEdit']/div/div)[3]/lightning-input/div/div/input")
    bill_to = (By.XPATH, "(//div[@class='slds-select_container']/select)[2]")
    hospital_status = (By.XPATH, "(//div[@class='slds-select_container']/select)[3]")
    save_button = (By.XPATH, "(//div[@class='slds-align_absolute-center']/button[@type='button'])[4]")

    #submitrelated
    patient_face_sheet = (By.XPATH, "(//span[@part='indicator'])[4]")
    patient_insurance_info = (By.XPATH, "(//span[@part='indicator'])[5]")
    pythology_report = (By.XPATH, "(//span[@part='indicator'])[6]")
    terms_and_condition = (By.XPATH, "(//span[@part='indicator'])[7]")
    submit_testReport_button = (By.XPATH, "(//button[@type='button'])[10]")