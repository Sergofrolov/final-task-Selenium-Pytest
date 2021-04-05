from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest

@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page = MainPage(browser, link)
    # открываем страницу
    page.open()
    # выполняем метод страницы — переходим на страницу логина
    page.go_to_login_page()
    # переменной login_page присваивается url текущей страницы
    login_page = LoginPage(browser, browser.current_url)
    # выполняются проверки страницы авторизации
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    #Гость открывает главную страницу
    page.open()
    #Переходит в корзину по кнопке в шапке сайта
    page.go_to_basket_page()
    # переменной basket_page присваивается url текущей страницы
    basket_page = BasketPage(browser, browser.current_url)
    #Ожидаем, что в корзине нет товаров
    basket_page.should_not_be_goods_in_basket()
    #Ожидаем, что есть текст о том что корзина пуста
    basket_page.should_be_basket_empty_text()
