import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.profile_page import ProfilePage
from selenium.webdriver.remote.webdriver import WebDriver


@allure.parent_suite('Тестирование UI сервиса Stellar Burgers')
@allure.suite('Проверка раздела "Лента заказов"')
class TestOrderFeedPage:
    @allure.sub_suite('Тестирование отображения статуса заказа')
    @allure.title('Проверка открытия окна с деталями заказа после клика на заказ из списка')
    @allure.description('Нажимаем на Ленту заказов -> кликаем на первый заказ')
    def test_click_order_details_opened(self, driver: WebDriver) -> None:
        page = OrderFeedPage(driver)
        page.go_to_order_feed_page()
        page.click_first_order()
        assert page.is_order_info_displayed()

    @allure.sub_suite('Тестирование синхронизации истории заказов на окнах История заказов и '
                      'Лента заказов')
    @allure.title('Проверка наличия созданного заказа как в Истории заказов так и в Ленте Заказов')
    @allure.description('Создаем заказ и запоминаем его ID -> берем список ID-шников заказов из '
                        'Истории заказов и Ленты Заказов -> проверяем наличие ID созданного '
                        'заказа в обоих списках')
    def test_orders_ids_from_profile_exists_on_order_feed(self, login: WebDriver) -> None:
        main_page = MainPage(login)
        profile_page = ProfilePage(login)
        order_feed_page = OrderFeedPage(login)
        order_id = main_page.create_order_and_get_id()
        main_page.click_profile_text()
        orders_id_from_history = profile_page.get_orders_id_list()
        orders_id_from_order_feed = order_feed_page.get_orders_id_list()
        assert (order_id in orders_id_from_history and
                order_id in orders_id_from_order_feed and
                set(orders_id_from_history) & set(orders_id_from_order_feed) != {})

    @allure.sub_suite('Тестирование увеличения счетчика "Выполнено за всё время" при создании')
    @allure.title('Проверка увеличения счетчика "Выполнено за всё время" при создании заказа')
    @allure.description('Запоминаем исходное состояние счетчика -> создаем заказ -> снова берем '
                        'состояние счетчика и сравниваем')
    def test_create_order_all_order_count_increased(self, login: WebDriver) -> None:
        main_page = MainPage(login)
        order_feed_page = OrderFeedPage(login)
        order_count_before = order_feed_page.get_all_time_orders_count()
        main_page.create_order_and_get_id()
        assert order_feed_page.get_all_time_orders_count() > order_count_before

    @allure.sub_suite('Тестирование увеличения счетчика "Выполнено за сегодня" при создании')
    @allure.title('Проверка увеличения счетчика "Выполнено за сегодня" при создании заказа')
    @allure.description('Запоминаем исходное состояние счетчика -> создаем заказ -> снова берем '
                        'состояние счетчика и сравниваем')
    def test_create_order_today_order_count_increased(self, login: WebDriver) -> None:
        main_page = MainPage(login)
        order_feed_page = OrderFeedPage(login)
        order_count_before = order_feed_page.get_today_orders_count()
        main_page.create_order_and_get_id()
        assert order_feed_page.get_today_orders_count() > order_count_before

    @allure.sub_suite('Тестирование списка заказов в разделе "В работе"')
    @allure.title('Проверка наличия ID созданного заказа в списке ID-шников в разделе "В работе"')
    @allure.description('Создаем заказ -> проверяем наличие ID в проверяемом списке')
    def test_create_order_created_id_in_work_list(self, login: WebDriver) -> None:
        main_page = MainPage(login)
        order_feed_page = OrderFeedPage(login)
        order_id = main_page.create_order_and_get_id()
        orders_in_work = order_feed_page.get_orders_id_in_work_list()
        assert order_id in orders_in_work
