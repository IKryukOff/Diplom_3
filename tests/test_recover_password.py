import allure
from data.urls import Urls
from faker import Faker
from pages.login_page import LoginPage
from pages.recover_passord_page import RecoverPasswordPage
from selenium.webdriver.remote.webdriver import WebDriver


@allure.parent_suite('Тестирование UI сервиса Stellar Burgers')
@allure.suite('Восстановление пароля')
class TestRecoverPassword:
    @allure.sub_suite('Тестирование перехода на страницу восстановления пароля (ввод email)')
    @allure.title('Проверка перехода из окна логин на окно восстановления парля при нажатии на '
                  'кнопку "Восстановить пароль"')
    @allure.description('На странице логина нажимаем на "Восстановить пароль" и проверям, что '
                        'произошел переход на страницу восстановления пароля (указание почты)')
    def test_click_recover_password_on_login_open_forgot_password_page(self,
                                                                       driver: WebDriver) -> None:
        login_page = LoginPage(driver)
        login_page.click_recover_password_text()
        assert login_page.current_url() == Urls.recover_password_forgot_page

    @allure.sub_suite('Тестирование перехода на страницу восстановления пароля (сменя пароля)')
    @allure.title('Проверка перехода на страницу смены пароля после указания почты для '
                  'восстановления пароля')
    @allure.description('На странице восстановления пароля вводим почту и проверям, что '
                        'после нажатия на кнопку "Восстановить" произошел переход на страницу '
                        'смены пароля')
    def test_click_recover_password_on_forgot_open_reset_password_page(self,
                                                                       driver: WebDriver) -> None:
        recover_page = RecoverPasswordPage(driver)
        recover_page.fillup_email(Faker().email())
        recover_page.click_recover_password_button()
        recover_page.wait_change_forgot_page()
        assert recover_page.current_url() == Urls.recover_password_reset_page

    @allure.sub_suite('Тестирование кнопки показать/скрыть пароль')
    @allure.title('Проверка выделения поля ввода пароля при нажатии на кнопку показать/скрыть '
                  'пароль')
    @allure.description('На этапе смены пароля нажимаем на кнопку показать/скрыть пароль и '
                        'проверяем активный элемент')
    def test_switch_show_password_input_password_is_active(self,
                                                           driver: WebDriver) -> None:
        recover_page = RecoverPasswordPage(driver)
        recover_page.fillup_email(Faker().email())
        recover_page.click_recover_password_button()
        recover_page.wait_change_forgot_page()
        recover_page.click_switch_show_password_button()
        assert recover_page.find_active_input().text == 'Пароль'
