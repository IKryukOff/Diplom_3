import allure
from data.urls import Urls
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def go_to_main_page(self) -> None:
        self.driver_get_url(Urls.main_page)
        self.find_clickable_element(MainPageLocators.order_button)

    @allure.step('Кликаем по элементу "Личный кабинет"')
    def click_profile_text(self) -> None:
        self.click_on_element(MainPageLocators.profile_link_text)

    def is_main_page_opened(self) -> bool:
        return (self.current_url() == Urls.main_page and
                self.find_clickable_element(MainPageLocators.order_button) is not None)
