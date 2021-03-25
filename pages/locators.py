from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADD_TO_CART_SUCCESS_MESSAGE_GOOD = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    CART_PRICE_NOW = (By.CSS_SELECTOR, ".alert-info strong")
    GOOD_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    GOOD_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
