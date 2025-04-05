import pytest
import allure
import curl
from data import dropdown_list
from pages.base_page import BasePage
from pages.main_page import MainPage


class TestDropdownList:

    @allure.title('Проверка ответов на вопросы на экране "Вопросы о важном"')
    @allure.description('Нажимаем на элемент выпадающего списка и проверяем корректность ответов')
    @pytest.mark.parametrize('question_number, answer_number, answer_text', dropdown_list)
    def test_questions_in_dropdown_list(self, driver, question_number, answer_number, answer_text):

        base_page = BasePage(driver)
        base_page.load_page(curl.MAIN_PAGE_URL)
        main_page = MainPage(driver)
        main_page.click_on_the_question(question_number)
        text = main_page.text_in_question(answer_number)
        assert text == answer_text
