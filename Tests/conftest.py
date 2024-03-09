from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture(scope='class')
def init_driver(request):
    
    options= webdriver.ChromeOptions()
    options.add_argument("--ignore-ssl-errors")
    driver= webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.maximize_window()
    request.cls.driver= driver 
    yield
    driver.close() 