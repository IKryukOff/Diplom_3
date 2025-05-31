import allure
from data.urls import Urls
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver_get_url(Urls.login_page)

    @allure.step('Кликаем по элементу "Восстановить пароль"')
    def click_recover_password_text(self) -> None:
        self.click_on_element(LoginPageLocators.recover_password_text_href)
