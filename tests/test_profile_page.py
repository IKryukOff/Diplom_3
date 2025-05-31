import allure
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
