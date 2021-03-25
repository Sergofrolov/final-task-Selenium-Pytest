from pages.main_page import MainPage
from pages.login_page import LoginPage


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
