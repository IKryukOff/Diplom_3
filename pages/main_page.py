import allure
from data import Urls, drag_and_drop_js_script
from locators.main_page_locators import IngredientsLocators, MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def go_to_main_page(self) -> None:
        self.driver_get_url(Urls.main_page)
        self.find_visible_element(MainPageLocators.ingredients_section)

    def go_to_order_feed_page(self) -> None:
        self.driver_get_url(Urls.order_feed_page)
        self.find_visible_element(MainPageLocators.order_feed_div)

    @allure.step('Кликаем по элементу "Личный кабинет"')
    def click_profile_text(self) -> None:
        self.click_on_element(MainPageLocators.profile_link_text)

    @allure.step('Кликаем по элементу "Конструктор"')
    def click_constructor_header(self) -> None:
        self.click_on_element(MainPageLocators.constructor_link_text)

    @allure.step('Кликаем по элементу "Лента Заказов"')
    def click_order_feed_header(self) -> None:
        self.click_on_element(MainPageLocators.order_feed_text)

    @allure.step("Кликаем по ингредиенту {name}")
    def click_on_ingredient(self, name: str) -> None:
        self.click_on_element(IngredientsLocators.ingredient_item(name))

    @allure.step("Кликаем по кнопке закрытия Деталей ингредиента")
    def click_close_details_button(self) -> None:
        self.click_on_element(IngredientsLocators.close_details_button)
        self.wait_element_to_be_invisible(IngredientsLocators.ingredient_details_text)

    @allure.step("Получить значение каунтера для ингредиента {name}")
    def get_ingredient_count(self, name: str) -> int:
        return int(self.find_visible_element(IngredientsLocators.ingredient_counter(name)).text)

    @allure.step("Добавить ингредиент {name} в корзину")
    def move_ingredient_to_basket(self, name: str) -> None:
        source = self.find_visible_element(IngredientsLocators.ingredient_item(name))
        target = self.find_visible_element(IngredientsLocators.ingredient_basket)
        # ActionChains drag_and_drop на Firefox не работает, поэтому используем js скрипт
        # ActionChains(self.driver).drag_and_drop(source, target).perform()
        self.driver.execute_script(drag_and_drop_js_script, source, target)

    @allure.step('Кликаем по элементу "Оформить заказ"')
    def click_order_button(self) -> None:
        self.click_on_element(MainPageLocators.order_button)

    def is_order_accepted(self) -> bool:
        return self.find_presence_element(IngredientsLocators.order_start_status).is_displayed()

    def ingredient_details_is_displayed(self) -> bool:
        return self.find_presence_element(
            IngredientsLocators.ingredient_details_text).is_displayed()

    def is_order_feed_opened(self) -> bool:
        return (self.current_url() == Urls.order_feed_page and
                self.find_visible_element(MainPageLocators.order_feed_div) is not None)

    def is_main_page_opened(self) -> bool:
        return (self.current_url() == Urls.main_page and
                self.find_visible_element(MainPageLocators.ingredients_section) is not None)
