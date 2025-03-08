from selenium.webdriver.common.by import By
from data_day import DataDay

class OrderPageLocators:
    #Для кого самокат
    COOKIE_ACCEPT_BUTTON = [By.CSS_SELECTOR, 'div[class^=App_CookieConsent] button']
    NAME_FIELD = [By.CSS_SELECTOR, '[class^=Order_Form] [class^=Input_InputContainer]:nth-child(1) input']
    LAST_NAME_F = [By.CSS_SELECTOR, '[class^=Order_Form] [class^=Input_InputContainer]:nth-child(2) input']
    ADDRESS_F = [By.CSS_SELECTOR, '[class^=Order_Form] [class^=Input_InputContainer]:nth-child(3) input']
    METRO_FIELD = [By.CSS_SELECTOR, '[class^=Order_Form] .select-search input']
    STATION_NAME = [By.XPATH, '//div[@class="select-search__select"]//div[text()="Лубянка"]']
    PHONE_FIELD = [By.CSS_SELECTOR, '[class^=Order_Form] [class^=Input_InputContainer]:nth-child(5) input']

    #Кнопка "Далее" страницы заказа
    FURTHER_BUTTON = [By.CSS_SELECTOR, '[class^=Order_NextButton] button']

    #Об аренде
    INPUT_DELIVERY_DATE = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    CALENDAR_DATE_TODAY = [By.XPATH, f'//div[contains(@class,"react-datepicker__day--0{DataDay.get_delivery_day_today}")]']
    CALENDAR_DATE_TOMORROW = [By.XPATH, f'//div[contains(@class,"react-datepicker__day--0{DataDay.get_delivery_day_tomorrow()}")]']
    FIELD_RENT_LIMIT = [By.XPATH, "//div[@class='Dropdown-placeholder']"]
    DROPDOWN_RENT_1st_POSITION = [By.XPATH, "(//div[@class='Dropdown-option'])[1]"]
    RENTAL_PERIOD_1_DAY = [By.XPATH, "(//div[@class='Dropdown-option'])[1]"]
    RENTAL_PERIOD_2_DAYS = [By.XPATH, "(//div[@class='Dropdown-option'])[2]"]
    INPUT_CHECKBOX_COLOR_BLACK = [By.XPATH, "//input[@id='black']"]
    COMMENT_FIELD = [By.CSS_SELECTOR, 'input[placeholder~=Комментарий]']

    #Заказать
    ORDER_BUTTON_ORDER_PAGE = [By.CSS_SELECTOR, '[class^=Order_Buttons] button:last-child']

    #Подтвердить
    CONFIRMATION_BUTTON = [By.CSS_SELECTOR, '[class^=Order_Modal] [class^=Order_Buttons] button:last-child']
    STATUS_BUTTON = [By.CSS_SELECTOR, '[class^=Order_NextButton] button']
    ORDER_DONE = (By.XPATH, ".//div[text()='Заказ оформлен']")