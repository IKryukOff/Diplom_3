from typing import Any, Generator

import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request) -> Generator[WebDriver, Any, None]:
    driver: WebDriver
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
    yield driver
    driver.quit()
