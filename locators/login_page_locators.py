from selenium.webdriver.common.by import By


class LoginPageLocators:
    title_text = (By.XPATH, './/h2[text()="Вход"]')
    login_button = (By.XPATH, './/button[text()="Войти"]')
    email_field = (By.XPATH, './/label[text()="Email"]//parent::*/input')
    password_field = (By.XPATH, './/input[@type="password"]')
    recover_password_text_href = (By.XPATH, './/a[contains(@href, "/forgot-password")]')
