from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

        self.delay_input = (By.ID, "delay")
        self.button_7 = (By.XPATH, "//span[text()='7']")
        self.button_8 = (By.XPATH, "//span[text()='8']")
        self.button_plus = (By.XPATH, "//span[text()='+']")
        self.button_equals = (By.XPATH, "//span[text()='=']")
        self.screen = (By.CLASS_NAME, "screen")

    def open(self):
        """Открывает страницу калькулятора."""
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    def set_delay(self, delay):
        """Устанавливает задержку для эмуляции медленной работы UI."""
        element = self.wait.until(EC.element_to_be_clickable(self.delay_input))
        element.clear()
        element.send_keys(delay)

    def click_button_7(self):
        """Нажимает кнопку 7."""
        self.wait.until(EC.element_to_be_clickable(self.button_7)).click()

    def click_button_8(self):
        """Нажимает кнопку 8."""
        self.wait.until(EC.element_to_be_clickable(self.button_8)).click()

    def click_plus(self):
        """Нажимает кнопку +."""
        self.wait.until(EC.element_to_be_clickable(self.button_plus)).click()

    def click_equals(self):
        """Нажимает кнопку =."""
        self.wait.until(EC.element_to_be_clickable(self.button_equals)).click()

    def get_result(self):
        """Возвращает текст результата."""

        self.wait.until(
            lambda driver: self.driver.find_element(*self.screen).text == "15"
        )
        element = self.wait.until(
            EC.visibility_of_element_located(self.screen)
            )
        return element.text

    def perform_calculation_7_plus_8(self):
        """Выполняет последовательность 7 + 8 =."""
        self.click_button_7()
        self.click_plus()
        self.click_button_8()
        self.click_equals()
