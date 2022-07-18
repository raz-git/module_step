from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasketPage(BasePage):
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_basket_message_present(self):
        empty_msg = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE)
        assert 'Your basket is empty.' in empty_msg.text, f'basket message incorrect - {empty_msg.text}'

    def is_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), 'items in basket are present, but should not be'