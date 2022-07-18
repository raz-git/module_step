from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BUTTON_BASKET = (By.CSS_SELECTOR, '.basket-mini .btn-group .btn')

class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PASS = (By.CSS_SELECTOR, '#id_login-password')
    REGISTER_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASS1 = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_PASS2 = (By.CSS_SELECTOR, '#id_registration-password2')

class ProducPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form .btn-add-to-basket')
    PRODCUT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODCUT_NAME_IN_MSG = (By.CSS_SELECTOR, '#messages .alertinner strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alertinner')
    TOTAL_BASKET = (By.CSS_SELECTOR, '#messages .alert-info .alertinner strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')

class BasketPageLocators():
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner p')
    BASKET_ITEMS = (By.CLASS_NAME, 'basket-items')