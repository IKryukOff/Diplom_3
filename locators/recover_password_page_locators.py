from selenium.webdriver.common.by import By


class RecoverPasswordPageLocators:
    email_field = (By.XPATH, './/label[text()="Email"]//parent::*/input')
    recover_button = (By.XPATH, '//button[text()="Восстановить"]')
    save_button = (By.XPATH, '//button[text()="Сохранить"]')
    show_password_switcher = (By.XPATH, '//div[contains(@class,"icon-action")]')
    active_input_label = (By.XPATH, './/div[contains(@class,"input_status_active")]/label')
