import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestSauceDemo:
    @pytest.fixture
    def driver(self):
        
        options = Options()
        options.add_argument('--start-maximized')
        
        
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
        driver.implicitly_wait(10)
        
        yield driver
        driver.quit()

    def test_checkout_total_amount(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        inventory_page.add_all_items_to_cart()
        inventory_page.go_to_cart()
        cart_page.click_checkout()
        checkout_page.fill_checkout_info("Михаил", "Савельев", "662606")
        total_amount = checkout_page.get_total_amount()
        
        assert total_amount == 58.29, f"Ожидалось 58.29, получено {total_amount}"