from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")

class BasketPageLocators():
    BASKET_GOODS_FORMSET = (By.CSS_SELECTOR, "#basket_formset")
    BASKET_HEADER = (By.CSS_SELECTOR, ".page-header.action")
    BASKET_IS_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADD_TO_CART_SUCCESS_MESSAGE_GOOD = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    CART_PRICE_NOW = (By.CSS_SELECTOR, ".alert-info strong")
    GOOD_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    GOOD_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
