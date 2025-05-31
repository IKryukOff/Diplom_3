from data.urls import Urls
from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):
    def go_to_profile_page(self) -> None:
        self.driver_get_url(Urls.profile_page)
        self.find_clickable_element(ProfilePageLocators.logout_button)

    def is_profile_page_opened(self) -> bool:
        return (self.current_url() == Urls.profile_page and
                self.find_clickable_element(ProfilePageLocators.logout_button) is not None)
