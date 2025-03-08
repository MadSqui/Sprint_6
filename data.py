from locators.order_page_locators import OrderPageLocators
from data_day import DataDay

USER_1 = {
    "name": "Максим",
    "last_name": 'Волшебный',
    "address": 'ул. Перерва, 53',
    "phone_number": '+76669995522',
    'delivery_date': OrderPageLocators.CALENDAR_DATE_TODAY,
    'rental_period': OrderPageLocators.RENTAL_PERIOD_1_DAY,
    "comment": 'Позвони на АТС'
}

USER_2 = {
    "name": "Скволл",
    "last_name": 'Леонхарт',
    "address": 'ул. Усачева, 3',
    "phone_number": '+71112223344',
    'delivery_date': OrderPageLocators.CALENDAR_DATE_TOMORROW,
    'rental_period': OrderPageLocators.RENTAL_PERIOD_2_DAYS,
    "comment": 'За Орду!'
}
class Data:
    WAIT_TIME = 20
class ExpectedText:
    ORDER_CREATED_TEXT = 'Заказ оформлен'

class Answers:
    ANSWER_0 = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    ANSWER_1 = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
    ANSWER_2 = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
    ANSWER_3 = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    ANSWER_4 = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    ANSWER_5 = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
    ANSWER_6 = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
    ANSWER_7 = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'