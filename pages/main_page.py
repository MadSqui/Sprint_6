from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидание загрузки главной страницы')
    def wait_for_main_page(self):
        self.wait_for_element(MainPageLocators.PAGE)

    @allure.step('Принимаем куки')
    def click_on_cookie(self):
        self.click_on_element(MainPageLocators.COOKIE)

    @allure.step('Скролл страницы до последнего вопроса')
    def scroll_page_to_last_question(self):
        last_question = self.wait_for_element(MainPageLocators.QUESTION_LAST)
        self.driver.execute_script("arguments[0].scrollIntoView();", last_question)

    @allure.step('Кликаем на вопрос')
    def click_on_question(self, number):
        question_locator = self.reformate_locator(MainPageLocators.QUESTION, number)
        self.click_on_element(question_locator)

    @allure.step('Получаем текст ответа')
    def get_text_from_answer(self, number):
        answer_locator = self.reformate_locator(MainPageLocators.ANSWER, number)
        return self.get_text_from_element(answer_locator)

    @allure.step('Клик на вопрос и получение текста ответа')
    def click_to_question_get_answer(self, number):
        self.click_on_question(number)
        return self.get_text_from_answer(number)

    @allure.step('Клик на кнопку "Заказать"')
    def click_on_order_button(self, button):
        self.click_on_element(button)

    @allure.step('Клик на логотип самоката')
    def click_the_scooter_logo(self):
        self.click_on_element(MainPageLocators.SCOOTER_LINK)

    @allure.step('Клик на лого Яндекс')
    def click_on_logo_yandex(self):
        self.click_on_element(MainPageLocators.LOGO_YANDEX)

    @allure.step('Поиск кнопки "Найти" на странице Дзена')
    def search_find_button(self):
        self.switch_to_second_browser_window()
        find_button = self.wait_for_element(MainPageLocators.BUTTON_FIND)
        return find_button.is_displayed()

    @allure.step('Ожидание перехода на "Дзен"')
    def redirect_to_dzen(self):
        self.wait_url_change('dzen')

    @allure.step('Скролл и клик на кнопку Заказать внизу страницы')
    def scroll_and_click_order_button_below(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BELOW)
        self.click_on_element(MainPageLocators.ORDER_BUTTON_BELOW, timeout=50)