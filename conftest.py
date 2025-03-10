import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

@pytest.fixture(scope="function")
def driver():
    options = FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def main_page(driver):
    main_page = MainPage(driver)
    main_page.get_url("https://qa-scooter.praktikum-services.ru/")
    return main_page

@pytest.fixture(scope="function")
def order_page(driver):
    page = OrderPage(driver)
    page.get_url("https://qa-scooter.praktikum-services.ru/order")
    page.click_on_cookie()
    return page