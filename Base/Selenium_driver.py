import os
import logging


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Utilities.Custom_Logger import CustomLogger
from Utilities.utils import getUniqueName
import time

class seleniumDriver():
    log = CustomLogger(loggerName="classLogger", logLevel=logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_url(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def getTitle(self):
        return self.driver.title

    def getElement(self, locator):
        element = None
        try:
            element = self.driver.find_element(*locator)
            self.log.info("Element Found with locator: " + locator[1])
        except:
            self.log.info("Element not found with locator: " + locator[1])
        return element

    def getElementList(self, locator):
        """
        Get list of elements
        """
        elements = self.driver.find_elements(*locator)
        if (elements):
            self.log.info("Element list FOUND with locator: " + locator[1])
        else:
            self.log.info("Element list NOT FOUND with locator: " + locator[1])
        return elements

    def elementClick(self, locator, timeout=5):
        """
        Takes locator and timeout values as parameter.
        Default timeout value is 5 secs.
        """
        try:
            element = self.getElement(locator)
            self.highlight_element(locator)
            element.click()
            self.log.info("Clicked on element with locator: " + locator[1])
        except Exception as err_msg:
            self.takeScreenshot()
            raise AssertionError("Cannot click on the element with locator: " + locator[1] + "\nerror:" + str(err_msg))

    def clickOnLinkText(self, text):
        try:
            element = self.driver.find_element_by_partial_link_text(text)
            element.click()
        except:
            self.log.info("Failed to click on link text: " + text)

    def sendKeys(self, data, locator):
        try:
            element = self.getElement(locator)
            self.highlight_element(locator)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator[1])
        except Exception as err_msg:
            self.takeScreenshot()
            raise AssertionError("Cannot send data on element with locator: " + locator[1] + "\nerror:" + str(err_msg))

    def getText(self, locator):
        """
        NEW METHOD
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            element = self.getElement(locator)
            self.highlight_element(locator)
            text = element.text
            if len(text) == 0:
                text = element.get_attribute("innerText")
            else:
                self.log.info("Getting text on element :: " + locator[1])
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except Exception as err_msg:
            self.takeScreenshot()
            raise AssertionError("Failed to get text on element: " + locator[1] + "\nerror:" + str(err_msg))
        return text

    def isElementPresent(self, locator):
        try:
            elements = self.driver.find_elements(*locator)
            if (elements):
                self.log.info("Element Found: " + str(locator))
                return True
            else:
                self.log.info("Element not found: " + str(locator))
                return False
        except:
            self.log.info("Element not found: " + str(locator))
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if (elementList):
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def isEnabled(self, locator, info=""):
        """
        Check if element is enabled

        Parameters:
            1. Required:
                1. locator - Locator of the element to check
            2. Optional:
                1. locatorType - Type of the locator(id(default), xpath, css, className, linkText)
                2. info - Information about the element, label/name of the element
        Returns:
            boolean
        Exception:
            None
        """
        element = self.getElement(locator)
        enabled = False
        try:
            attributeValue = self.getElementAttributeValue(
                locator=locator, attribute="disabled"
            )
            if attributeValue is not None:
                enabled = element.is_enabled()
            else:
                value = self.getElementAttributeValue(
                    locator=locator, attribute="class"
                )
                self.log.info("Attribute value From Application Web UI --> :: " + value)
                enabled = not ("disabled" in value)
            if enabled:
                self.log.info("Element :: '" + str(locator) + "' is enabled")
            else:
                self.log.info("Element :: '" + str(locator) + "' is not enabled")
        except:
            self.log.error("Element :: '" + str(locator) + "' state could not be found")
        return enabled


    def getAttribute(self, attribute, locator):
        try:
            attribute_element = self.getElement(locator)
            temp = attribute_element.get_attribute(attribute)
            return temp
        except Exception as err_msg:
            self.takeScreenshot()
            raise AssertionError("Cannot get attribute of locator:" + locator[1] + "\nerror:" + str(err_msg))

    def uploadFile(self, locator, fileExt):
        try:
            if fileExt == "png":
                current_path = os.getcwd()
                path = current_path + "/uploadFiles/Screenshot.png"
                self.log.info("Path :: '" + str(path) + "' of a file")
                self.sendKeys(path, locator)
            elif fileExt == "jpeg":
                current_path = os.getcwd()
                path = current_path + "/uploadFiles/testImage.jpeg"
                self.log.info("Path :: '" + str(path) + "' of a file")
                self.sendKeys(path, locator)
            elif fileExt == "pdf":
                current_path = os.getcwd()
                path = current_path + "/uploadFiles/testPdf.pdf"
                self.log.info("Path :: '" + str(path) + "' of a file")
                self.sendKeys(path, locator)
            elif fileExt == "exe":
                current_path = os.getcwd()
                path = current_path + "/uploadFiles/testExe.exe"
                self.log.info("Path :: '" + str(path) + "' of a file")
                self.sendKeys(path, locator)
            else:
                self.log.error("File not found")
        except Exception as err_msg:
            raise AssertionError("Element :: '" + locator + "' state could not be found \n error:" + str(err_msg))

    def takeScreenshot(self):
        fileName = getUniqueName() + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativePath = screenshotDirectory + fileName
        currntDirectry = os.path.dirname(__file__)
        destinationFile = os.path.join(currntDirectry, relativePath)
        destinationDirectory = os.path.join(currntDirectry, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory: " + destinationFile)

        except:
            self.log.error("### Exception Occurred when taking screenshot")
    def highlight_element(self, locator):
        """
        function to highlight the web element so that we know, we are interacting with right element
        :params: locator - web element locator
        :return: none
        """
        try:
            element = self.getElement(locator)
            # this JS code will change the border of the element with Red color
            self.driver.execute_script("arguments[0].style.border='3px groove red'", element)
            time.sleep(1)
            # this JS is making the border as it was
            self.driver.execute_script("arguments[0].style.border=''", element)
            self.log.info("Element got highlighted with locator" + locator[1])
        except Exception:
            self.log.info("Cannot find element with locator: " + locator[1])

    def waitForElement(self, locator, timeout=10, pollFrequency=0.5, condition="presence_of_element_located",
                       initial_implicit_wait_time=0, final_implicit_wait_time=10):
        self.driver.implicitly_wait(initial_implicit_wait_time)
        try:
            wait = WebDriverWait(
                self.driver,
                timeout,
                poll_frequency=pollFrequency,
                ignored_exceptions=[
                    NoSuchElementException,
                    ElementNotVisibleException,
                    ElementNotSelectableException,
                ],
            )
            if condition == "presence_of_element_located":
                self.log.info(
                    "Waiting for maximum :: " + str(timeout) + " :: seconds for element to be present. " + locator[1])
                element = wait.until(EC.presence_of_element_located(locator))
                # the above case holds the Web element in the element variable
            elif condition == "presence_of_all_elements_located":
                self.log.info(
                    "Waiting for maximum :: " + str(timeout) + " :: seconds for all elements to be present. " + locator[
                        1])
                element = wait.until(EC.presence_of_all_elements_located(locator))
                # the above case holds the Web element(s) (in list form) in the element variable
            elif condition == "element_to_be_clickable":
                element = wait.until(EC.element_to_be_clickable(locator))
                # the above case holds the Web element in the element variable
            elif condition == "visibility_of_element_located":
                self.log.info(
                    "Waiting for maximum :: " + str(timeout) + " :: seconds for element to be visible. " + locator[1])
                element = wait.until(EC.visibility_of_element_located(locator))
                # the above case holds the Web element in the element variable
            elif condition == "visibility_of_any_elements_located":
                self.log.info(
                    "Waiting for maximum :: " + str(timeout) + " :: seconds for element to be clickable. " + locator[1])
                element = wait.until(EC.visibility_of_any_elements_located(locator))
                # the above case holds the Web element(s) (in list form) in the element variable
            elif condition == "invisibility_of_element_located":
                self.log.info(
                    "Waiting for maximum :: " + str(timeout) + " :: seconds for element to be clickable. " + locator[1])
                element = wait.until(EC.invisibility_of_element_located(locator))
                # the above case holds boolean value in the element variable
            else:
                self.log.info("Given condition (" + condition + ") was not found, locator: " + locator[1])
        except Exception as err_msg:
            self.log.info(
                "Wait for element call with the given condition (" + condition + ") was not successful: " + locator[1])
            element = []
        self.driver.implicitly_wait(final_implicit_wait_time)
        return element
