from selenium.webdriver.common.by import By


class BasePageLocators:
    loading_img = (By.XPATH, './/img[contains(@class,"Modal_modal__loading")]')
