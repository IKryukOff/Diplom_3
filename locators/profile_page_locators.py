from selenium.webdriver.common.by import By


class ProfilePageLocators:
    info_text = (By.XPATH, './/p[contains(text(),"персональные данные")]')
    history_link_text = (By.XPATH, './/a[text()="История заказов"]')
    constructor_link_text = (By.XPATH, './/p[text()="Конструктор"]')
    main_logo = (By.CLASS_NAME, 'AppHeader_header__logo__2D0X2')
    logout_button = (By.XPATH, './/button[text()="Выход"]')
