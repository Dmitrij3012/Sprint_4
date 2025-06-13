from selenium.webdriver.common.by import By


class MainPageLocators:

    ORDER_BUTTON_IN_HEADER = (
        By.CLASS_NAME,
        'Button_Button__ra12g'
    )
    ORDER_BUTTON = (
        By.CSS_SELECTOR,
        '.Button_Button__ra12g.Button_Middle__1CSJM'
    )
    SAMOKAT_LOGO = (
        By.CLASS_NAME,
        'Header_LogoScooter__3lsAR'
    )
    YANDEX_LOGO = (
        By.CLASS_NAME,
        'Header_LogoYandex__3TSOI'
    )

    @staticmethod
    def question(number):
        return By.ID, f'accordion__heading-{number}'

    @staticmethod
    def answer(number):
        return By.XPATH, f'//div[@id="accordion__panel-{number}"]/p'

