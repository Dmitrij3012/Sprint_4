import pytest
import allure
import curl
import text_constants as const
from pages.main_page import MainPage


class TestDropdownList:

    @allure.title('Проверка ответов на вопросы на экране "Вопросы о важном"')
    @allure.description('Нажимаем на элемент выпадающего списка и проверяем корректность ответов')
    @pytest.mark.parametrize(
        'question_number, answer_number, answer_text',
        [
            ['0', '0', const.TEXT_1],
            ['1', '1', const.TEXT_2],
            ['2', '2', const.TEXT_3],
            ['3', '3', const.TEXT_4],
            ['4', '4', const.TEXT_5],
            ['5', '5', const.TEXT_6],
            ['6', '6', const.TEXT_7],
            ['7', '7', const.TEXT_8],
        ]
    )
    def test_questions_in_dropdown_list(self, driver, question_number, answer_number, answer_text):
        driver.get(curl.MAIN_PAGE_URL)
        main_page = MainPage(driver)
        main_page.click_on_the_question(question_number)
        text = main_page.text_in_question(answer_number)
        assert text == answer_text
