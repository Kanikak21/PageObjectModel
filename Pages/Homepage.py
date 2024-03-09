from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class HUbHome(BasePage):

    Industries=(By.CSS_SELECTOR,"li[data-section='Industries']>a")


    def __init__(self, driver):
        super().__init__(driver)

    def homePageClick(self,Industries):
        self.do_click(Industries)
        