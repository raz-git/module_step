from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProducPageLocators
import math
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):
    def add_to_cart(self):
        button = self.browser.find_element(*ProducPageLocators.ADD_BUTTON)
        button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def correct_product_name(self):
        name_in_message = self.browser.find_element(*ProducPageLocators.PRODCUT_NAME_IN_MSG)
        name_product = self.browser.find_element(*ProducPageLocators.PRODCUT_NAME)
        assert name_in_message.text == name_product.text, f'product name - {name_product.text} != name of product in message - {name_in_message.text}'

    def correct_product_price(self):
        product_price = self.browser.find_element(*ProducPageLocators.PRODUCT_PRICE)
        basket_total = self.browser.find_element(*ProducPageLocators.TOTAL_BASKET)
        assert product_price.text == basket_total.text, f'basket = {basket_total.text}, product = {product_price.text}'

    def success_message(self):
        success_msg = self.browser.find_element(*ProducPageLocators.SUCCESS_MESSAGE)
        assert 'has been added to your basket.' or 'был добавлен в вашу корзину.' in success_msg.text, 'success message is not correct'

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProducPageLocators.SUCCESS_MESSAGE), 'success message is presented, but should not be'

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def until_success(self):
        assert self.is_disappeared(*ProducPageLocators.SUCCESS_MESSAGE), 'success message still presented'



