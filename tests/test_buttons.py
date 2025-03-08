import pytest
import allure
from urls import order_page_url, main_page_url
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators

class TestButtons:
    @allure.title('После нажатия на "Заказать" в шапке страницы происходит переход на оформление заказа')
    def test_click_on_the_order_button_page_header_redirect_to_order(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_element(MainPageLocators.PAGE)
        main_page.click_on_order_button(MainPageLocators.ORDER_BUTTON_TOP)
        assert main_page.is_current_url(order_page_url)

    @allure.title('Нажатие на "Заказать" внизу страницы ведет на страницу оформления заказа')
    def test_click_on_the_order_button_below_redirect_to_order(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_element(MainPageLocators.PAGE)
        main_page.scroll_and_click_order_button_below()
        assert main_page.is_current_url(order_page_url)