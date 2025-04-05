import allure
import curl
from pages.base_page import BasePage
from pages.main_page import MainPage


class TestTransition:

    @allure.title('Проверка перехода на главную страницу по клику на логотип "Самокат"')
    @allure.description('Кликаем на логотип "Самокат" и проверяем, что переходим на главную страницу "Яндекс.Самокат"')
    def test_scooter_logo(self, driver):
        base_page = BasePage(driver)
        base_page.load_page(curl.MAIN_PAGE_URL)
        main_page = MainPage(driver)
        main_page.click_on_scooter_logo()
        url = base_page.return_url()

        assert url == curl.MAIN_PAGE_URL

    @allure.title('Проверка перехода на главную страницу "Дзен" по клику на логотип "Яндекс"')
    @allure.description('Кликаем на логотип "Яндекс" и проверяем, что переходим на главную страницу "Дзен"')
    def test_yandex_logo(self, driver):
        base_page = BasePage(driver)
        base_page.load_page(curl.MAIN_PAGE_URL)
        main_page = MainPage(driver)
        main_page.click_on_yandex_logo('Дзен')
        url = base_page.return_url()

        assert url == curl.DZEN_MAIN_PAGE_URL
