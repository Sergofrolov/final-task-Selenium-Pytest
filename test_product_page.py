from pages.product_page import ProductPage
import pytest

@pytest.mark.skip
@pytest.mark.parametrize('promolink', ["0",
                                  "1",
                                  "2",
                                  "3",
                                  "4",
                                  "5",
                                  "6",
                                  pytest.param("7", marks=pytest.mark.xfail),
                                  "8",
                                  "9"])

def test_guest_can_add_product_to_basket(browser, promolink):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promolink}"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page = ProductPage(browser, link)
    # открываем страницу
    page.open()
    # выполняем метод страницы — добавляем товар в корзину
    page.add_to_cart()
    # Получение проверочного кода
    page.solve_quiz_and_get_code()
    # проверка вывода сообщения о том, что товар добавлен в корзину
    page.should_be_message_good_added_to_cart()
    # название товара в сообщении должно совпадать с добавленным товаром
    page.check_message_good_added_to_cart()
    # проверка вывода сообщения со стоимостью корзины
    page.should_be_cart_price()
    # cтоимость корзины совпадает с ценой товара
    page.check_cart_price_is_good_price()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()   

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    #Открываем страницу товара
    page.open()
    #Добавляем товар в корзину
    page.add_to_cart()
    #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.should_not_be_success_message()

@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    #Открываем страницу товара
    page.open()
    #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.should_not_be_success_message()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    #Открываем страницу товара
    page.open()
    #Добавляем товар в корзину
    page.add_to_cart()
    #Проверяем, что нет сообщения об успехе с помощью is_disappeared
    page.success_message_disappeared_after_adding_product_to_basket()
    


