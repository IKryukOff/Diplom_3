import allure
import pytest
from data import INGREDIENT_NAMES
from pages.main_page import MainPage
from selenium.webdriver.remote.webdriver import WebDriver


@allure.parent_suite('Тестирование UI сервиса Stellar Burgers')
@allure.suite('Проверка основного функционала')
class TestMainPage:
    @allure.sub_suite('Тестирование перехода на Конструктор')
    @allure.title('Проверка перехода на Конструктор бургера по клику на кнопку "Конструктор"')
    @allure.description('Открываем cтраницу ленты заказов, кликаем на "Контсруктор"')
    def test_click_constructor_ingredients_show(self, driver: WebDriver) -> None:
        main_page = MainPage(driver)
        main_page.go_to_order_feed_page()
        main_page.click_constructor_header()
        assert main_page.is_main_page_opened()

    @allure.sub_suite('Тестирование перехода перехода на Ленту Заказов')
    @allure.title('Проверка перехода на Ленту Заказов бургера по клику на кнопку "Лента Заказов"')
    @allure.description('Открываем главную страницу, кликаем на "Лента Заказов"')
    def test_click_order_feed_header_order_feed_show(self, driver: WebDriver) -> None:
        main_page = MainPage(driver)
        main_page.go_to_main_page()
        main_page.click_order_feed_header()
        assert main_page.is_order_feed_opened()

    @allure.sub_suite('Тестирование открытия Деталей инредиента')
    @allure.title('Проверка открытия информации об ингредиенте после клика на него')
    @allure.description('Открываем главную страницу, кликаем на ингредент')
    @pytest.mark.parametrize('ingredient_name', INGREDIENT_NAMES)
    def test_click_ingredient_details_show(self, driver: WebDriver,
                                           ingredient_name: str) -> None:
        main_page = MainPage(driver)
        main_page.go_to_main_page()
        main_page.click_on_ingredient(ingredient_name)
        assert main_page.ingredient_details_is_displayed()

    @allure.sub_suite('Тестирование закрытия окна Деталей инредиента')
    @allure.title('Проверка закрытия информации об ингредиенте после клика на кнопку крестика')
    @allure.description('Открываем главную страницу -> кликаем на ингредент -> кликаем на крестик')
    @pytest.mark.parametrize('ingredient_name', INGREDIENT_NAMES)
    def test_click_close_ingredient_details_closed(self, driver: WebDriver,
                                                   ingredient_name: str) -> None:
        main_page = MainPage(driver)
        main_page.go_to_main_page()
        main_page.click_on_ingredient(ingredient_name)
        main_page.click_close_details_button()
        assert main_page.ingredient_details_is_displayed() is False

    @allure.sub_suite('Тестирование изменение каунтера ингредиента')
    @allure.title('Проверка того, что при добавлении ингредиента в заказ, увеличивается каунтер '
                  'данного ингредиента')
    @allure.description('Открываем главную страницу -> перемещаем ингредиент в корзину -> '
                        'сравниваем значения каунтера ингредиента')
    @pytest.mark.parametrize('ingredient_name', INGREDIENT_NAMES)
    def test_drag_and_drop_ingredient_counter_changed(self, driver: WebDriver,
                                                      ingredient_name: str) -> None:
        main_page = MainPage(driver)
        main_page.go_to_main_page()
        count_before = main_page.get_ingredient_count(ingredient_name)
        main_page.move_ingredient_to_basket(ingredient_name)
        assert main_page.get_ingredient_count(ingredient_name) > count_before

    @allure.sub_suite('Тестирование создания заказа авторизованным пользователем')
    @allure.title('Проверка создания заказа авторизованным пользователем по кнопке Оформить заказ')
    @allure.description('При условии авторицации открываем главную страницу -> перемещаем '
                        'ингредиент в корзину -> нажимаем на Оформить заказ -> Ожидаем сообщение '
                        'со статусом заказа')
    def test_create_order_by_authed_user_order_accepted(self, login: WebDriver) -> None:
        main_page = MainPage(login)
        main_page.move_ingredient_to_basket(INGREDIENT_NAMES[0])
        main_page.click_order_button()
        assert main_page.is_order_accepted()
