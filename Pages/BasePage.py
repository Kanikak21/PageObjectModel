from selenium.webdriver import  ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self,driver):
        self.driver=driver

    def do_click(self,locator):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(locator)).click()

    def enter_text(self,locator,data):
        self.driver.find_element(locator).sendkeys(data)