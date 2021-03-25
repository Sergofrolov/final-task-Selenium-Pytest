from pages.product_page import ProductPage
import pytest

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
