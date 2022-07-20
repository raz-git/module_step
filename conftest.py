import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: en, ru, es..")

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


