# Проект автоматизации тестирования с Allure

## Структура проекта

lesson_10/
├── pages/ # Page Object классы
│ ├── login_page.py
│ ├── inventory_page.py
│ ├── cart_page.py
│ └── checkout_page.py
├── conftest.py # Фикстуры для браузеров
├── calculator_page.py # Страница калькулятора
├── test_calculator.py # Тесты калькулятора
├── test_saucedemo.py # Тесты интернет-магазина
├── requirements.txt # Зависимости


## Установка зависимостей

pip install -r requirements.txt

Запуск тестов с Allure

1. Запустить тесты и сохранить результаты
pytest . --alluredir=./allure-results -v

2. Сгенерировать HTML отчёт
allure generate ./allure-results -o ./allure-report --clean

3. Открыть отчёт в браузере
allure open ./allure-report

