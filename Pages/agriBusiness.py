from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class agriBusiness(BasePage):
    def __init__(self, driver):
          super().__init__(driver)
        
    firstName=(By.XPATH,'//*[@id="CrmItem_FirstNameField"]')
    lastName=(By.XPATH,'//*[@id="CrmItem_LastNameField"]')
    jobTitle=(By.XPATH,'//*[@id="CrmItem_JobTitle"]')
    email=(By.XPATH,'//*[@id="CrmItem_EmailField"]')
    companyName=(By.XPATH,'//*[@id="CrmItem_CompanyField"]')
    phone=(By.XPATH,'//*[@id="CrmItem_PhoneField"]')
    zipCode=(By.XPATH,'//*[@id="CrmItem_CompanyZipCodeField"]')
    noOfEmployees=(By.XPATH,'//*[@id="CrmItem_NumberOfEmployees"]')   



    def enter_text_agriform(self):
            self.enter_text(self.firstName,"Kanika")
            self.enter_text(self.lastName,"Khattri")