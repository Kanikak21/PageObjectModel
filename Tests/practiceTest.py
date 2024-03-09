from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome()
driver.implicitly_wait(5)
# driver.get("https://www.rediff.com")
driver.get("https://www.hubinternational.com/en-CA/contact-us/personal-insurance/")

print(driver.title)
# driver.find_element(By.NAME,'q').send_keys("PGWP Canada")
# ele= driver.find_elements(By.CSS_SELECTOR, "ul.G43f7e li>div>div:nth-child(2) div>div:nth-child(1)>span")
# #print(ele)


# for x in ele:
#     print(x.text)
#     if x.text=='pgwp canada requirements':
#        x.click()
#        break

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# image= driver.find_element(By.XPATH, '//div[@class="bigstory"]/h5/a/img')
# driver.execute_script("arguments[0].style.border= '10px solid red'",image)

# inner_text= driver.execute_script("return document.documentElement.innerText")
# print(inner_text)

print(driver.execute_script("return navigator.userAgent;    "))


Fname= driver.find_element(By.XPATH,'//*[@id="CrmItem_FirstNameField"]')
driver.execute_script("arguments[0].value='Kanika'",Fname)
time.sleep(10)