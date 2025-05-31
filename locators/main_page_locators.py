from selenium.webdriver.common.by import By


class MainPageLocators:
    profile_link_text = (By.XPATH, './/p[text()="Личный Кабинет"]')
    login_button = (By.XPATH, './/button[text()="Войти в аккаунт"]')
    order_button = (By.XPATH, './/button[text()="Оформить заказ"]')
    constructor_link_text = (By.XPATH, './/p[text()="Конструктор"]')
    buns_tab = (By.XPATH, './/span[text()="Булки"]/parent::*')
    sauces_tab = (By.XPATH, './/span[text()="Соусы"]/parent::*')
    fillings_tab = (By.XPATH, './/span[text()="Начинки"]/parent::*')
    active_tab_class = 'tab_tab_type_current__2BEPc'
