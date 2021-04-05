from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_goods_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_GOODS_FORMSET), \
        "Goods in basket is presented, but should not be"

    def should_be_basket_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE), \
        "No text that basket is empty"
