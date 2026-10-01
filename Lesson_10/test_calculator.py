import time
import allure
from allure_commons.types import Severity
from calculator_page import SlowCalculatorPage


@allure.feature("Калькулятор")
@allure.story("Арифметические операции")
@allure.title("Тест сложения с задержкой: 7 + 8 = 15")
@allure.description("""
    Проверка работы калькулятора с настраиваемой задержкой.
    Устанавливается задержка 45 секунд, затем выполняется операция 7 + 8.
    Результат должен быть 15.
""")
@allure.severity(Severity.CRITICAL)
def test_calculator_with_delay(chrome_driver):
    calc = SlowCalculatorPage(chrome_driver)

    with allure.step("Открыть страницу калькулятора"):
        calc.open()

    with allure.step("Установить задержку 45 секунд"):
        calc.set_delay(45)

    with allure.step("Нажать кнопку '7'"):
        calc.click_button_7()

    with allure.step("Нажать кнопку '+'"):
        calc.click_plus()

    with allure.step("Нажать кнопку '8'"):
        calc.click_button_8()

    with allure.step("Нажать кнопку '='"):
        calc.click_equals()

    with allure.step("Ожидание 46 секунд (больше задержки)"):
        time.sleep(46)

    with allure.step("Получить результат с экрана"):
        result = calc.get_result()

    with allure.step("Проверить, что результат равен '15'"):
        assert result == "15", f"Ожидался результат 15, получен {result}"