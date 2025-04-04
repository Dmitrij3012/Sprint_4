from selenium.webdriver.common.by import By


class OrderPageLocators:

    NEXT_BUTTON = (
        By.XPATH,
        "//button[text()='Далее']"
    )
    ORDER_BUTTON = (
        By.XPATH,
        "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']"
    )
    ORDER_CONFIRMATION = (
        By.XPATH,
        "//div[text()='Хотите оформить заказ?']"
    )
    ORDER_CONFIRMATION_BUTTON = (
        By.XPATH,
        "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']"
    )
    ORDER_SUCCESSFUL = (
        By.XPATH,
        "//div[contains(text(), 'Заказ оформлен')]"
    )
    NAME_FIELD = (
        By.XPATH,
        "//input[@placeholder='* Имя']"
    )
    SURNAME_FIELD = (
        By.XPATH,
        "//input[@placeholder='* Фамилия']"
    )
    ADDRESS_FIELD = (
        By.XPATH,
        "//input[@placeholder='* Адрес: куда привезти заказ']"
    )
    METRO_FIELD = (
        By.CLASS_NAME,
        'select-search__input'
    )
    METRO_FIELD_SELECT = (
        By.XPATH,
        "//div[@class='select-search__select']"
    )
    PHONE_FIELD = (
        By.XPATH,
        "//input[@placeholder='* Телефон: на него позвонит курьер']"
    )
    DATE_FIELD = (
        By.XPATH,
        "//input[@placeholder='* Когда привезти самокат']"
    )

    @staticmethod
    def choose_date(day):
        return By.XPATH, f'//div[contains(@class, "react-datepicker__day") and text()={day}]'

    RENTAL_FIELD = (
        By.CLASS_NAME,
        'Dropdown-root'
    )

    @staticmethod
    def rental_value(days):
        return By.XPATH, f'//div[text()="{days}"]'

    @staticmethod
    def color_field(color):
        return By.ID, f'{color}'

    COMMENT_FIELD = (
        By.XPATH,
        "//input[@placeholder='Комментарий для курьера']"
    )
