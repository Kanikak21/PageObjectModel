import pytest
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from Pages.Homepage import HUbHome

from Config.config import TestData


# print(driver.title)
# if driver.title=='Insurance Brokers | HUB International':
#     assert True

@pytest.mark.usefixtures("init_driver")
class baseTest:
    pass

class Testhub(baseTest):

    @pytest.mark.testTitle
    def test_homePage(self):
        explicit_wait= WebDriverWait(self.driver,20)
        self.driver.get(TestData.baseURL)
        

        
        # # explicit_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"li[data-section='Industries']>a"))) 
        # if headerElements.text=='Industries':
        #     headerElements.click()
        # # print(headerElements)

        HUbHome.homePageClick()

        headerOptions=self.driver.find_elements(By.CSS_SELECTOR,"div[class='container']>div:nth-child(3)>div>div>h5>a")
        # print(headerOptions)
        time.sleep(10)

        for ele in headerOptions:
            if ele.text == 'Agribusiness':
                print(ele.text)
                ele.click()
                break

        # contactUs= explicit_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"a[data-link-text='contact us']")))
        # contactUs.click()

    def clickAgribusiness(self):
        explicit_wait= WebDriverWait(self.driver,20)
        connectToBroker= explicit_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"a[class='btn-primary btn']")))
        # driver.find_element(By.CSS_SELECTOR,"div[class='banner-contact-content']")

        connectToBroker.click()

        firstName=self.driver.find_element(By.XPATH,'//*[@id="CrmItem_FirstNameField"]')
        lastName=self.driver.find_element(By.XPATH,'//*[@id="CrmItem_LastNameField"]')
        jobTitle=self.driver.find_element(By.XPATH,'//*[@id="CrmItem_JobTitle"]')
        email=self.driver.find_element(By.XPATH,'//*[@id="CrmItem_EmailField"]')
        companyName=self.driver.find_element(By.XPATH,'//*[@id="CrmItem_CompanyField"]')
        phone=self.driver.find_element(By.XPATH,'//*[@id="CrmItem_PhoneField"]')
        zipCode=self.driver.find_element(By.XPATH,'//*[@id="CrmItem_CompanyZipCodeField"]')
        noOfEmployees=self.driver.find_element(By.XPATH,'//*[@id="CrmItem_NumberOfEmployees"]')

        firstName.send_keys("Kanika")
        lastName.send_keys("Khattri")
        jobTitle.send_keys("Consultant")
        email.send_keys("knk@gmail.com")
        companyName.send_keys("ABC")
        phone.send_keys("1112228888")
        zipCode.send_keys("N9C1M2")
        noOfEmployees.send_keys("20")

        selectRevenue= self.driver.find_element(By.XPATH,'//*[@id="RevenueList"]')
        select=Select(selectRevenue)
        select.select_by_visible_text("$500,000 to $1.9 Million")

        # driver.find_element(By.XPATH,'//*[@id="recaptcha-anchor"]/div[1]').click()
        self.driver.get_screenshot_as_file("screenshotHUB.png")

        # driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

        submit= self.driver.find_element(By.XPATH,'//*[@id="generalContactForm"]/section[2]/div/div/div/div/div[12]/input')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit)
        # driver.execute_script("arguments[0].scrollIntoView(true);", Phone)

    @pytest.mark.testTitle
    def test_pagetitle(self):
        self.driver.get("https://www.hubinternational.com/")
        pageTitle=self.driver.execute_script("return document.title;")
        print(pageTitle)
        time.sleep(10)

# openURL
# clickBtn
# sendKeys
# screenshot
# executeScript
# dropdown

