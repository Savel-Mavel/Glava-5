import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from calculator_page import SlowCalculatorPage


class TestSlowCalculator:
    @pytest.fixture
    def driver(self):
        
        options = Options()
        options.add_argument('--start-maximized')
        
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)
        yield driver
        driver.quit()

    def test_slow_calculator_7_plus_8_equals_15(self, driver):
        page = SlowCalculatorPage(driver)
        page.open()
        page.set_delay("45")
        page.perform_calculation_7_plus_8()
        result = page.get_result()
        assert result == "15", f"Ожидалось 15, получено {result}"