from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        
        self.backpack_add_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.bolt_tshirt_add_button = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.onesie_add_button = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack_to_cart(self):
        
        self.wait.until(EC.element_to_be_clickable(self.backpack_add_button)).click()

    def add_bolt_tshirt_to_cart(self):
        
        self.wait.until(EC.element_to_be_clickable(self.bolt_tshirt_add_button)).click()

    def add_onesie_to_cart(self):
        
        self.wait.until(EC.element_to_be_clickable(self.onesie_add_button)).click()

    def add_all_items_to_cart(self):
        
        self.add_backpack_to_cart()
        self.add_bolt_tshirt_to_cart()
        self.add_onesie_to_cart()

    def go_to_cart(self):
        
        self.wait.until(EC.element_to_be_clickable(self.cart_icon)).click()