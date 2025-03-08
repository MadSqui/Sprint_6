import pytest
import allure
from urls import order_page_url, main_page_url
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


class TestTransition:
    @allure.title('После нажатия на логотип "Самокат" в шапке происходит переход на главную Самоката')
    def test_click_on_the_scooter_logo_redirect_to_the_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_main_page()
        main_page.click_the_scooter_logo()
        assert main_page.is_current_url(main_page_url)

    @allure.title('После нажатия на логотип "Яндекс" в шапке происходит переход на главную Дзена')
    def test_click_on_the_yandex_logo_redirect_to_the_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_main_page()
        main_page.click_on_logo_yandex()
        main_page.wait_for_two_windows()
        main_page.redirect_to_dzen()
        assert main_page.current_url_contains('dzen.ru')