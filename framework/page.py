from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Page:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find_element(self, locator, by=AppiumBy.XPATH):
        return self.wait.until(ec.presence_of_element_located((by, locator)))

    @staticmethod
    def click_element(element):
        element.click()
