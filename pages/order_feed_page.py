import allure
from data import Urls
from locators.main_page_locators import MainPageLocators
from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    def go_to_order_feed_page(self) -> None:
        self.driver_get_url(Urls.order_feed_page)
        self.find_visible_element(MainPageLocators.order_feed_div)

    @allure.step('Кликаем по элементу "Лента Заказов"')
    def click_order_feed_header(self) -> None:
        self.click_on_element(MainPageLocators.order_feed_text)

    @allure.step('Кликаем по первому (верхнему) заказу из Ленты заказов')
    def click_first_order(self) -> None:
        self.click_on_element(OrderFeedPageLocators.order_list)

    @allure.step('Получить список номеров заказов из Ленты заказов')
    def get_orders_id_list(self) -> list[int]:
        self.click_order_feed_header()
        orders_id_str = self.find_visible_elements(OrderFeedPageLocators.orders_id_list)
        return list(map(lambda x: int(x.text.replace('#0', '')), orders_id_str))

    @allure.step('Получить список номеров заказов со статусом В работе')
    def get_orders_id_in_work_list(self) -> list[int]:
        self.click_order_feed_header()
        orders_id_str = self.find_visible_elements(OrderFeedPageLocators.orders_in_work_list)
        return list(map(lambda x: int(x.text[1:]), orders_id_str))

    @allure.step('Получить общее количество созданных заказов')
    def get_all_time_orders_count(self) -> int:
        self.click_order_feed_header()
        return int(self.find_visible_element(OrderFeedPageLocators.all_time_orders_count).text)

    @allure.step('Получить количество созданных за сегодня заказов')
    def get_today_orders_count(self) -> int:
        self.click_order_feed_header()
        return int(self.find_visible_element(OrderFeedPageLocators.today_order_count).text)

    def is_order_info_displayed(self) -> bool:
        return self.find_presence_element(OrderFeedPageLocators.order_info).is_displayed()
