from selenium.webdriver.common.by import By


class ProfilePageLocators:
    info_text = (By.XPATH, './/p[contains(text(),"персональные данные")]')
    history_link_text = (By.XPATH, './/a[text()="История заказов"]')
    constructor_link_text = (By.XPATH, './/p[text()="Конструктор"]')
    logout_button = (By.XPATH, './/button[text()="Выход"]')
    order_history_div = (By.XPATH, './/div[contains(@class,"orderHistory")]')
