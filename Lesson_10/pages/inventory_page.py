from selenium.webdriver.common.by import By

class InventoryPage:
    SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def add_product_by_name(self, product_name: str):
        product_id = product_name.lower().replace(" ", "-")
        locator = (By.ID, f"add-to-cart-{product_id}")
        self.driver.find_element(*locator).click()

    def go_to_cart(self):
        self.driver.find_element(*self.SHOPPING_CART).click()