from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def should_be_message_good_added_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_SUCCESS_MESSAGE_GOOD), "Add to cart message is not presented"

    def check_message_good_added_to_cart(self):
        good_message = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_SUCCESS_MESSAGE_GOOD)
        good_message_text = good_message.text
        good_name = self.browser.find_element(*ProductPageLocators.GOOD_NAME)
        good_name_text = good_name.text
        assert good_name_text == good_message_text, "Good name in add to cart message does not match with name of added good"

    def should_be_cart_price(self):
        assert self.is_element_present(*ProductPageLocators.CART_PRICE_NOW), "Cart price is not presented"
    
    def check_cart_price_is_good_price(self):
        cart_price = self.browser.find_element(*ProductPageLocators.CART_PRICE_NOW)
        cart_price_text = cart_price.text
        good_price = self.browser.find_element(*ProductPageLocators.GOOD_PRICE)
        good_price_text = good_price.text
        assert cart_price_text == good_price_text, "Cart price does not fit to price of added good"

    def success_message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is not disappeared, but should be"

