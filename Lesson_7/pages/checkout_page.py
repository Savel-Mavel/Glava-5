from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_checkout_info(self, first_name, last_name, postal_code):
        
        self.wait.until(EC.element_to_be_clickable(self.first_name_input)).send_keys(first_name)
        self.wait.until(EC.element_to_be_clickable(self.last_name_input)).send_keys(last_name)
        self.wait.until(EC.element_to_be_clickable(self.postal_code_input)).send_keys(postal_code)
        self.wait.until(EC.element_to_be_clickable(self.continue_button)).click()

    def get_total_amount(self):
        
        self.wait.until(EC.visibility_of_element_located(self.total_label))
        total_text = self.driver.find_element(*self.total_label).text
        
        total_amount = total_text.replace("Total: $", "")
        return float(total_amount)