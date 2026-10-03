import allure
from allure_commons.types import Severity
from selenium.webdriver.support.ui import WebDriverWait
from calculator_page import SlowCalculatorPage


@allure.feature("Калькулятор")
@allure.story("Арифметические операции")
@allure.title("Тест сложения: 7 + 8 = 15")
@allure.description(
    "Проверка работы калькулятора без выставления таймера с задания №7."
)
@allure.severity(Severity.CRITICAL)
def test_calculator_addition(chrome_driver):
    calc = SlowCalculatorPage(chrome_driver)
    wait = WebDriverWait(chrome_driver, timeout=15)

    with allure.step("Открыть страницу калькулятора"):
        calc.open()

    with allure.step("Нажать кнопку '7'"):
        calc.click_button_7()

    with allure.step("Нажать кнопку '+'"):
        calc.click_plus()

    with allure.step("Нажать кнопку '8'"):
        calc.click_button_8()

    with allure.step("Нажать кнопку '='"):
        calc.click_equals()

    with allure.step("Получить результат (ожидание до 15 сек)"):
        # Возвращаем сам результат, а не сравнение
        result = wait.until(
            lambda d: calc.get_result(),
            message="Не удалось получить значение результата"
            "в течение таймаута",
        )

    with allure.step("Проверить, что результат равен '15'"):
        assert result == "15", f"Ожидался результат 15, получен {result}"
