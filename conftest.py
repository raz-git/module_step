import time
from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    yield browser
    print("\nquit browser..")
    #time.sleep(3)
    browser.quit()