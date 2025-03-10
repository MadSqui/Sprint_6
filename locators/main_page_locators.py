from selenium.webdriver.common.by import By
from data_day import DataDay

class MainPageLocators:
    ORDER_BUTTON_TOP = [By.CSS_SELECTOR, '[class^=Header_Nav] button']
    ORDER_BUTTON_BELOW = [By.CSS_SELECTOR, '[class^=Home_FinishButton] button']
    FAQ_LINK = [By.CSS_SELECTOR, '[class^=Home_FourPart] [class^=Home_SubHeader]']
    SCOOTER_LINK = [By.CSS_SELECTOR, '[class^=Header_Logo] [class^=Header_LogoScooter]']
    YANDEX_LINK = [By.CSS_SELECTOR, '[class^=Header_Logo] [class^=Header_LogoYandex]']
    PAGE = [By.CSS_SELECTOR, '[class^=Home_FourPart]']
    LOGO_YANDEX = By.XPATH, '//*[@href = "//yandex.ru"]'
    BUTTON_FIND = By.XPATH, '//*[text() = "Найти"]'
    COOKIE = By.XPATH, '//button[text() = "да все привыкли"]'
    QUESTION = By.XPATH, '//div[@id = "accordion__heading-{}"]'
    QUESTION_LAST = By.XPATH, '//div[@id = "accordion__heading-7"]'
    ANSWER = By.XPATH, '//div[@id = "accordion__panel-{}"]'

    @staticmethod
    def question_number(question):
        return By.CSS_SELECTOR, f'.accordion .accordion__item:nth-child({question}) .accordion__heading div'

    @staticmethod
    def answer_number(answer):
        return By.CSS_SELECTOR, f'.accordion .accordion__item:nth-child({answer}) .accordion__panel'