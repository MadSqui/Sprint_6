import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators
from data import ExpectedText, USER_1, USER_2

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Принимаем куки')
    def click_on_cookie(self):
        self.click_on_element(MainPageLocators.COOKIE)

    @allure.step('Ожидание загрузки страницы заказа')
    def wait_for_order_page(self):
        self.wait_for_element_to_be_clickable(OrderPageLocators.COOKIE_ACCEPT_BUTTON)
        self.click_on_element(OrderPageLocators.COOKIE_ACCEPT_BUTTON)

    @allure.step('Заполнение полей "Для кого самокат"')
    def fill_user_data(self, user_data=USER_1):
        self.set_text_to_element(OrderPageLocators.NAME_FIELD, user_data["name"])
        self.set_text_to_element(OrderPageLocators.LAST_NAME_F, user_data["last_name"])
        self.set_text_to_element(OrderPageLocators.ADDRESS_F, user_data["address"])
        self.click_on_element(OrderPageLocators.METRO_FIELD)
        self.click_on_element(OrderPageLocators.STATION_NAME)
        self.set_text_to_element(OrderPageLocators.PHONE_FIELD, user_data["phone_number"])
        self.click_on_element(OrderPageLocators.FURTHER_BUTTON)

    @allure.step('Заполнение полей "Про аренду"')
    def fill_rental_options(self, user_data=USER_1):
        if user_data['delivery_date'] == OrderPageLocators.CALENDAR_DATE_TODAY:
            self.click_on_element(OrderPageLocators.INPUT_DELIVERY_DATE)
            self.click_on_element(OrderPageLocators.CALENDAR_DATE_TODAY)
        elif user_data['delivery_date'] == OrderPageLocators.CALENDAR_DATE_TOMORROW:
            self.click_on_element(OrderPageLocators.INPUT_DELIVERY_DATE)
            self.click_on_element(OrderPageLocators.CALENDAR_DATE_TOMORROW)

        if user_data['rental_period'] == OrderPageLocators.RENTAL_PERIOD_1_DAY:
            self.click_on_element(OrderPageLocators.FIELD_RENT_LIMIT)
            self.click_on_element(OrderPageLocators.RENTAL_PERIOD_1_DAY)
        elif user_data['rental_period'] == OrderPageLocators.RENTAL_PERIOD_2_DAYS:
            self.click_on_element(OrderPageLocators.FIELD_RENT_LIMIT)
            self.click_on_element(OrderPageLocators.RENTAL_PERIOD_2_DAYS)

        self.click_on_element(OrderPageLocators.INPUT_CHECKBOX_COLOR_BLACK)
        self.set_text_to_element(OrderPageLocators.COMMENT_FIELD, user_data["comment"])

    @allure.step('Подтверждение заказа')
    def confirm_order(self):
        self.click_on_element(OrderPageLocators.ORDER_BUTTON_ORDER_PAGE)
        self.click_on_element(OrderPageLocators.CONFIRMATION_BUTTON)

    @allure.step('Проверка успешного оформления заказа')
    def check_order_confirmation(self):
        return self.get_text_from_element(OrderPageLocators.ORDER_DONE) == ExpectedText.ORDER_CREATED_TEXT

    @allure.step('Полное заполнение формы заказа')
    def make_order(self, user_data=USER_1):
        self.fill_user_data(user_data)
        self.fill_rental_options(user_data)
        self.confirm_order()

    @allure.step('Получаем и сравниваем текст элемента окна готовности заказа')
    def check_order_created(self):
        actual_text = self.get_text_from_element(OrderPageLocators.ORDER_DONE)
        return actual_text == ExpectedText.ORDER_CREATED_TEXT