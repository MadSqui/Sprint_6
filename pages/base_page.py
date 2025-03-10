from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
import allure



class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание элемента')
    def wait_for_element(self, locator, timeout=Data.WAIT_TIME) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step('Ожидание кликабельности элемента')
    def wait_for_element_to_be_clickable(self, locator, timeout=30) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step('Ожидание видимости элемента')
    def wait_for_element_to_be_visible(self, locator, timeout=30) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step('Загружаем страницу')
    def get_url(self, url):
        self.driver.get(url)
        try:
            WebDriverWait(self.driver, Data.WAIT_TIME).until(
                EC.presence_of_all_elements_located((By.TAG_NAME, "body"))
            )
        except Exception as e:
            raise Exception(f"Failed to load page. Error: {e}")

    @allure.step('Поиск элемента с ожиданием')
    def find_element_and_wait(self, locator):
        return self.wait_for_element_to_be_visible(locator)

    @allure.step('Клик на элемент')
    def click_on_element(self, locator):
        element = WebDriverWait(self.driver, Data.WAIT_TIME).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    @allure.step('Получение текста элемента')
    def get_text_from_element(self, locator):
        element = self.find_element_and_wait(locator)
        return element.text

    @allure.step('Ввод текста в поле')
    def set_text_to_element(self, locator, text):
        element = self.find_element_and_wait(locator)
        element.clear()
        element.send_keys(text)

    @allure.step('Скролл до элемента')
    def scroll_page(self, locator):
        self.scroll_to_element(locator)

    @allure.step('Форматирование локатора')
    def reformate_locator(self, locator_template, value):
        by, selector = locator_template
        formatted_selector = selector.format(value)
        return by, formatted_selector

    @allure.step('Переключение на вторую вкладку')
    def switch_to_second_browser_window(self):
        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[1])
        else:
            raise Exception("Second browser window not found")

    @allure.step('Получение текущего URL')
    def get_current_url(self):
        current_url = self.driver.current_url
        if not current_url:
            raise Exception("Current URL is empty or not loaded")
        return current_url

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator, timeout=15):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Сравнить url')
    def is_current_url(self, url):
        return self.driver.current_url == url

    @allure.step('Сравнить, что url содержит нужный адрес')
    def current_url_contains(self, url_part):
        return url_part in self.driver.current_url

    @allure.step('Дождаться открытия окон')
    def wait_for_two_windows(self):
        WebDriverWait(self.driver, 15).until(EC.number_of_windows_to_be(2))
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)

    @allure.step('Дождаться перехода на сайт "дзена"')
    def wait_url_change(self, url, timeout=90):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(url))