import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from selenium.webdriver.remote.webdriver import WebDriver


@allure.parent_suite('Тестирование UI сервиса Stellar Burgers')
@allure.suite('Личный кабинет')
class TestProfilePage:
    @allure.sub_suite('Тестирование перехода на страницу личного кабинета')
    @allure.title('Проверка перехода из главного окна на страницу личного кабинета авторизованного '
                  'пользователя')
    @allure.description('При условии авторицации пользователя нажимаем на главной странице на '
                        'кнопку "Личный Кабинет"')
    def test_click_profile_text_profile_page_opened(self, driver: WebDriver, login: None) -> None:
        main_page = MainPage(driver)
        main_page.go_to_main_page()
        main_page.click_profile_text()
        assert ProfilePage(driver).is_profile_page_opened()

    @allure.sub_suite('Тестирование перехода в раздел истории заказов')
    @allure.title('Проверка перехода в раздел Истории заказов с Личного кабинета')
    @allure.description('При условии авторицации пользователя нажимаем на главной странице на '
                        'кнопку "Личный Кабинет" -> "История заказов"')
    def test_click_order_history_text_order_history_opened(self, driver: WebDriver,
                                                           login: None) -> None:
        main_page = MainPage(driver)
        main_page.go_to_main_page()
        main_page.click_profile_text()
        profile_page = ProfilePage(driver)
        profile_page.click_order_history()
        assert profile_page.is_order_history_opened()

    @allure.sub_suite('Тестирование выхода из аккаунта')
    @allure.title('Проверка выхода из аккаунта по кнопке "Выйти" в Личном кабинете')
    @allure.description('При условии авторицации пользователя нажимаем на главной странице на '
                        'кнопку "Личный Кабинет" -> "Выйти"')
    def test_click_logout_login_page_opened(self, driver: WebDriver, login: None) -> None:
        main_page = MainPage(driver)
        main_page.go_to_main_page()
        main_page.click_profile_text()
        profile_page = ProfilePage(driver)
        profile_page.click_logout_button()
        profile_page.wait_change_profile_page_after_logout()
        assert LoginPage(driver).is_login_page_opened()
