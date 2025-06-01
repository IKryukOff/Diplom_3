import allure
from data.urls import Urls
from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):
    def go_to_profile_page(self) -> None:
        self.driver_get_url(Urls.profile_page)
        self.find_clickable_element(ProfilePageLocators.logout_button)

    @allure.step('Кликаем на кнопку "История заказов"')
    def click_order_history(self) -> None:
        self.click_on_element(ProfilePageLocators.history_link_text)

    @allure.step('Кликаем на кнопку "Выход')
    def click_logout_button(self) -> None:
        self.click_on_element(ProfilePageLocators.logout_button)

    @allure.step('Ждем обновления страницы после logout')
    def wait_change_profile_page_after_logout(self) -> None:
        self.wait_change_url(Urls.profile_page)

    def is_order_history_opened(self) -> bool:
        return (self.current_url() == Urls.order_hstory_page and
                self.find_visible_element(ProfilePageLocators.order_history_div) is not None)

    def is_profile_page_opened(self) -> bool:
        return (self.current_url() == Urls.profile_page and
                self.find_clickable_element(ProfilePageLocators.logout_button) is not None)
