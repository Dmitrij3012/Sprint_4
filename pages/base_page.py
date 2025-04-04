import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from config import TIMEOUT_VALUE


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Подождать видимость элемента')
    def wait_for_element(self, locator, timeout=TIMEOUT_VALUE):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Подождать кликабельность элемента')
    def wait_for_element_clicked(self, locator, timeout=TIMEOUT_VALUE):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator, timeout=TIMEOUT_VALUE):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Кликнуть на элемент')
    def click_on_element(self, locator, timeout=TIMEOUT_VALUE):
        element = self.wait_for_element_clicked(locator, timeout)
        element.click()

    @allure.step('Ввести текст в поле ввода')
    def send_keys_to_input(self, locator, keys, timeout=TIMEOUT_VALUE):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step('Получить текст элемента')
    def get_text_on_element(self, locator, timeout=TIMEOUT_VALUE):
        element = self.wait_for_element(locator, timeout)
        return element.text

    @allure.step('Подождать и проверить, что атрибут элемента содержит текст')
    def wait_for_attribute(self, locator, attribute, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element_attribute(locator, attribute, value)
        )

    @allure.step('Переключится на другое окно')
    def switch_to_another_window(self, title_contains, timeout=TIMEOUT_VALUE, number_windows=2):
        original_window = self.driver.current_window_handle
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.number_of_windows_to_be(number_windows))
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
        wait.until(EC.title_contains(title_contains))
