import allure
from data.urls import Urls
from locators.recover_password_page_locators import RecoverPasswordPageLocators
from pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebElement


class RecoverPasswordPage(BasePage):
    def go_to_recover_password_page(self) -> None:
        self.driver_get_url(Urls.recover_password_forgot_page)
        self.find_clickable_element(RecoverPasswordPageLocators.recover_button)

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
        return self.find_visible_element(RecoverPasswordPageLocators.active_input_label)

    @allure.step('Ждем обновления страницы после указания почты')
    def wait_change_forgot_page(self) -> None:
        self.wait_change_url(Urls.recover_password_forgot_page)

    def is_forgot_password_page_opened(self) -> bool:
        return (self.current_url() == Urls.recover_password_forgot_page and
                self.find_clickable_element(RecoverPasswordPageLocators.recover_button) is not None)

    def is_reset_password_page_opened(self) -> bool:
        return (self.current_url() == Urls.recover_password_reset_page and
                self.find_clickable_element(RecoverPasswordPageLocators.save_button) is not None)
