import allure
from data.urls import Urls
from locators.recover_password_page_locators import RecoverPasswordPageLocators
from pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver, WebElement


class RecoverPasswordPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver_get_url(Urls.recover_password_forgot_page)

    @allure.step('Заполняем поле "Email"')
    def fillup_email(self, email: str) -> None:
        self.send_keys_into_field(RecoverPasswordPageLocators.email_field, email)

    @allure.step('Кликаем по кнопке "Восстановить"')
    def click_recover_password_button(self) -> None:
        self.click_on_element(RecoverPasswordPageLocators.recover_button)

    @allure.step('Кликаем по элементу "Показать/Скрыть пароль"')
    def click_switch_show_password_button(self) -> None:
        self.click_on_element(RecoverPasswordPageLocators.show_password_switcher)

    @allure.step('Находим активное поле ввода')
    def find_active_input(self) -> WebElement:
        return self.find_element(RecoverPasswordPageLocators.active_input_label)

    @allure.step('Ждем обновления страницы после указания почты')
    def wait_change_forgot_page(self) -> None:
        self.wait_change_url(Urls.recover_password_forgot_page)
