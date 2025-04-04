import allure
import curl
from pages.main_page import MainPage


class TestTransition:

    @allure.title('Проверка перехода на главную страницу по клику на логотип "Самокат"')
    @allure.description('Кликаем на логотип "Самокат" и проверяем, что переходим на главную страницу "Яндекс.Самокат"')
    def test_scooter_logo(self, driver):
        driver.get(curl.MAIN_PAGE_URL)
        main_page = MainPage(driver)
        main_page.click_on_scooter_logo()

        assert driver.current_url == curl.MAIN_PAGE_URL

    @allure.title('Проверка перехода на главную страницу "Дзен" по клику на логотип "Яндекс"')
    @allure.description('Кликаем на логотип "Яндекс" и проверяем, что переходим на главную страницу "Дзен"')
    def test_yandex_logo(self, driver):
        driver.get(curl.MAIN_PAGE_URL)
        main_page = MainPage(driver)
        main_page.click_on_yandex_logo('Дзен')

        assert driver.current_url == curl.DZEN_MAIN_PAGE_URL
