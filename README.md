#### <h1>Финальный проект 6 спринта</h1>
<hr>

#### <h3>Студент: Дмитрий Соловьев</h2>
#### <h3>Когорта: #18</h2>
<hr>

#### <h1>Тестирование Яндекс:Самокат</h1>

#### <h2>Инструкция по запуску:</h>

### 1. Установить зависимости:

> pip install -r requirements.txt</h>

### 2. Запустить все тесты и записать отчет:

> pytest --alluredir=./allure-results

### <h>3. Посмотреть отчет по тестированию</h>

> allure serve ./allure-results

<hr>

<h3 align="left" style="color:green">Project files and description:</h3>

| Название файла                                                 | Содержание файла                                 |
|----------------------------------------------------------------|--------------------------------------------------|
| [tests](tests)                                                 | Директория с тестами                             |
| [test_dropdown_list.py](tests/test_dropdown_list.py)           | Тесты раздела "Вопросы о важном"                 |
| [test_order.py](tests/test_order.py)                           | Тесты заказа самоката                            |
| [test_transition_by_logo.py](tests/test_transition_by_logo.py) | Тесты перехода по логотипам "Самокат" и "Яндекс" |
| [base_page.py](pages/base_page.py)                             | Базовые методы                                   |
| [main_page.py](pages/main_page.py)                             | Методы главной страницы                          |
| [order_page.py](pages/order_page.py)                           | Методы страницы заказа                           |
| [main_page_locators.py](locators/main_page_locators.py)        | Локаторы главной страницы                        |
| [order_page_locators.py](locators/order_page_locators.py)      | Локаторы страницы заказа                         |
| [conftest.py](tests/conftest.py)                               | Фикстуры                                         |
| [generators.py](generators.py)                                 | Генератор данных                                 |
| [config.py](config.py)                                         | Конфигурационные параметры(таймауты и пр.)       |
| [text_constants.py](text_constants.py)                         | Текстовые константы                              |
| [curl.py](curl.py)                                             | Файл с URL                                       |
| [requirements.txt](requirements.txt)                           | Файл с зависимостями                             |
| [allure_results](allure_results)                               | Папка с отчетами Allure                          |
