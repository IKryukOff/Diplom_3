from selenium.webdriver.common.by import By


class MainPageLocators:
    profile_link_text = (By.XPATH, './/p[text()="Личный Кабинет"]')
    login_button = (By.XPATH, './/button[text()="Войти в аккаунт"]')
    order_button = (By.XPATH, './/button[text()="Оформить заказ"]')
    constructor_link_text = (By.XPATH, './/p[text()="Конструктор"]')
    order_feed_text = (By.XPATH, './/p[text()="Лента Заказов"]')
    ingredients_section = (By.XPATH, './/section[contains(@class,"BurgerIngredients")]')
    buns_tab = (By.XPATH, './/span[text()="Булки"]/parent::*')
    sauces_tab = (By.XPATH, './/span[text()="Соусы"]/parent::*')
    fillings_tab = (By.XPATH, './/span[text()="Начинки"]/parent::*')
    order_feed_div = (By.XPATH, './/div[contains(@class,"orderFeed")]')
    active_tab_class = 'tab_tab_type_current__2BEPc'


class IngredientsLocators:
    bun_r2_d3 = (By.XPATH, './/p[text()="Флюоресцентная булка R2-D3"]/parent::a[@draggable]')
    sauce_spicy_x = (By.XPATH, './/p[text()="Соус Spicy-X"]/parent::a[@draggable]')
    filling_cheese = (By.XPATH, './/p[text()="Сыр с астероидной плесенью"]/parent::a[@draggable]')

    ingredient_details_text = (By.XPATH, './/h2[text()="Детали ингредиента"]')
    close_details_button = (
        By.XPATH, './/h2[text()="Детали ингредиента"]/../../button[contains(@class,"close")]')
