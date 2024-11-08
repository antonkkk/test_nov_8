from selenium.webdriver.chrome.options import  Options
import pytest
from selenium import webdriver

@pytest.fixture()
def driver():   #browser
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.close()